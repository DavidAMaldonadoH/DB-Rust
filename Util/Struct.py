from Util import Symbol


class Struct:
    def __init__(self, name: str):
        self.name = name
        self.items = dict()

    def __getitem__(self, key: str) -> Symbol:
        return self.items[key]

    def __setitem__(self, key: str, value: Symbol):
        self.items[key] = value
