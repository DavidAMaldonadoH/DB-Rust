from Util.Error import ERRORS_, Error
from Util.Retorno import Type
from Util.Symbol import Symbol


class Array:
    def __init__(self, type: Type, size: int):
        self.type = type
        self.size = size
        self.data: list[Symbol] = []

    def getType(self) -> Type:
        return self.type

    def getNestedType(self) -> str:
        if self.type == Type.Array:
            return str(self.size) + "*" + self.data[0].getValue().getNestedType()
        else:
            if self.type == Type.Struct:
                return str(self.size) + "*" + self.data[0].getValue().name
            return str(self.size) + "*" + self.type.fullname

    def getValue(self, index: int) -> Symbol:
        return self.data[index]

    def appendValue(self, value: Symbol):
        if self.size == len(self.data):
            err = Error(self.line, self.column, "Array overflow", "Array")
            ERRORS_.append(err)
            raise Exception(err)
        else:
            self.data.append(value)

    def setValue(self, index: int, value: any):
        self.data[index].value = value
