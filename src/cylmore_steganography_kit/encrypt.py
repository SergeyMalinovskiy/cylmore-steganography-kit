from abc import ABC, abstractmethod
from enum import Enum


class DataType(Enum):
    Raw = 1
    Image = 2
    Text = 3

class ICanSaving(ABC):
    @abstractmethod
    def save(self, output_path: str) -> None:
        pass


class IFileMaskingNode(ABC):
    @abstractmethod
    def hide(self, file_path: str, message: str) -> ICanSaving:
        pass

    @abstractmethod
    def reveal(self, carrier_path: str) -> str:
        pass


class ICanHideDataToCarrier(ABC):
    @abstractmethod
    def hide_data(self, data: bytes, carrier_path: str, output_path: str, data_type: DataType = DataType.Raw) -> None:
        pass


class ICanExtractDataFromCarrier(ABC):
    @abstractmethod
    def extract_data(self, carrier: str) -> bytes:
        pass
