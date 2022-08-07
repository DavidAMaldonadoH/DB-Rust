from Util.Expression import Expression
from Util.Retorno import Retorno, Type
from Util.Scope import Scope
from Util.Error import ERRORS_, Error


class Remove(Expression):
    def __init__(self, line: int, column: int, expr: Expression, index: Expression):
        super().__init__(line, column)
        self.expr = expr
        self.index = index

    def execute(self, scope: Scope) -> Retorno:
        var = self.expr.execute(scope)
        index = self.index.execute(scope)
        if var.getType() == Type.Vector:
            if scope.getVar(self.expr.id).isMutable():
                value = var.value.data[index.getValue()]
                var.value.size -= 1
                var.value.data.pop(index.getValue())
                return Retorno(value.getValue(), value.getType())
            else:
                err = Error(
                    self.line,
                    self.column,
                    "No se puede eliminar en un arreglo que no es mutable",
                    scope.name,
                )
                ERRORS_.append(err)
                raise Exception(err)
        else:
            err = Error(
                self.line,
                self.column,
                "Se esperaba un arreglo o vector, pero se obtuvo un "
                + var.getType().fullname,
                scope.name,
            )
            ERRORS_.append(err)
            raise Exception(err)
