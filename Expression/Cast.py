from Util.Error import ERRORS_, Error
from Util.Expression import Expression
from Util.Retorno import Retorno, Type
from Util.Scope import Scope


class Cast(Expression):
    def __init__(self, line: int, column: int, expr: Expression, type: Type):
        super().__init__(line, column)
        self.expr = expr
        self.type = type

    def execute(self, scope: Scope) -> Retorno:
        expr = self.expr.execute(scope)
        if self.type == Type.Int:
            if expr.getType() == Type.Str or expr.getType() == Type.String:
                err = Error(
                    self.line,
                    self.column,
                    f"Castear `{expr.type.fullname}` a `{self.type.fullname}` es  inválido",
                    scope.name,
                )
                ERRORS_.append(err)
                raise Exception(err)
            elif expr.getType() == Type.Char:
                return Retorno(ord(expr.getValue()), Type.Int)
            else:
                return Retorno(int(expr.getValue()), Type.Int)
        elif self.type == Type.Float:
            if (
                expr.getType() == Type.Str
                or expr.getType() == Type.String
                or expr.getType() == Type.Char
                or expr.getType() == Type.Bool
            ):
                err = Error(
                    self.line,
                    self.column,
                    f"Castear `{expr.type.fullname}` a `{self.type.fullname}` es  inválido",
                    scope.name,
                )
                ERRORS_.append(err)
                raise Exception(err)
            else:
                return Retorno(float(expr.getValue()), Type.Float)
        elif self.type == Type.Bool:
            if expr.getType() == Type.Bool:
                return expr
            else:
                err = Error(
                    self.line,
                    self.column,
                    "No se puede castear a `bool`",
                    scope.name,
                )
                ERRORS_.append(err)
                raise Exception(err)
        elif self.type == Type.Char:
            if expr.getType() == Type.Int or expr.getType() == Type.Usize:
                return Retorno(chr(expr.getValue()), Type.Char)
            else:
                err = Error(
                    self.line,
                    self.column,
                    "No se puede castear a `bool`",
                    scope.name,
                )
                ERRORS_.append(err)
                raise Exception(err)
        elif self.type == Type.Str:
            err = Error(
                self.line,
                self.column,
                f"Casteo no-primitivo: `{expr.getType().fullname}` como `&str`",
                scope.name,
            )
            ERRORS_.append(err)
            raise Exception(err)
        elif self.type == Type.String:
            err = Error(
                self.line,
                self.column,
                f"Casteo no-primitivo: `{expr.getType().fullname}` como `String`",
                scope.name,
            )
            ERRORS_.append(err)
            raise Exception(err)
        elif self.type == Type.Usize:
            if expr.getType() == Type.Str or expr.getType() == Type.String:
                err = Error(
                    self.line,
                    self.column,
                    f"Castear `{expr.type.fullname}` a `{self.type.fullname}` es  inválido",
                    scope.name,
                )
                ERRORS_.append(err)
                raise Exception(err)
            elif expr.getType() == Type.Char:
                return Retorno(ord(expr.getValue()), Type.Usize)
            else:
                return Retorno(int(expr.getValue()), Type.Usize)
        else:
            err = Error(
                self.line,
                self.column,
                f"Casteo no-permitido: `{expr.getType().fullname}` como `{self.type.fullname}`",
                scope.name,
            )
            ERRORS_.append(err)
            raise Exception(err)
