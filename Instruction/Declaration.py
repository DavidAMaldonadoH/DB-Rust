from Util.Error import ERRORS_, Error
from Util.Expression import Expression
from typing import Optional
from Util.Instruction import Instruction
from Util.Retorno import Type
from Util.Scope import Scope


class Declaration(Instruction):
    def __init__(
        self,
        line: int,
        column: int,
        id: str,
        mut: bool,
        value: Optional[Expression],
        type: Optional[Type],
    ):
        super().__init__(line, column)
        self.line = line
        self.column = column
        self.id = id
        self.mut = mut
        self.value = value
        self.type = type

    def getNestedType(self, nested_type: dict) -> str:
        if isinstance(nested_type["type"], dict):
            return f"{nested_type['size']}*" + self.getNestedType(nested_type["type"])
        else:
            return f"{nested_type['size']}*{nested_type['type'].fullname}"

    def execute(self, scope: Scope) -> any:
        exists = scope.variables.get(self.id)
        if exists == None:
            if self.value == None:
                scope.saveVar(
                    self.id, self.mut, self.value, self.type, self.line, self.column
                )
            else:
                value_ = self.value.execute(scope)
                if self.type != None:
                    if self.type == Type.Usize and value_.getType() == Type.Int:
                        value_.type = Type.Usize
                    if value_.getType() == Type.Array:
                        if (
                            self.getNestedType(self.type)
                            == value_.getValue().getNestedType()
                        ):
                            scope.saveVar(
                                self.id,
                                self.mut,
                                value_.getValue(),
                                Type.Array,
                                self.line,
                                self.column,
                            )
                        else:
                            err = Error(
                                self.line,
                                self.column,
                                "Array type mismatch",
                                scope.name,
                            )
                            ERRORS_.append(err)
                            raise Exception(err)
                    elif value_.getType() == self.type:
                        scope.saveVar(
                            self.id,
                            self.mut,
                            value_.getValue(),
                            self.type,
                            self.line,
                            self.column,
                        )
                    else:
                        err = Error(
                            self.line,
                            self.column,
                            f"Los tipos no coinciden: se esperaba `{self.type.fullname}`, se obtuvo `{value_.getType().fullname}`",
                            scope.name,
                        )
                        ERRORS_.append(err)
                        raise Exception(err)
                else:
                    scope.saveVar(
                        self.id,
                        self.mut,
                        value_.getValue(),
                        value_.getType(),
                        self.line,
                        self.column,
                    )
        else:
            err = Error(
                self.line,
                self.column,
                f"La variable `{self.id}` ya ha sido declarada anteriormente!",
                scope.name,
            )
            ERRORS_.append(err)
            raise Exception(err)
