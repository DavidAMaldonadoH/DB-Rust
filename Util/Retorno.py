from enum import Enum


class Type(Enum):
    Int = 0, "integer"
    Float = 1, "float"
    Bool = 2, "bool"
    Char = 3, "char"
    Str = 4, "&str"
    String = 5, "String"
    Usize = 6, "usize"
    Array = 7, "Array"
    Vector = 8, "Vector"
    Struct = 9, "Struct"
    Null = 10, "Null"

    def __new__(cls, value, name):
        member = object.__new__(cls)
        member._value_ = value
        member.fullname = name
        return member

    def __int__(self):
        return self.value


class ArithmeticType(Enum):
    Addition = 1
    Substraction = 2
    Multiplication = 3
    Division = 4
    Power = 5
    Module = 6
    Negation = 7


class LogicType(Enum):
    Or = 1
    And = 2
    Not = 3


class RelationalType(Enum):
    Equals = 1
    NotEquals = 2
    Less = 3
    LessOrEqual = 4
    Greater = 5
    GreaterOrEqual = 6


class Retorno:
    def __init__(self, value: any, type: Type):
        self.value = value
        self.type = type

    def getValue(self) -> any:
        return self.value

    def getType(self) -> Type:
        return self.type

    def showInfo(self):
        print(f"Value: {self.value}\nType: {self.type}")


def getNestedType(nested_type: dict) -> str:
    if isinstance(nested_type["type"], dict):
        if "size" in nested_type:
            return f"{nested_type['size']}*" + getNestedType(
                nested_type["type"]
            )
        else:
            return f"vec<" + getNestedType(nested_type["type"]) + ">"
    else:
        if not isinstance(nested_type["type"], Type):
            if "size" in nested_type:
                return f"{nested_type['size']}*" + nested_type["type"]
            else:
                return "vec<" + nested_type["type"] + ">"
        else:
            if "size" in nested_type:
                return f"{nested_type['size']}*{nested_type['type'].fullname}"
            else:
                return f"vec<{nested_type['type'].fullname}>"
