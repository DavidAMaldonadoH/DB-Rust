from Util.Instruction import Instruction
from Util.Error import Error, ERRORS_
from Util.Scope import Scope
from Util.Struct import Struct
from Util.Symbol import Symbol


class NewStruct(Instruction):
    def __init__(self, line: int, column: int, name: str, items: dict):
        super().__init__(line, column)
        self.name = name
        self.items = items

    def execute(self, scope: Scope) -> any:
        struct = Struct(self.name)
        for key, value in self.items.items():
            if key not in struct.items:
                sym = Symbol(key, True, None, value)
                struct.items[key] = sym
            else:
                err = Error(
                    self.line,
                    self.column,
                    f"El {self.name} struct ya tiene el campo {key}",
                    scope.name,
                )
                ERRORS_.append(err)
                raise err
        scope.saveStruct(self.name, struct, self.line, self.column)
