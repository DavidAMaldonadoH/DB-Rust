from Util.Error import ERRORS_, Error
from Util.Expression import Expression
from Util.Retorno import Retorno
from Util.Scope import Scope


class SimpleAccess(Expression):
    def __init__(self, line: int, column: int, id: str):
        super().__init__(line, column)
        self.id = id

    def execute(self, scope: Scope) -> Retorno:
        var = scope.getVar(self.id)
        if var != None:
            if var.getValue() != None:
                return Retorno(var.getValue(), var.getType())
            else:
                err = Error(
                    self.line,
                    self.column,
                    f"A la variable `{self.id}` no se le a asignado un valor anteriormente!",
                    scope.name,
                )
                ERRORS_.append(err)
                raise Exception(err)
        else:
            err = Error(
                self.line,
                self.column,
                f"La variable `{self.id}` no ha sido declarada anteriormente!",
                scope.name,
            )
            ERRORS_.append(err)
            raise Exception(err)
