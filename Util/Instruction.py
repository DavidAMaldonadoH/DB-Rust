from Util.Retorno import Retorno, Type
from Util.Scope import Scope


class Instruction:
    def __init__(self, line: int, column: int):
        self.line = line
        self.column = column

    def execute(self, scope: Scope) -> any:
        print(scope.name)
        return Retorno(1, Type.Null)
