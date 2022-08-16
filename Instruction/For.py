from typing import Optional
from Util.Instruction import Instruction
from Util.Expression import Expression
from Util.Error import ERRORS_, Error
from Util.Retorno import Type
from Util.Scope import Scope


class For(Instruction):
    def __init__(
        self,
        line: int,
        column: int,
        id: str,
        start: Expression,
        end: Optional[Expression],
        code: Instruction,
    ):
        super().__init__(line, column)
        self.id = id
        self.start = start
        self.end = end
        self.code = code

    def execute(self, scope: Scope) -> any:
        start_expr = self.start.execute(scope)
        if start_expr.getType() == Type.Int or start_expr.getType() == Type.Usize:
            end_expr = self.end.execute(scope)
            if end_expr.getType() == Type.Int or end_expr.getType() == Type.Usize:
                for_scope = Scope(scope, "For")
                for_scope.saveVar(
                    self.id,
                    True,
                    start_expr.getValue(),
                    start_expr.getType(),
                    self.line,
                    self.column,
                )
                var = for_scope.getVar(self.id)
                while var.getValue() < end_expr.getValue():
                    retorno = self.code.execute(for_scope)
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
                            var.value = var.value + 1
                            continue
                        else:
                            return retorno
                    var.value = var.value + 1
        elif start_expr.getType() == Type.Array or start_expr.getType() == Type.Vector:
            for_scope = Scope(scope, "For")
            for_scope.saveVar(
                self.id,
                True,
                start_expr.getValue().data[0].value,
                start_expr.getValue().data[0].type,
                self.line,
                self.column,
            )
            var = for_scope.getVar(self.id)
            index = 0
            while index < len(start_expr.getValue().data):
                var.value = start_expr.getValue().data[index].value
                retorno = self.code.execute(for_scope)
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
                        index = index + 1
                        continue
                    else:
                        return retorno
                index = index + 1
        else:
            err = Error(
                self.line,
                self.column,
                "Error: La expresion inicial del for debe ser un entero o un arreglo",
                scope.name,
            )
            ERRORS_.append(err)
