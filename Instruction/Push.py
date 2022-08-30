from typing import Optional
from Util.Error import ERRORS_, Error
from Util.Expression import Expression
from Util.Instruction import Instruction
from Util.Retorno import Type, getNestedType
from Util.Scope import Scope
from Util.Symbol import Symbol


class Push(Instruction):
    def __init__(
        self,
        line: int,
        column: int,
        id: Optional[str],
        ids: Optional[list],
        value: Expression,
    ):
        super().__init__(line, column)
        self.id = id
        self.ids = ids
        self.value = value

    def execute(self, scope: Scope) -> any:
        value_ = self.value.execute(scope)
        if self.id is not None:
            var = scope.getVar(self.id)
            if var.getType() == Type.Vector:
                if var.isMutable():
                    if value_.type == Type.Vector or value_.type == Type.Array:
                        value_type = "vec<" + value_.value.getNestedType() + ">"
                    else:
                        if value_.type == Type.Struct:
                            value_type = "vec<" + value_.value.name + ">"
                        else:
                            value_type = "vec<" + value_.type.fullname + ">"
                    if isinstance(var.getValue().type, dict):
                        vector_type = getNestedType(var.getValue().type)
                    else:
                        vector_type = var.getValue().getNestedType()
                    if vector_type == value_type:
                        sym = Symbol("", True, value_.value, value_.type)
                        var.getValue().appendValue(sym)
                else:
                    err = Error(
                        self.line,
                        self.column,
                        "La variable '" + self.id + "' no es mutable",
                        scope.name,
                    )
            else:
                err = Error(
                    self.line,
                    self.column,
                    "La variable '" + self.id + "' no es un vector",
                    scope.name,
                )
                ERRORS_.append(err)
        else:
            pass  # push anidado
