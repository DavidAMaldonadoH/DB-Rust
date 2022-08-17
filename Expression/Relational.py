from Util.Error import ERRORS_, Error
from Util.Expression import Expression
from Util.Retorno import RelationalType, Retorno, Type
from Util.Scope import Scope


class Relational(Expression):
    def __init__(
        self,
        line: int,
        column: int,
        left: Expression,
        right: Expression,
        type: RelationalType,
    ):
        super().__init__(line, column)
        self.left = left
        self.right = right
        self.type = type

    def execute(self, scope: Scope) -> Retorno:
        left_op = self.left.execute(scope)
        right_op = self.right.execute(scope)
        if self.type == RelationalType.Equals:
            return self.equals(left_op, right_op, self.line, self.column, scope.name)
        elif self.type == RelationalType.NotEquals:
            return self.notEquals(left_op, right_op, self.line, self.column, scope.name)
        elif self.type == RelationalType.Greater:
            return self.greater(left_op, right_op, self.line, self.column, scope.name)
        elif self.type == RelationalType.GreaterOrEqual:
            return self.greaterOrE(
                left_op, right_op, self.line, self.column, scope.name
            )
        elif self.type == RelationalType.Less:
            return self.less(left_op, right_op, self.line, self.column, scope.name)
        elif self.type == RelationalType.LessOrEqual:
            return self.lessOrE(left_op, right_op, self.line, self.column, scope.name)
        else:
            err = Error(
                self.line,
                self.column,
                "Operación relacional incarrecta!",
                scope.name,
            )
            ERRORS_.append(err)

    def equals(
        self, left_op: Retorno, right_op: Retorno, line: int, column: int, name: str
    ) -> Retorno:
        if left_op.type == Type.Int and right_op.type == Type.Int:
            return Retorno(left_op.value == right_op.value, Type.Bool)
        elif left_op.type == Type.Float and right_op.type == Type.Float:
            return Retorno(left_op.value == right_op.value, Type.Bool)
        elif left_op.type == Type.Bool and right_op.value == Type.Bool:
            return Retorno(left_op.value == right_op.value, Type.Bool)
        elif left_op.type == Type.Char and right_op.type == Type.Char:
            return Retorno(ord(left_op.value) == ord(right_op.value), Type.Bool)
        elif (left_op.type == Type.Str or left_op.type == Type.String) and (
            right_op.type == Type.Str or right_op.type == Type.String
        ):
            return Retorno(left_op.value == right_op.value, Type.Bool)
        elif left_op.type == Type.Usize and right_op.type == Type.Usize:
            return Retorno(left_op.value == right_op.value, Type.Bool)
        else:
            err = Error(
                line,
                column,
                f"Los tipos no coinciden: {left_op.type.fullname} con {right_op.type.fullname}",
                name,
            )
            ERRORS_.append(err)

    def notEquals(
        self, left_op: Retorno, right_op: Retorno, line: int, column: int, name: str
    ) -> Retorno:
        if left_op.type == Type.Int and right_op.type == Type.Int:
            return Retorno(left_op.value != right_op.value, Type.Bool)
        elif left_op.type == Type.Float and right_op.type == Type.Float:
            return Retorno(left_op.value != right_op.value, Type.Bool)
        elif left_op.type == Type.Bool and right_op.value == Type.Bool:
            return Retorno(left_op.value != right_op.value, Type.Bool)
        elif left_op.type == Type.Char and right_op.type == Type.Char:
            return Retorno(ord(left_op.value) != ord(right_op.value), Type.Bool)
        elif (left_op.type == Type.Str or left_op.type == Type.String) and (
            right_op.type == Type.Str or right_op.type == Type.String
        ):
            return Retorno(left_op.value != right_op.value, Type.Bool)
        elif left_op.type == Type.Usize and right_op.type == Type.Usize:
            return Retorno(left_op.value != right_op.value, Type.Bool)
        else:
            err = Error(
                line,
                column,
                f"Los tipos no coinciden: {left_op.type.fullname} con {right_op.type.fullname}",
                name,
            )
            ERRORS_.append(err)

    def greater(
        self, left_op: Retorno, right_op: Retorno, line: int, column: int, name: str
    ) -> Retorno:
        if left_op.type == Type.Int and right_op.type == Type.Int:
            return Retorno(left_op.value > right_op.value, Type.Bool)
        elif left_op.type == Type.Float and right_op.type == Type.Float:
            return Retorno(left_op.value > right_op.value, Type.Bool)
        elif left_op.type == Type.Bool and right_op.value == Type.Bool:
            return Retorno(left_op.value > right_op.value, Type.Bool)
        elif left_op.type == Type.Char and right_op.type == Type.Char:
            return Retorno(ord(left_op.value) > ord(right_op.value), Type.Bool)
        elif (left_op.type == Type.Str or left_op.type == Type.String) and (
            right_op.type == Type.Str or right_op.type == Type.String
        ):
            return Retorno(left_op.value > right_op.value, Type.Bool)
        elif left_op.type == Type.Usize and right_op.type == Type.Usize:
            return Retorno(left_op.value > right_op.value, Type.Bool)
        else:
            err = Error(
                line,
                column,
                f"Los tipos no coinciden: {left_op.type.fullname} con {right_op.type.fullname}",
                name,
            )
            ERRORS_.append(err)

    def greaterOrE(
        self, left_op: Retorno, right_op: Retorno, line: int, column: int, name: str
    ) -> Retorno:
        if left_op.type == Type.Int and right_op.type == Type.Int:
            return Retorno(left_op.value >= right_op.value, Type.Bool)
        elif left_op.type == Type.Float and right_op.type == Type.Float:
            return Retorno(left_op.value >= right_op.value, Type.Bool)
        elif left_op.type == Type.Bool and right_op.value == Type.Bool:
            return Retorno(left_op.value >= right_op.value, Type.Bool)
        elif left_op.type == Type.Char and right_op.type == Type.Char:
            return Retorno(ord(left_op.value) >= ord(right_op.value), Type.Bool)
        elif (left_op.type == Type.Str or left_op.type == Type.String) and (
            right_op.type == Type.Str or right_op.type == Type.String
        ):
            return Retorno(left_op.value >= right_op.value, Type.Bool)
        elif left_op.type == Type.Usize and right_op.type == Type.Usize:
            return Retorno(left_op.value >= right_op.value, Type.Bool)
        else:
            err = Error(
                line,
                column,
                f"Los tipos no coinciden: {left_op.type.fullname} con {right_op.type.fullname}",
                name,
            )
            ERRORS_.append(err)

    def less(
        self, left_op: Retorno, right_op: Retorno, line: int, column: int, name: str
    ) -> Retorno:
        if left_op.type == Type.Int and right_op.type == Type.Int:
            return Retorno(left_op.value < right_op.value, Type.Bool)
        elif left_op.type == Type.Float and right_op.type == Type.Float:
            return Retorno(left_op.value < right_op.value, Type.Bool)
        elif left_op.type == Type.Bool and right_op.value == Type.Bool:
            return Retorno(left_op.value < right_op.value, Type.Bool)
        elif left_op.type == Type.Char and right_op.type == Type.Char:
            return Retorno(ord(left_op.value) < ord(right_op.value), Type.Bool)
        elif (left_op.type == Type.Str or left_op.type == Type.String) and (
            right_op.type == Type.Str or right_op.type == Type.String
        ):
            return Retorno(left_op.value < right_op.value, Type.Bool)
        elif left_op.type == Type.Usize and right_op.type == Type.Usize:
            return Retorno(left_op.value < right_op.value, Type.Bool)
        else:
            err = Error(
                line,
                column,
                f"Los tipos no coinciden: {left_op.type.fullname} con {right_op.type.fullname}",
                name,
            )
            ERRORS_.append(err)

    def lessOrE(
        self, left_op: Retorno, right_op: Retorno, line: int, column: int, name: str
    ) -> Retorno:
        if left_op.type == Type.Int and right_op.type == Type.Int:
            return Retorno(left_op.value <= right_op.value, Type.Bool)
        elif left_op.type == Type.Float and right_op.type == Type.Float:
            return Retorno(left_op.value <= right_op.value, Type.Bool)
        elif left_op.type == Type.Bool and right_op.value == Type.Bool:
            return Retorno(left_op.value <= right_op.value, Type.Bool)
        elif left_op.type == Type.Char and right_op.type == Type.Char:
            return Retorno(ord(left_op.value) <= ord(right_op.value), Type.Bool)
        elif (left_op.type == Type.Str or left_op.type == Type.String) and (
            right_op.type == Type.Str or right_op.type == Type.String
        ):
            return Retorno(left_op.value <= right_op.value, Type.Bool)
        elif left_op.type == Type.Usize and right_op.type == Type.Usize:
            return Retorno(left_op.value <= right_op.value, Type.Bool)
        else:
            err = Error(
                line,
                column,
                f"Los tipos no coinciden: {left_op.type.fullname} con {right_op.type.fullname}",
                name,
            )
            ERRORS_.append(err)
