from Util.Instruction import Instruction
from Util.Scope import Scope


class Statement(Instruction):
    def __init__(self, line: int, column: int, code: list[Instruction]):
        super().__init__(line, column)
        self.code = code
        self.name = "Local"

    def setName(self, name: str):
        self.name = name

    def execute(self, scope: Scope) -> any:
        new_scope = Scope(scope, self.name)
        for instruction in self.code:
            retorno = instruction.execute(new_scope)
            if retorno is not None:
                return retorno
