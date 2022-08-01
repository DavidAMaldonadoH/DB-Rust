from Util.Instruction import Instruction
from Util.Scope import Scope


class Continue(Instruction):
    def __init__(self, line: int, column: int):
        super().__init__(line, column)

    def execute(self, scope: Scope) -> any:
        return {
            "type": "continue",
            "line": self.line,
            "column": self.column,
        }
