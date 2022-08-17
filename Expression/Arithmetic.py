from Util.Error import ERRORS_, Error
from Util.Expression import Expression
from Util.Retorno import ArithmeticType, Retorno, Type
from Util.Scope import Scope


class Arithmetic(Expression):
    def __init__(
        self,
        line: int,
        column: int,
        left: Expression,
        right: Expression,
        type: ArithmeticType,
        r_type=None,
    ):
        super().__init__(line, column)
        self.left = left
        self.right = right
        self.type = type
        self.r_type = r_type

    def execute(self, scope: Scope) -> Retorno:
        left_op = self.left.execute(scope)
        right_op = self.right.execute(scope)
        if self.type == ArithmeticType.Addition:
            return self.addition(left_op, right_op, self.line, self.column, scope.name)
        elif self.type == ArithmeticType.Substraction:
            return self.subs(left_op, right_op, self.line, self.column, scope.name)
        elif self.type == ArithmeticType.Multiplication:
            return self.mult(left_op, right_op, self.line, self.column, scope.name)
        elif self.type == ArithmeticType.Division:
            return self.division(left_op, right_op, self.line, self.column, scope.name)
        elif self.type == ArithmeticType.Power:
            return self.power(left_op, right_op, self.line, self.column, scope.name)
        elif self.type == ArithmeticType.Module:
            return self.mod(left_op, right_op, self.line, self.column, scope.name)
        elif self.type == ArithmeticType.Negation:
            return self.unegation(right_op, self.line, self.column, scope.name)
        else:
            err = Error(
                self.line,
                self.column,
                f"Operación aritmética incorrecta!",
                scope.name,
            )
            ERRORS_.append(err)

    def addition(
        self, left_op: Retorno, right_op: Retorno, line: int, column: int, name: str
    ) -> Retorno:
        if left_op.getType() == Type.Int and right_op.getType() == Type.Int:
            return Retorno(left_op.getValue() + right_op.getValue(), Type.Int)
        elif left_op.getType() == Type.Float and right_op.getType() == Type.Float:
            return Retorno(left_op.getValue() + right_op.getValue(), Type.Float)
        elif left_op.getType() == Type.String and right_op.getType() == Type.Str:
            return Retorno(f"{left_op.getValue()}{right_op.getValue()}", Type.String)
        elif left_op.getType() == Type.Usize and right_op.getType() == Type.Usize:
            return Retorno(left_op.getValue() + right_op.getValue(), Type.Usize)
        else:
            err = Error(
                line,
                column,
                f"No se puede sumar `{{{right_op.type.fullname}}}` a un `{left_op.type.fullname}`",
                name,
            )
            ERRORS_.append(err)

    def subs(
        self, left_op: Retorno, right_op: Retorno, line: int, column: int, name: str
    ) -> Retorno:
        if left_op.getType() == Type.Int and right_op.getType() == Type.Int:
            return Retorno(left_op.getValue() - right_op.getValue(), Type.Int)
        elif left_op.getType() == Type.Float and right_op.getType() == Type.Float:
            return Retorno(left_op.getValue() - right_op.getValue(), Type.Float)
        elif left_op.getType() == Type.Usize and right_op.getType() == Type.Usize:
            return Retorno(left_op.getValue() - right_op.getValue(), Type.Usize)
        else:
            err = Error(
                line,
                column,
                f"No se puede restar `{{{right_op.type.fullname}}}` a un `{left_op.type.fullname}`",
                name,
            )
            ERRORS_.append(err)

    def mult(
        self, left_op: Retorno, right_op: Retorno, line: int, column: int, name: str
    ) -> Retorno:
        if left_op.getType() == Type.Int and right_op.getType() == Type.Int:
            return Retorno(left_op.getValue() * right_op.getValue(), Type.Int)
        elif left_op.getType() == Type.Float and right_op.getType() == Type.Float:
            return Retorno(left_op.getValue() * right_op.getValue(), Type.Float)
        elif left_op.getType() == Type.Usize and right_op.getType() == Type.Usize:
            return Retorno(left_op.getValue() * right_op.getValue(), Type.Usize)
        else:
            err = Error(
                line,
                column,
                f"No se puede multiplicar `{{{right_op.type.fullname}}}` por un `{left_op.type.fullname}`",
                name,
            )
            ERRORS_.append(err)

    def division(
        self, left_op: Retorno, right_op: Retorno, line: int, column: int, name: str
    ) -> Retorno:
        if right_op.value == 0:
            err = Error(
                line,
                column,
                f"No se puede dividir entre 0",
                name,
            )
            ERRORS_.append(err)
            return Retorno(0, Type.Int)
        if left_op.getType() == Type.Int and right_op.getType() == Type.Int:
            return Retorno(int(left_op.getValue() / right_op.getValue()), Type.Int)
        elif left_op.getType() == Type.Float and right_op.getType() == Type.Float:
            return Retorno(left_op.getValue() / right_op.getValue(), Type.Float)
        elif left_op.getType() == Type.Usize and right_op.getType() == Type.Usize:
            return Retorno(int(left_op.getValue() / right_op.getValue()), Type.Usize)
        else:
            err = Error(
                line,
                column,
                f"No se puede dividir `{{{right_op.type.fullname}}}` por un `{left_op.type.fullname}`",
                name,
            )
            ERRORS_.append(err)

    def power(
        self, left_op: Retorno, right_op: Retorno, line: int, column: int, name: str
    ) -> Retorno:
        if self.r_type == Type.Int and (
            left_op.getType() == Type.Float or right_op.getType() == Type.Float
        ):
            err = Error(
                line,
                column,
                f"Se esperaba `i64`, se encontro float",
                name,
            )
            ERRORS_.append(err)

        if self.r_type == Type.Float and (
            left_op.getType() == Type.Int or right_op.getType() == Type.Int
        ):
            err = Error(
                line,
                column,
                f"Se esperaba `f64`, se encontro integer",
                name,
            )
            ERRORS_.append(err)

        if left_op.getType() == Type.Int and right_op.getType() == Type.Int:
            return Retorno(left_op.value ** right_op.value, Type.Int)
        elif left_op.getType() == Type.Float and right_op.getType() == Type.Float:
            return Retorno(left_op.value ** right_op.value, Type.Float)
        else:
            err = Error(
                line,
                column,
                f"No se puede potenciar {left_op.type.fullname} por un {right_op.type.fullname}",
                name,
            )
            ERRORS_.append(err)

    def mod(
        self, left_op: Retorno, right_op: Retorno, line: int, column: int, name: str
    ) -> Retorno:
        if left_op.getType() == Type.Int and right_op.getType() == Type.Int:
            return Retorno(left_op.getValue() % right_op.getValue(), Type.Int)
        elif left_op.getType() == Type.Float and right_op.getType() == Type.Float:
            return Retorno(left_op.getValue() % right_op.getValue(), Type.Float)
        elif left_op.getType() == Type.Usize and right_op.getType() == Type.Usize:
            return Retorno(left_op.getValue() % right_op.getValue(), Type.Usize)
        else:
            err = Error(
                line,
                column,
                f"No se puede mod `{{{right_op.type.fullname}}}` por un `{left_op.type.fullname}`",
                name,
            )
            ERRORS_.append(err)

    def unegation(
        self, right_op: Retorno, line: int, column: int, name: str
    ) -> Retorno:
        if right_op.getType() == Type.Int:
            return Retorno(-1 * right_op.getValue(), Type.Int)
        elif right_op.getType() == Type.Float:
            return Retorno(-1 * right_op.getValue(), Type.Float)
        elif right_op.getType() == Type.Usize:
            return Retorno(-1 * right_op.getValue(), Type.Usize)
        else:
            err = Error(
                line,
                column,
                f"No se aplicar negacion unaria a un `{right_op.type.fullname}`",
                name,
            )
            ERRORS_.append(err)
