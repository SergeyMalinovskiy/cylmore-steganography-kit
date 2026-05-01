from stegosphere import image, binary_to_data, data_to_binary
from stegosphere.embeddings import LSB

from cylmore_steganography_kit.src.cylmore_steganography_kit.containers.stegosphere_image_container import \
    StegosphereImageContainer
from cylmore_steganography_kit.src.cylmore_steganography_kit.encrypt import IFileMaskingNode, ICanSaving


class LsbStegosphereMasking(IFileMaskingNode):
    def hide(self, file_path: str, message: str) -> ICanSaving:
        img = image.ImageContainer(file_path)
        pixels = img.read()

        stego_pixels = LSB.embed(pixels, data_to_binary(message))

        return StegosphereImageContainer(img, stego_pixels)

    def reveal(self, carrier_path: str) -> str:
        print(carrier_path)
        stego_img = image.ImageContainer(carrier_path)
        # print(stego_img)
        stego_pixels = stego_img.read()

        extracted_binary = LSB.extract(stego_pixels)

        return binary_to_data(extracted_binary).decode('utf-8')