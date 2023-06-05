from mitmproxy import ctx
from process_image import extract_images, show_two_images_diff

class ZaebombaDump:
    def __init__(self):
        self.num = 0

    def response(self, flow):
        if flow.request.url=='https://find-vk.zebomba.ru/index.php/img2':
            self.num = self.num + 1
            
            show_two_images_diff(*extract_images(flow.response.raw_content))

            ctx.log.info("We've seen %d flows" % self.num)


addons = [
    ZaebombaDump()
]
