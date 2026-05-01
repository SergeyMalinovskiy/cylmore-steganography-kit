import hashlib

from simple_encryptor import Encryptor

from cylmore_steganography_kit.src.cylmore_steganography_kit.encrypt import ICanHideDataToCarrier, \
    ICanExtractDataFromCarrier, IFileMaskingNode, DataType


class LsbEncodingService(ICanHideDataToCarrier, ICanExtractDataFromCarrier):
    def __init__(self, pkey: str, file_masking_node: IFileMaskingNode):
        self._encryptor = Encryptor(pkey)
        self._masking_node = file_masking_node
        # self._masking_node = lsb

    def _calc_hash(self, data: bytes, data_type: DataType) -> str:
        return hashlib.sha256(data + bytes([data_type.value])).hexdigest()


    def hide_data(self, data: bytes, carrier_path: str, output_path: str, data_type: DataType = DataType.Raw) -> None:
        hex_data = data.hex()
        sha256_hash = self._calc_hash(data, data_type)

        packet = sha256_hash + str(data_type.value) + hex_data

        encrypted_data = self._encryptor.encrypt(packet)
        if encrypted_data is None:
            raise RuntimeError('Encrypted data is empty')

        container = self._masking_node.hide(carrier_path, encrypted_data)

        container.save(output_path)


    def extract_data(self, carrier: str) -> bytes:
        data = self._masking_node.reveal(carrier)

        packet = self._encryptor.decrypt(data)

        sha256_hash = packet[:64]
        data_type = DataType(int(packet[64]))
        hex_data = packet[65:]

        data = bytes.fromhex(hex_data)

        if self._calc_hash(data, data_type) != sha256_hash:
            raise ValueError("Hash mismatch")


        return data
