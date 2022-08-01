from Util.Retorno import Type


class Symbol:
    def __init__(self, id: str, mutable: bool, value: any, type: Type):
        self.id = id
        self.mutable = mutable
        self.value = value
        self.type = type

    def getId(self) -> str:
        return self.id

    def isMutable(self) -> bool:
        return self.mutable

    def getValue(self) -> any:
        return self.value

    def getType(self) -> Type:
        return self.type


class ReportSymbol:
    def __init__(self, id: str, env: str, type: Type, type2: str, line: int, col: int):
        self.id = id
        self.env = env
        self.type = type
        self.type2 = type2
        self.line = line
        self.col = col


SYMBOLS: list[ReportSymbol] = list()
