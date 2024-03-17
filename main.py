import io
import json
from PIL import Image

from imgProcessor import insertNamesToImage


def readPickData():
    with open('pickData.json', 'r') as file:
        bracket_data = json.load(file)
        return bracket_data


def getLocalImageData():
    with open('wide.png', 'rb') as file:
        return file.read()


def getLocalFontData():
    with open('Poppins-Regular.ttf', 'rb') as file:
        return file.read()


def getLocalChampionFontData():
    with open('Poppins-SemiBold.ttf', 'rb') as file:
        return file.read()


# Load local image data
imageData = getLocalImageData()

# Open the image using PIL
image = Image.open(io.BytesIO(imageData))

# Insert names into the image
fontData = getLocalFontData()
championFontData = getLocalChampionFontData()
pickData = readPickData()
newImageData = insertNamesToImage(imageData, pickData, fontData, championFontData)
# Create a new image using the returned pixel data
width, height = image.size
newImage = Image.new('RGB', (width, height))
newImage.putdata(newImageData)
# Display the edited image
newImage.show()
