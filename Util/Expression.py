from Util.Retorno import Retorno, Type
from Util.Scope import Scope


class Expression:
    def __init__(self, line: int, column: int):
        self.line = line
        self.column = column

    def execute(self, scope: Scope) -> Retorno:
        print(scope.name)
        return Retorno(1, Type.Null)
