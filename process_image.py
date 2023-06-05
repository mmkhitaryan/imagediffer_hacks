import io
import tempfile
import webbrowser

from PIL import Image
from PIL import ImageFile

import numpy as np
from skimage.metrics import structural_similarity

ImageFile.LOAD_TRUNCATED_IMAGES = True

def open_numpy_array_in_browser(numpy_array):
    file = tempfile.NamedTemporaryFile()

    filled_img = Image.fromarray(numpy_array)
    filled_img.save(file, 'png')

    webbrowser.open(file.name)

def extract_images(response_raw):
    newline_pos = response_raw.find(b'\r\n')
    number_in_raw_binary = response_raw[0:newline_pos]
    skip_numbers = newline_pos+2

    image_size = int(number_in_raw_binary, base=16)

    first_chunk_with = response_raw[skip_numbers:image_size] # without

    second_chunk = response_raw[image_size:]

    second_chunk_newline_pos = second_chunk.find(b'\r\n')
    second_chunk_skip_numbers = second_chunk_newline_pos+2

    second_chunk_with = second_chunk[second_chunk_skip_numbers:]

    return (first_chunk_with, second_chunk_with)

def show_two_images_diff(image1, image2):
    # Код был взят с
    # https://stackoverflow.com/a/32264327/7415288
    # https://stackoverflow.com/a/56193442/7415288

    pil_image1 = Image.open(io.BytesIO(image1))

    pil_image2 = Image.open(io.BytesIO(image2))

    before = np.array(pil_image1)
    after = np.array(pil_image2)

    # Compute SSIM between two images
    (score, diff) = structural_similarity(before, after, multichannel=True, full=True)
    print("Image similarity", score)

    # The diff image contains the actual image differences between the two images
    # and is represented as a floating point data type in the range [0,1] 
    # so we must convert the array to 8-bit unsigned integers in the range
    # [0,255] before we can use it with OpenCV
    diff = (diff * 255).astype("uint8")

    open_numpy_array_in_browser(diff)
