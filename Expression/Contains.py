from Util.Expression import Expression
from Util.Retorno import Retorno, Type
from Util.Scope import Scope
from Util.Error import ERRORS_, Error


class Contains(Expression):
    def __init__(self, line: int, column: int, expr: Expression, value: Expression):
        super().__init__(line, column)
        self.expr = expr
        self.value = value

    def execute(self, scope: Scope) -> Retorno:
        var = self.expr.execute(scope)
        if var.getType() == Type.Vector:
            value = self.value.execute(scope)
            for val in var.value.data:
                if val.getValue() == value.getValue():
                    return Retorno(True, Type.Bool)
            return Retorno(False, Type.Bool)
        else:
            err = Error(
                self.line,
                self.column,
                "Se esperaba un arreglo o vector, pero se obtuvo un "
                + var.getType().fullname,
                scope.name,
            )
            ERRORS_.append(err)
