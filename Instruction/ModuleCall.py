from Instruction.FunctionCall import FunctionCall
from Util.Error import ERRORS_, Error
from Util.Expression import Expression
from Util.Instruction import Instruction
from Util.Scope import Scope


class ModuleCall(Instruction):
    def __init__(
        self, line: int, column: int, ids: list[str], params: list[Expression]
    ):
        super().__init__(line, column)
        self.ids = ids
        self.params = params

    def execute(self, scope: Scope) -> any:
        current_scope = scope.getGlobal()
        if self.ids[0] in current_scope.modules:
            current_scope = current_scope.modules[self.ids[0]].scope
            for i in range(1, len(self.ids) - 1):
                if self.ids[i] in current_scope.modules:
                    current_scope = current_scope.modules[self.ids[i]].scope
                else:
                    err = Error(
                        self.line,
                        self.column,
                        f"El módulo {self.ids[i]} no existe dentro del módulo {self.ids[i - 1]}.",
                        current_scope.name,
                    )
                    ERRORS_.append(err)
            current_scope.variables = scope.variables
            if self.ids[-1] in current_scope.functions:
                if current_scope.functions[self.ids[-1]].public:
                    return FunctionCall(
                        self.line, self.column, self.ids[-1], self.params
                    ).execute(current_scope)
                else:
                    err = Error(
                        self.line,
                        self.column,
                        f"La función {self.ids[-1]} no es pública.",
                        current_scope.name,
                    )
                    ERRORS_.append(err)
            else:
                err = Error(
                    self.line,
                    self.column,
                    f"La función {self.ids[-1]} no existe dentro del módulo {current_scope.name}.",
                    current_scope.name,
                )
                ERRORS_.append(err)
        else:
            err = Error(
                self.line,
                self.column,
                f"El módulo {self.ids[0]} no existe.",
                scope.name,
            )
            ERRORS_.append(err)
