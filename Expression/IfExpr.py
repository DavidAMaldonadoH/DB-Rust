from typing import Optional
from Util.Expression import Expression
from Util.Instruction import Instruction
from Util.Retorno import Type
from Util.Scope import Scope


class IfExpr(Expression):
    def __init__(
        self,
        line: int,
        column: int,
        expr: Expression,
        code: Optional[list[Instruction]],
        result: Expression,
        elsest: Optional[Expression],
    ):
        super().__init__(line, column)
        self.expr = expr
        self.code = code
        self.result = result
        self.elsest = elsest

    def execute(self, scope: Scope) -> any:
        cond = self.expr.execute(scope)
        if cond.getType() == Type.Bool:
            if cond.getValue() == True:
                new_scope = Scope(scope, "If")
                if self.code is not None:
                    for instruction in self.code:
                        instruction.execute(new_scope)
                return self.result.execute(new_scope)
            elif self.elsest is not None:
                return self.elsest.execute(scope)
