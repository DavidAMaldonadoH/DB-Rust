from Util.Expression import Expression
from Util.Retorno import Retorno, Type
from Util.Scope import Scope


class Reference(Expression):
    def __init__(self, line: int, column: int, expression: Expression):
        super().__init__(line, column)
        self.expression = expression

    def execute(self, scope: Scope) -> Retorno:
        expr = self.expression.execute(scope)
        if expr.getType() == Type.String:
            return Retorno(expr.getValue(), Type.Str)
        else:
            return Retorno(expr.getValue(), expr.getType())
