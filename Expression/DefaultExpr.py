from typing import Optional
from Util.Expression import Expression
from Util.Instruction import Instruction
from Util.Retorno import Retorno
from Util.Scope import Scope


class DefaultExpr(Expression):
    def __init__(
        self,
        line: int,
        column: int,
        code: Optional[list[Instruction]],
        result: Expression,
    ):
        super().__init__(line, column)
        self.code = code
        self.result = result

    def execute(self, scope: Scope) -> Retorno:
        new_scope = Scope(scope, "Default")
        if self.code is not None:
            for instruction in self.code:
                instruction.execute(new_scope)
        return self.result.execute(new_scope)
