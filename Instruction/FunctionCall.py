from Util.Instruction import Instruction
from Util.Scope import Scope

class FunctionCall(Instruction):
    def __init__(self, line: int, column: int, name: str, args: list):
        super().__init__(line, column)
        self.name = name
        self.args = args

    def execute(self, scope: Scope) -> any:
        fn = scope.getFunction(self.name)
        if fn is not None:
            if len(fn.parameters) == len(self.args):
                fn_scope = Scope(scope.getGlobal(), fn.id)
                fn.code.name = fn.id
                fn.code.execute(fn_scope)
        else:
            pass