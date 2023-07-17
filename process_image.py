import io
import tempfile
import webbrowser

from PIL import Image
from PIL import ImageFile
from PIL import ImageFilter
from PIL import ImageChops 


ImageFile.LOAD_TRUNCATED_IMAGES = True

def open_numpy_array_in_browser(pil_image):
    temp_file = tempfile.NamedTemporaryFile(dir="./tempimages", delete=False, suffix='.png')

    pil_image.save(temp_file.name)

    webbrowser.open(temp_file.name)

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
    im1 = Image.open(io.BytesIO(image1))
    pil_image1 = im1.filter(ImageFilter.GaussianBlur(radius = 3))

    im2 = Image.open(io.BytesIO(image2))
    pil_image2 = im2.filter(ImageFilter.GaussianBlur(radius = 3))

    buffer3 = ImageChops.difference(pil_image1, pil_image2)

    open_numpy_array_in_browser(buffer3)
