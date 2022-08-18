from typing import Optional
from Util.Expression import Expression
from Util.Instruction import Instruction
from Util.Retorno import Type, getNestedType
from Util.Scope import Scope
from Util.Symbol import Symbol


class Insert(Instruction):
    def __init__(
        self,
        line: int,
        column: int,
        id: Optional[str],
        ids: Optional[list],
        value: Expression,
        index: Expression,
    ):
        super().__init__(line, column)
        self.id = id
        self.ids = ids
        self.value = value
        self.index = index

    def execute(self, scope: Scope) -> any:
        value_ = self.value.execute(scope)
        if self.id is not None:
            var = scope.getVar(self.id)
            if var.isMutable():
                if var.getType() == Type.Vector:
                    index_ = self.index.execute(scope)
                    if index_.type == Type.Int or index_.type == Type.Usize:
                        if value_.type == Type.Vector or value_.type == Type.Array:
                            value_type = "vec<" + value_.value.getNestedType() + ">"
                        else:
                            value_type = "vec<" + value_.type.fullname + ">"
                        if isinstance(var.getValue().type, dict):
                            vector_type = getNestedType(var.getValue().type)
                        else:
                            vector_type = var.getValue().getNestedType()
                        if vector_type == value_type:
                            sym = Symbol("", True, value_.value, value_.type)
                            var.getValue().insertValue(index_.value, sym)
                else:
                    pass  # error solo se puede hacer insert a vectores
            else:
                pass  # error no se puede hacer insert a una variable no mutable
        else:
            pass  # insert anidado
