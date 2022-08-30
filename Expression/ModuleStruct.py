from Expression.CreateStruct import CreateStruct
from Util.Error import ERRORS_, Error
from Util.Expression import Expression
from Util.Retorno import Retorno
from Util.Scope import Scope


class ModuleStruct(Expression):
    def __init__(self, line: int, column: int, ids: str, items: dict):
        super().__init__(line, column)
        self.ids = ids
        self.items = items

    def execute(self, scope: Scope) -> Retorno:
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
            if self.ids[-1] in current_scope.structs:
                if current_scope.structs[self.ids[-1]].public:
                    return CreateStruct(
                        self.line, self.column, self.ids[-1], self.items
                    ).execute(current_scope)
                else:
                    err = Error(
                        self.line,
                        self.column,
                        f"El struct {self.ids[-1]} no es publico.",
                        current_scope.name,
                    )
                    ERRORS_.append(err)
            else:
                err = Error(
                    self.line,
                    self.column,
                    f"El struct {self.ids[-1]} no existe.",
                    current_scope.name,
                )
                ERRORS_.append(err)
        else:
            err = Error(
                self.line,
                self.column,
                f"El módulo {self.ids[0]} no existe.",
                current_scope.name,
            )
            ERRORS_.append(err)
