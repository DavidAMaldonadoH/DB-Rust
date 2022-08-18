from Util.Retorno import Type
from Util.Symbol import Symbol


class Vector:
    def __init__(self, type: Type, size: int, capacity: bool = False):
        self.type = type
        self.size = size
        self.capacity = capacity
        self.data: list[Symbol] = []

    def getType(self) -> Type:
        return self.type

    def getNestedType(self) -> str:
        if self.type == Type.Vector:
            return "vec<" + self.data[0].getValue().getNestedType() + ">"
        else:
            if self.type == Type.Struct:
                return "vec<" + self.data[0].getValue().name + ">"
            elif self.type == Type.Array:
                return "vec<" + self.data[0].getValue().getNestedType() + ">"
            return "vec<" + self.type.fullname + ">"

    def getValue(self, index: int) -> Symbol:
        return self.data[index]

    def getLen(self) -> int:
        return len(self.data)

    def getCapacity(self) -> int:
        return self.size

    def appendValue(self, value: Symbol):
        self.data.append(value)
        if self.size == len(self.data):
            self.size = self.size * 2

    def insertValue(self, index: int, value: any):
        self.data.insert(index, value)
        if self.size == len(self.data):
            self.size = self.size * 2

    def setValue(self, index: int, value: any):
        self.data[index].value = value
