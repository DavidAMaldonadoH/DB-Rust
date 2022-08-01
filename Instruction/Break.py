from typing import Optional
from Util.Expression import Expression
from Util.Instruction import Instruction
from Util.Scope import Scope


class Break(Instruction):
    def __init__(self, line: int, column: int, expr: Optional[Expression]):
        super().__init__(line, column)
        self.expr = expr

    def execute(self, scope: Scope) -> any:
        value = None
        if self.expr != None:
            value = self.expr.execute(scope)
        return {
            "type": "break",
            "value": value,
            "line": self.line,
            "column": self.column,
        }
