from Util.Expression import Expression
from Util.Retorno import Retorno, Type
from Util.Scope import Scope
from Util.Error import ERRORS_, Error


class Capacity(Expression):
    def __init__(self, line: int, column: int, expr: Expression):
        super().__init__(line, column)
        self.expr = expr

    def execute(self, scope: Scope) -> Retorno:
        val = self.expr.execute(scope)
        if val.getType() == Type.Vector:
            return Retorno(val.getValue().size, Type.Int)
        else:
            err = Error(
                self.line,
                self.column,
                "Se esperaba un arreglo o vector, pero se obtuvo un "
                + val.getType().fullname,
                scope.name,
            )
            ERRORS_.append(err)
            raise Exception(err)
