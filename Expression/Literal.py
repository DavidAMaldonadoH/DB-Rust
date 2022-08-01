import re
from Util.Expression import Expression
from Util.Retorno import Type, Retorno
from Util.Scope import Scope


class Literal(Expression):
    def __init__(self, line: int, column: int, value: any):
        super().__init__(line, column)
        self.value = value

    def execute(self, scope: Scope) -> Retorno:
        if isinstance(self.value, bool):
            return Retorno(self.value, Type.Bool)
        elif isinstance(self.value, int):
            return Retorno(self.value, Type.Int)
        elif isinstance(self.value, float):
            return Retorno(self.value, Type.Float)
        elif isinstance(self.value, str):
            if re.match(r"\'((\\)?(.{1}?))\'", self.value):
                return Retorno(self.value[1:-1], Type.Char)
            else:
                return Retorno(self.value, Type.Str)
        else:
            return Retorno(self.value, Type.Null)
