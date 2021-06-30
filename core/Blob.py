from core import config

class Blob():
    def __init__(self, id: int, type: int):
        self.id = id
        self.type = type
        self.birthday = config.NUM_PASSED_NIGHTS

