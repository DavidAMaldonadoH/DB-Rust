from Util.Expression import Expression
from Util.Retorno import Retorno, Type
from Util.Scope import Scope


class ArrayAccess(Expression):
    def __init__(self, line: int, column: int, array: Expression, index: Expression):
        super().__init__(line, column)
        self.array = array
        self.index = index

    def execute(self, scope: Scope) -> Retorno:
        var = self.array.execute(scope)
        if var.getType() == Type.Array:
            index = self.index.execute(scope)
            if index.getType() == Type.Int or index.getType() == Type.Usize:
                val = var.value.getValue(index.getValue())
                return Retorno(val.value, val.type)
