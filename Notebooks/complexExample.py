#!/usr/bin/env python3

# First we need to get a list of the images that are available.
baseDir = "."
imageSizeDesired = ["small","normal"] # options are "small" or "normal"
sleepPeriod = 0.2

import requests
import xmltodict
import os 
import shutil
from time import sleep
import datetime
import glob
from PIL import Image
import logging
import concurrent.futures

logger = logging.getLogger(__name__)
logfilename = f"{baseDir}/satelliteImages/{datetime.date.today().strftime('%Y%m%d')}.log"
logging.basicConfig(filename=logfilename,level=logging.INFO,format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger.info(f"Starting processing")
# set the user agent
headers = {
    'User-Agent': 'https://github.com/dfbr/pythonLessons',
    'From': 'dave@dfbr.co.uk'  # This is another valid field
}

# next we use the "get" method to retrieve a list of the available images
# logger.info(f'Getting https://api.met.no/weatherapi/geosatellite/1.4/available')
try:
    response = requests.get("https://api.met.no/weatherapi/geosatellite/1.4/available",headers=headers)
except Exception as e:
    logger.exception(f"Failed getting https://api.met.no/weatherapi/geosatellite/1.4/available with status code {response.status_code}: {e}")
    exit()
logger.info(f'Got https://api.met.no/weatherapi/geosatellite/1.4/available with status code {response.status_code}')
availableImages = xmltodict.parse(response.content)

# now let's get the fields...
fields = {}

# now we loop through the list of images
for image in availableImages['available']['query']:

    # and within each image we want to look at the parameters
    for detail in image['parameter']:
        
        # if we haven't seen the key before, 
        # add it as an array to the fields dictionary
        # with the value as the first element
        if detail['name'] not in fields.keys():
            fields[detail['name']] = [detail['value']]

        # if we have seen it before, add the value if it's
        # not already in the array
        elif detail['value'] not in fields[detail['name']]:
            fields[detail['name']].append(detail['value'])

#region make directories if they don't already exist
path = os.path.join(baseDir,"satelliteImages")
if not os.path.exists(path):
    try:
        os.mkdir(path)
        logger.info(f"Created directory {path}")
    except Exception as e:
        logger.exception(f"Failed to create directory {path}: {e}")
        exit()
for size in imageSizeDesired:
    path = os.path.join(baseDir,"satelliteImages", size)
    if not os.path.exists(path):
        try:
            os.mkdir(path)
            logger.info(f"Created directory {path}")
        except Exception as e:
            logger.exception(f"Failed to create directory {path}: {e}")
            exit()
    for area in fields['area']:
        path = os.path.join(baseDir,"satelliteImages", size, area)
        if not os.path.exists(path):
            try:
                os.mkdir(path)
                logger.info(f"Created directory {path}")
            except Exception as e:
                logger.exception(f"Failed to create directory {path}: {e}")
                exit()
            logger.info(f"Created directory {path}")
        for spectrum in fields['type']:
            path = os.path.join(baseDir,"satelliteImages", size, area, spectrum)
            if not os.path.exists(path):
                try:
                    os.mkdir(path)
                    logger.info(f"Created directory {path}")
                except Exception as e:
                    logger.exception(f"Failed to create directory {path}: {e}")
                    exit()
#endregion

newFiles = False
for image in availableImages['available']['query']:
    # for ease let us make some shorthand variable names
    area = image['parameter'][0]['value']
    imageSize = image['parameter'][1]['value']
    imageDate = image['parameter'][2]['value'].replace(":","")
    imageType = image['parameter'][3]['value']
    imageUrl = image['uri']

    # now we download the image, but only the larger images...
    if imageSize in imageSizeDesired:
        # if we run this often, we might already have the file, so let's check for that first...
        filename = f'{baseDir}/satelliteImages/{imageSizeDesired[imageSizeDesired.index(imageSize)]}/{area}/{imageType}/{imageDate}.png'
        if not os.path.exists(filename):
            newFiles = True
            try:
                # met.no don't like too many requests at a time so
                # we make our program wait half a second after each file
                sleep(sleepPeriod)
                response = requests.get(imageUrl, stream=True, headers=headers)
            except Exception as e:
                logger.exception(f"Error downloading {imageUrl}, got {response.status_code}")
                print(f"Error downloading {imageUrl}, got {response.status_code}")
                pass
            logger.info(f"Got {imageUrl} with status code {response.status_code}")

            if response.ok:         
                with open(filename, 'wb') as out_file:
                    response.raw.decode_content = True
                    shutil.copyfileobj(response.raw, out_file)
                logger.info(f"Wrote {imageUrl} to {filename}")

def makeAnimatedGifFromPngsInDirectory(directory):
    # first we get a list of all the png images in the directory
    # because of the date format, we know they will be returned
    # in date order. This is _handy_!
    logger.info(f"Creating animated GIF for {directory}")
    pngImages = glob.glob(os.path.join(directory, '*.png'))
    logger.info(f"Found {len(pngImages)} in {directory}")

    if len(pngImages) > 0:
        # now create one frame for each PNG image
        frames = []

        for i in pngImages[-200:]:
            try:
                new_frame = Image.open(i)
                frames.append(new_frame)
            except Exception as e:
                logger.exception(f"Got exception trying to add an image frame: {e}")

        # Save into a GIF file that loops forever
        animatedGifFilename = f'{directory}/animated.gif'
        # print(animatedGifFilename)
        try:
            frames[0].save(animatedGifFilename, format='GIF',
                        append_images=frames[1:],
                        save_all=True,
                        duration=300, loop=0, subrectangles=True)
            logger.info(f"Finished creating animated gif {animatedGifFilename}")
        except Exception as e:
            logger.exception(f"Failed to create {animatedGifFilename}")
            return False
        return animatedGifFilename
    else:
        return False
    
# now we can run our function on each of our directories.
if newFiles:
    directories = []
    for area in fields['area']:
        for spectrum in fields['type']:
            for imageSize in imageSizeDesired:
                directories.append(f"{baseDir}/satelliteImages/{imageSize}/{area}/{spectrum}")
                # print(f"{baseDir}/satelliteImages/{imageSize}/{area}/{spectrum}")

    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = list(executor.map(makeAnimatedGifFromPngsInDirectory,directories))


htmlHeader = f"""
<html>
  <head>
    <title>Satellite Images</title>
  </head>
  <body>
  <h1>Satellite images from Met.no, updated {datetime.datetime.now().strftime('%A %d %B %Y, %H:%M:%S')}</h1>
"""
htmlFooter = """
  </body>
</html>
"""
htmlContent = ""

for area in fields['area']:
    for spectrum in fields['type']:
        normalExists = os.path.exists(f"satelliteImages/{imageSizeDesired[1]}/{area}/{spectrum}/animated.gif")
        smallExists = os.path.exists(f"satelliteImages/{imageSizeDesired[0]}/{area}/{spectrum}/animated.gif")
        if normalExists:
          linkHref = (f"normal/{area}/{spectrum}/animated.gif")
        else:
          linkHref = (f"small/{area}/{spectrum}/animated.gif")
        if smallExists:
          htmlContent += f"""
          <h2>{area} image in {spectrum} spectrum</h2>
          <center>
            <a href="{linkHref}">
              <img src="small/{area}/{spectrum}/animated.gif" alt="{area} image in {spectrum} spectrum">
            </a>
          </center>
          <br />
          """

# now we want to combine our html
overallHtml = htmlHeader + htmlContent + htmlFooter

# then write it to a file
logger.info(f"Writing html to {baseDir}/satelliteImages/index.html")
with open(f"{baseDir}/satelliteImages/index.html", "w") as html_file:
    html_file.write(overallHtml)
logger.info(f"Wrote html to {baseDir}/satelliteImages/index.html")
