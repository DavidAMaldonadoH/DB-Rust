from Util.Instruction import Instruction
from Util.Expression import Expression
from Util.Retorno import Type
from Util.Scope import Scope
from Util.Error import ERRORS_, Error


class NestedAssignation(Instruction):
    def __init__(self, line: int, column: int, vars: list, value: Expression):
        super().__init__(line, column)
        self.vars = vars
        self.value = value

    def execute(self, scope: Scope) -> any:
        actual_var = scope.getVar(self.vars[0])
        if actual_var is not None:
            value_ = self.value.execute(scope)
            if actual_var.isMutable():
                for i in range(1, len(self.vars) - 1):
                    if isinstance(self.vars[i], Expression):
                        index = self.vars[i].execute(scope)
                        if index.type == Type.Int or index.type == Type.Usize:
                            if (
                                actual_var.type == Type.Array
                                or actual_var.type == Type.Vector
                            ):
                                actual_var = actual_var.value.getValue(index.value)
                        else:
                            err = Error(
                                self.line,
                                self.column,
                                "El índice debe ser un integer o usize",
                                scope.name,
                            )
                            ERRORS_.append(err)
                    else:
                        actual_var.value = actual_var.value[self.vars[i]]
                if isinstance(self.vars[-1], Expression):
                    index = self.vars[len(self.vars) - 1].execute(scope)
                    if index.type == Type.Int or index.type == Type.Usize:
                        if (
                            actual_var.type == Type.Array
                            or actual_var.type == Type.Vector
                        ):
                            if isinstance(value_, dict):
                                value_ = value_["value"]
                            actual_var.value.setValue(index.value, value_.value)
                        else:
                            err = Error(
                                self.line,
                                self.column,
                                "El índice debe ser un integer o usize",
                                scope.name,
                            )
                            ERRORS_.append(err)
                else:
                    if isinstance(value_, dict):
                        value_ = value_["value"]
                    actual_var.value[self.vars[-1]].value = value_.value
            else:
                err = Error(
                    self.line,
                    self.column,
                    f"La variable {self.vars[0]} no es mutable",
                    scope.name,
                )
                ERRORS_.append(err)
        else:
            err = Error(
                self.line,
                self.column,
                f"La variable {self.vars[0]} no se ha declarado anteriormente!",
                scope.name,
            )
            ERRORS_.append(err)
