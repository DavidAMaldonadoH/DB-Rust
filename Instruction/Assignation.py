from Expression.Literal import Literal
from Util.Error import ERRORS_, Error
from Util.Expression import Expression
from Util.Instruction import Instruction
from Util.Retorno import Type, getNestedType
from Util.Scope import Scope


class Assignation(Instruction):
    def __init__(self, line: int, column: int, id: str, value: Expression):
        super().__init__(line, column)
        self.id = id
        self.value = value

    def execute(self, scope: Scope) -> any:
        var = scope.getVar(self.id)
        if var is None:
            err = Error(
                self.line,
                self.column,
                f"La variable {self.id} no se ha declarado anteriormente.",
                scope.name,
            )
            ERRORS_.append(err)
            return
        if not var.isMutable():
            err = Error(
                self.line,
                self.column,
                f"{self.id} no es una variable mutable, no se puede modificar.",
                scope.name,
            )
            ERRORS_.append(err)
            return
        value_ = self.value.execute(scope)
        if isinstance(value_, dict):
            value_ = value_["value"]
        if isinstance(self.value, Literal) and value_.getType() == Type.Int:
            value_.type = Type.Usize if var.type == Type.Usize else Type.Int
        var_type = var.getType()
        value_type = value_.getType()
        if var_type == Type.Vector:
            if value_.value.type == Type.Null:
                value_.value.type = var.value.type
            var_type = getNestedType(var.value.getType())
            if isinstance(value_.value.type, dict):
                value_type = getNestedType(value_.value.getType())
            else:
                value_type = value_.value.getNestedType()
        if var_type != value_type:
            err = Error(
                self.line,
                self.column,
                f"Los tipos no coinciden: se esperaba {var.type.fullname} y se recibio {value_.getType().fullname}",
                scope.name,
            )
            ERRORS_.append(err)
            return
        var.value = value_.getValue()
