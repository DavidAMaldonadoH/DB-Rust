from Util.Error import ERRORS_, Error
from Util.Expression import Expression
from Util.Retorno import LogicType, Retorno, Type
from Util.Scope import Scope


class Logic(Expression):
    def __init__(
        self,
        line: int,
        column: int,
        left: Expression,
        right: Expression,
        type: LogicType,
    ):
        super().__init__(line, column)
        self.left = left
        self.right = right
        self.type = type

    def execute(self, scope: Scope) -> Retorno:
        left_operand = self.left.execute(scope)
        right_operand = self.right.execute(scope)
        if (left_operand.getType() == Type.Bool) and (
            right_operand.getType() == Type.Bool
        ):
            if self.type == LogicType.Or:
                result = left_operand.getValue() or right_operand.getValue()
                return Retorno(result, Type.Bool)
            elif self.type == LogicType.And:
                result = left_operand.getValue() and right_operand.getValue()
                return Retorno(result, Type.Bool)
            else:
                result = not right_operand.getValue()
                return Retorno(result, Type.Bool)
        else:
            err = Error(
                self.line,
                self.column,
                "Los valores a operar no son booleanos",
                scope.name,
            )
            ERRORS_.append(err)
