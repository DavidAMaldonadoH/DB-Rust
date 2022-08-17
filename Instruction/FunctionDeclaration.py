from Util.Instruction import Instruction
from Util.Scope import Scope


class FunctionDeclaration(Instruction):
    def __init__(
        self,
        line: int,
        column: int,
        id: str,
        parameters: list,
        code: Instruction,
        type: any,
    ):
        super().__init__(line, column)
        self.id = id
        self.parameters = parameters
        self.code = code
        self.type = type

    def execute(self, scope: Scope) -> any:
        scope.saveFunction(
            self.id,
            {"parameters": self.parameters, "code": self.code, "type": self.type},
            self.line,
            self.column,
        )
