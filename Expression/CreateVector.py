from typing import Optional
from Util.Error import ERRORS_, Error
from Util.Expression import Expression
from Util.Retorno import Retorno, Type
from Util.Scope import Scope
from Util.Vector import Vector
from Util.Symbol import Symbol


class CreateVector(Expression):
    def __init__(
        self,
        line: int,
        column: int,
        expressions: Optional[list[Expression]],
        expression: Optional[Expression],
        size: Optional[Expression],
        empty: Optional[bool],
    ):
        super().__init__(line, column)
        self.expressions = expressions
        self.expression = expression
        self.size = size
        self.empty = empty

    def execute(self, scope: Scope) -> Retorno:
        if self.expressions is not None:
            first_item = self.expressions[0].execute(scope)
            same_types = True
            for item in self.expressions:
                if first_item.type != item.execute(scope).type:
                    same_types = False
                    break
            if same_types:
                vec = Vector(first_item.type, len(self.expressions))
                for expr in self.expressions:
                    value = expr.execute(scope)
                    sym = Symbol("", True, value.value, value.type)
                    vec.appendValue(sym)
                return Retorno(vec, Type.Vector)
            else:
                err = Error(
                    self.line,
                    self.column,
                    "Los valores declarados en el vector no son del mismo tipo",
                    scope.getName(),
                )
                ERRORS_.append(err)
        elif self.expression is not None and self.size is not None:
            var = self.expression.execute(scope)
            size = self.size.execute(scope)
            vec = Vector(var.type, size.getValue())
            for _ in range(size.getValue()):
                sym = Symbol("", True, var.value, var.type)
                vec.appendValue(sym)
            return Retorno(vec, Type.Vector)
        elif self.size is not None:
            size = self.size.execute(scope)
            vec = Vector(Type.Null, size.getValue())
            return Retorno(vec, Type.Vector)
        else:
            vec = Vector(Type.Null, 0)
            return Retorno(vec, Type.Vector)
