from ...contracts.encrypt import ICanSaving


class StegosphereImageContainer(ICanSaving):
    def __init__(self, img, pixels):
        self._pixels = pixels
        self._img = img


    def save(self, output_path: str) -> None:
        self._img.save(output_path, self._pixels)
