from mitmproxy import ctx
from process_image import extract_images, show_two_images_diff

class ZaebombaDump:
    async def response(self, flow):
        if 'images/pics' in flow.request.path:            
            show_two_images_diff(*extract_images(flow.response.raw_content))


addons = [
    ZaebombaDump()
]
