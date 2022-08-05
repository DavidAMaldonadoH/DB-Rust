from Util.Expression import Expression
from Util.Retorno import Retorno, Type
from Util.Scope import Scope
from Util.Error import ERRORS_, Error


class StructAccess(Expression):
    def __init__(self, line: int, column: int, expr: Expression, member: str):
        super().__init__(line, column)
        self.expr = expr
        self.member = member

    def execute(self, scope: Scope) -> Retorno:
        var = self.expr.execute(scope)
        if var.type == Type.Struct:
            if self.member in var.getValue().items:
                value = var.value[self.member]
                return Retorno(value.value, value.type)
            else:
                err = Error(
                    self.line,
                    self.column,
                    f"Miembro {self.member} no encontrado en el struct {var.getValue().name}",
                    scope.name,
                )
                ERRORS_.append(err)
                raise err
        else:
            err = Error(
                self.line,
                self.column,
                f"",
                scope.name,
            )
            ERRORS_.append(err)
            raise err
