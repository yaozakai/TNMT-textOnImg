import io

import functions_framework

from google.cloud import storage

from markupsafe import escape
from PIL import Image, ImageDraw, ImageFont
from flask import Response, json
from imgProcessor import insertNamesToImage


@functions_framework.http
def createBracketImage(request):

    pickData = request.get_json(silent=True)

    imageData = getBucketImageData()

    fontData = getBucketFontData()
    championFontData = getBucketFontData(True)

    newImageData = insertNamesToImage(imageData, pickData, fontData, championFontData)

    # Get width and height of the input image
    input_image = Image.open(io.BytesIO(imageData))
    width, height = input_image.size

    # Construct the image with the same dimensions as the input
    image = Image.new('RGB', (width, height))
    image.putdata(newImageData)

    # Save the image to a BytesIO buffer in PNG format
    png_data = io.BytesIO()
    image.save(png_data, format='PNG')
    png_data.seek(0)

    # Return the image data as a response with appropriate MIME type
    return Response(png_data.getvalue(), mimetype='image/png')


def readPickData():
    with open('pickData.json', 'r') as file:
        bracket_data = json.load(file)
        return bracket_data


def getBucketImageData():
    storage_client = storage.Client()

    bucket = storage_client.bucket('gcf-v2-sources-533385044602-us-central1')
    blob = bucket.blob('createBracketImage/wide.png')

    # Download the image file as a string
    image_data = blob.download_as_string()

    # Open the image using PIL
    return image_data


def getBucketFontData(champ=False):
    storage_client = storage.Client()
    if champ:
        bucket = storage_client.bucket('gcf-v2-sources-533385044602-us-central1')
        blob = bucket.blob('createBracketImage/Poppins-SemiBold.ttf')
    else:
        bucket = storage_client.bucket('gcf-v2-sources-533385044602-us-central1')
        blob = bucket.blob('createBracketImage/Poppins-Regular.ttf')
    # Download the image file as a string
    return blob.download_as_bytes()

