from Util.Error import ERRORS_, Error
from Util.Instruction import Instruction
from Util.Scope import Scope


class Loop(Instruction):
    def __init__(self, line: int, column: int, code: Instruction):
        super().__init__(line, column)
        self.code = code

    def execute(self, scope: Scope) -> any:
        self.code.setName("Loop")
        while True:
            retorno = self.code.execute(scope)
            if retorno is not None:
                if retorno["type"] == "break":
                    if retorno["value"] is not None:
                        return retorno["value"]
                    else:
                        break
                else:
                    return retorno
