from Expression.Literal import Literal
from Util.Error import ERRORS_, Error
from Util.Expression import Expression
from Util.Instruction import Instruction
from Util.Retorno import Type
from Util.Scope import Scope


class Assignation(Instruction):
    def __init__(self, line: int, column: int, id: str, value: Expression):
        super().__init__(line, column)
        self.id = id
        self.value = value

    def execute(self, scope: Scope) -> any:
        var = scope.getVar(self.id)
        if var != None:
            value_ = self.value.execute(scope)
            if var.isMutable():
                if isinstance(value_, dict):
                    value_ = value_["value"]
                if isinstance(self.value, Literal) and value_.getType() == Type.Int:
                    value_.type = Type.Usize if var.type == Type.Usize else Type.Int
                if var.getType() == value_.getType():
                    var.value = value_.getValue()
                else:
                    err = Error(
                        self.line,
                        self.column,
                        f"Los tipos no coinciden: se esperaba {var.type.fullname} y se recibio {value_.getType().fullname}",
                        scope.name,
                    )
                    ERRORS_.append(err)
            else:
                err = Error(
                    self.line,
                    self.column,
                    f"{self.id} no es una variable mutable, no se puede modificar.",
                    scope.name,
                )
                ERRORS_.append(err)
        else:
            err = Error(
                self.line,
                self.column,
                f"La variable {self.id} no se ha declarado anteriormente.",
                scope.name,
            )
            ERRORS_.append(err)
