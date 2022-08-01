from Instruction.Statement import Statement
from Util.Instruction import Instruction
from Util.Scope import Scope


class Default(Instruction):
    def __init__(self, line: int, column: int, code: Instruction):
        super().__init__(line, column)
        self.code = code

    def execute(self, scope: Scope) -> any:
        if isinstance(self.code, Statement):
            self.code.setName("Default")
        retorno = self.code.execute(scope)
        if retorno is not None:
            return retorno
