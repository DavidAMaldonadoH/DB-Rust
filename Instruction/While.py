from Util.Error import ERRORS_, Error
from Util.Expression import Expression
from Util.Instruction import Instruction
from Util.Retorno import Type
from Util.Scope import Scope


class While(Instruction):
    def __init__(self, line: int, column: int, expr: Expression, code: Instruction):
        super().__init__(line, column)
        self.expr = expr
        self.code = code

    def execute(self, scope: Scope) -> any:
        self.code.setName("While")
        cond = self.expr.execute(scope)
        if cond.getType() == Type.Bool:
            while cond.getValue() == True:
                retorno = self.code.execute(scope)
                if retorno is not None:
                    if retorno["type"] == "break":
                        if retorno["value"] is not None:
                            err = Error(
                                self.line,
                                self.column,
                                "Error: El break no debe tener argumentos",
                                scope.name,
                            )
                            ERRORS_.append(err)
                        else:
                            break
                    elif retorno["type"] == "continue":
                        cond = self.expr.execute(scope)
                        continue
                    else:
                        return retorno
                cond = self.expr.execute(scope)
        else:
            err = Error(
                self.line,
                self.column,
                f"Los tipos no coinciden: se experaba `bool`, se encontro {cond.getType().fullname}",
                scope.name,
            )
            ERRORS_.append(err)
