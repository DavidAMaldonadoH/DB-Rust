from Instruction.FunctionDeclaration import FunctionDeclaration
from Instruction.NewStruct import NewStruct
from Util.Instruction import Instruction
from Util.Scope import Scope


class ModDeclaration(Instruction):
    def __init__(
        self, line: int, column: int, name: str, public: bool, code: Instruction
    ):
        super().__init__(line, column)
        self.name = name
        self.public = public
        self.code = code

    def execute(self, scope: Scope) -> any:
        self.code.name = self.name
        new_scope = Scope(scope, self.name)
        scope.saveModule(
            self.name,
            {
                "name": self.name,
                "scope": new_scope,
                "father": scope.name,
                "public": self.public,
            },
            self.line,
            self.column,
        )
        for node in self.code.code:
            if isinstance(node, FunctionDeclaration):
                node.execute(new_scope)
            elif isinstance(node, NewStruct):
                node.execute(new_scope)
            elif isinstance(node, ModDeclaration):
                node.execute(new_scope)
