from ...contracts.encrypt import ICanSaving


class SteganoImageContainerg(ICanSaving):
    def __init__(self, data):
        self._data = data

    def save(self, output_path: str) -> None:
        pass

