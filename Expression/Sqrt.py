import math
from Util.Error import ERRORS_, Error
from Util.Expression import Expression
from Util.Retorno import Retorno, Type
from Util.Scope import Scope


class Sqrt(Expression):
    def __init__(self, line: int, column: int, expr: Expression):
        super().__init__(line, column)
        self.expr = expr

    def execute(self, scope: Scope) -> Retorno:
        expr = self.expr.execute(scope)
        if expr.getType() == Type.Float:
            return Retorno(math.sqrt(expr.getValue()), Type.Float)
        else:
            err = Error(
                self.line,
                self.column,
                f"Los tipos no coinciden: se expera `f64`, se encontro {expr.getType().fullname}",
                scope.name,
            )
            ERRORS_.append(err)
            raise Exception(err)
