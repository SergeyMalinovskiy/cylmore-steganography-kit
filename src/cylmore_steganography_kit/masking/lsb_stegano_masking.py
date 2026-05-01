from stegano import lsb

from cylmore_steganography_kit.src.cylmore_steganography_kit.encrypt import IFileMaskingNode, ICanSaving


class LsbSteganoMasking(IFileMaskingNode):
    def hide(self, file_path: str, message: str) -> ICanSaving:
        return lsb.hide(file_path, message)

    def reveal(self, carrier_path: str) -> str:
        return lsb.reveal(carrier_path)