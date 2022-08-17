from Util.Error import ERRORS_, Error
from Util.Expression import Expression
from typing import Optional
from Util.Instruction import Instruction
from Util.Retorno import Type
from Util.Scope import Scope


class If(Instruction):
    def __init__(
        self,
        line: int,
        column: int,
        expr: Expression,
        code: Instruction,
        elsest: Optional[Instruction],
    ):
        super().__init__(line, column)
        self.expr = expr
        self.code = code
        self.elsest = elsest

    def execute(self, scope: Scope) -> any:
        self.code.setName("If")
        cond = self.expr.execute(scope)
        if cond.getType() == Type.Bool:
            if cond.getValue() == True:
                return self.code.execute(scope)
            elif self.elsest != None:
                return self.elsest.execute(scope)
        else:
            err = Error(
                self.line,
                self.column,
                f"Los tipos no coinciden: se experaba `bool`, se encontro {cond.getType().fullname}",
                scope.name,
            )
            ERRORS_.append(err)
