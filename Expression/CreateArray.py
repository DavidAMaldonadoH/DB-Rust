from typing import Optional
from Util.Array import Array
from Util.Error import ERRORS_, Error
from Util.Expression import Expression
from Util.Retorno import Retorno, Type
from Util.Scope import Scope
from Util.Symbol import Symbol


class CreateArray(Expression):
    def __init__(
        self,
        line: int,
        column: int,
        expressions: Optional[list[Expression]],
        expression: Optional[Expression],
        size: Optional[int],
    ):
        super().__init__(line, column)
        self.expressions = expressions
        self.expression = expression
        self.size = size

    def execute(self, scope: Scope) -> Retorno:
        if self.expressions != None:
            first_item = self.expressions[0].execute(scope)
            same_types = True
            for item in self.expressions:
                if first_item.type != item.execute(scope).type:
                    same_types = False
                    break
            if same_types:
                arr = Array(first_item.type, len(self.expressions))
                for expr in self.expressions:
                    value = expr.execute(scope)
                    sym = Symbol("", True, value.value, value.type)
                    arr.appendValue(sym)
                return Retorno(arr, Type.Array)
            else:
                err = Error(
                    self.line,
                    self.column,
                    "Los valores declarados en el array no son del mismo tipo",
                    scope.getName(),
                )
                ERRORS_.append(err)
        else:
            var = self.expression.execute(scope)
            arr = Array(var.type, self.size)
            for _ in range(self.size):
                sym = Symbol("", True, var.value, var.type)
                arr.appendValue(sym)
            return Retorno(arr, Type.Array)
