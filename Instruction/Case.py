from Instruction.Statement import Statement
from Util.Expression import Expression
from Util.Instruction import Instruction
from Util.Scope import Scope


class Case(Instruction):
    def __init__(
        self, line: int, column: int, exprs: list[Expression], code: Instruction
    ):
        super().__init__(line, column)
        self.exprs = exprs
        self.code = code

    def execute(self, scope: Scope) -> any:
        if isinstance(self.code, Statement):
            self.code.setName("Case")
        retorno = self.code.execute(scope)
        if retorno is not None:
            return retorno
