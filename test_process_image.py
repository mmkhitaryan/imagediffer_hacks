import pickle
from process_image import extract_images, show_two_images_diff

def extract_image_from_response():
    img22 = pickle.load( open( "tests/img22", "rb" ) )
    return extract_images(img22)

def test_hologram_process():
    extractedimages = extract_image_from_response()
    show_two_images_diff(*extractedimages)
    show_two_images_diff(*extractedimages)
