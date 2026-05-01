# from stegano import lsb

from cylmore_steganography_kit.src.cylmore_steganography_kit.encrypt import IFileMaskingNode, ICanSaving


class LsbSteganoMasking(IFileMaskingNode):
    def hide(self, file_path: str, message: str) -> ICanSaving:
        pass

    def reveal(self, carrier_path: str) -> str:
        pass