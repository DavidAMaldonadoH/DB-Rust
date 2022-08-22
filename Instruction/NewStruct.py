from Util.Instruction import Instruction
from Util.Error import Error, ERRORS_
from Util.Scope import Scope
from Util.Struct import Struct
from Util.Symbol import Symbol


class NewStruct(Instruction):
    def __init__(
        self, line: int, column: int, name: str, items: dict, public: bool = False
    ):
        super().__init__(line, column)
        self.name = name
        self.items = items
        self.public = public

    def execute(self, scope: Scope) -> any:
        struct = Struct(self.name, self.public)
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
        scope.saveStruct(self.name, struct, self.line, self.column)
