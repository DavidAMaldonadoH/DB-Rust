from Util import Symbol


class Struct:
    def __init__(self, name: str, public: bool):
        self.name = name
        self.items = dict()
        self.public = public

    def __getitem__(self, key: str) -> Symbol:
        return self.items[key]

    def __setitem__(self, key: str, value: Symbol):
        self.items[key] = value
