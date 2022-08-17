from Util.Error import ERRORS_, Error
from Util.Retorno import Retorno, Type
from Util.Expression import Expression
from Util.Instruction import Instruction
from Util.Scope import Scope


class FunctionCall(Instruction):
    def __init__(self, line: int, column: int, name: str, args: list[Expression]):
        super().__init__(line, column)
        self.name = name
        self.args = args

    def execute(self, scope: Scope) -> any:
        fn = scope.getFunction(self.name)
        if fn is not None:
            fn_scope = Scope(scope, fn.id)
            fn.code.name = fn.id
            same_types = True
            for i in range(len(fn.parameters)):
                arg = self.args[i].execute(scope)
                if fn.parameters[i]["type"] != arg.type:
                    same_types = False
                    break
                else:
                    fn_scope.saveVar(
                        fn.parameters[i]["name"],
                        True,
                        arg.value,
                        arg.type,
                        self.line,
                        self.column,
                    )
            if same_types:
                retorno = fn.code.execute(fn_scope)
                if fn.type is not Type.Null:
                    if retorno is not None:
                        if retorno["type"] == "return":
                            if retorno["value"].type == fn.type:
                                return Retorno(
                                    retorno["value"].value, retorno["value"].type
                                )
                            else:
                                err = Error(
                                    self.line,
                                    self.column,
                                    f"El tipo de retorno de la función {self.name} no coincide con el valor retornado.",
                                    scope.name,
                                )
                                ERRORS_.append(err)
                        else:
                            err = Error(
                                self.line,
                                self.column,
                                f"El valor de retorno no es el esperado",
                                scope.name,
                            )
                            ERRORS_.append(err)
                    else:
                        err = Error(
                            self.line,
                            self.column,
                            f"Se esperaba un valor de retorno",
                            scope.name,
                        )
                        ERRORS_.append(err)
                else:
                    if retorno is not None:
                        err = Error(
                            self.line,
                            self.column,
                            f"La función {self.name} no debe retornar ningún valor.",
                            scope.name,
                        )
                        ERRORS_.append(err)
            else:
                err = Error(
                    self.line,
                    self.column,
                    "Los tipos de los parámetros establecidos no coinciden con los brindados en la llamada!",
                    scope.name,
                )
                ERRORS_.append(err)
        else:
            err = Error(
                self.line,
                self.column,
                f"La función {self.name} no ha sido declarada!.",
                scope.name,
            )
            ERRORS_.append(err)
