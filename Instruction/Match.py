from email.policy import default
from typing import Optional
from Util.Error import ERRORS_, Error
from Util.Expression import Expression
from Util.Instruction import Instruction
from Util.Scope import Scope


class Match(Instruction):
    def __init__(
        self,
        line: int,
        column: int,
        expr: Expression,
        cases: list[Instruction],
        default: Optional[Instruction],
    ):
        super().__init__(line, column)
        self.expr = expr
        self.cases = cases
        self.default = default

    def execute(self, scope: Scope) -> any:
        var = self.expr.execute(scope)
        same_types = True
        for case in self.cases:
            for expr in case.exprs:
                val = expr.execute(scope)
                if val.type != var.type:
                    same_types = False
                    break
        if same_types:
            index = -1
            for i, case in enumerate(self.cases):
                for expr in case.exprs:
                    val = expr.execute(scope)
                    if val.value == var.value:
                        index = i
                        break
            retorno = None
            if index != -1:
                retorno = self.cases[index].execute(scope)
            else:
                if self.default is not None:
                    retorno = self.default.execute(scope)
                # TODO: else: error
            if retorno is not None:
                return retorno
        else:
            err = Error(
                self.line,
                self.column,
                f"Los tipos no coinciden: se experaba `{var.type.fullname}`, se encontro un tipo diferente en el caso",
                scope.name,
            )
            ERRORS_.append(err)
