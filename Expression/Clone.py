from Util.Expression import Expression
from Util.Retorno import Retorno
from Util.Scope import Scope


class Clone(Expression):
    def __init__(self, line: int, column: int, expr: Expression):
        super().__init__(line, column)
        self.expr = expr

    def execute(self, scope: Scope) -> Retorno:
        expr = self.expr.execute(scope)
        return Retorno(expr.getValue(), expr.getType())
