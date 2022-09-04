from Expression.Literal import Literal
from Util.Error import ERRORS_, Error
from Util.Retorno import Retorno, Type, getNestedType
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
                arg = self.args[i]["value"].execute(scope)
                if arg.type == Type.Struct:
                    right_type = arg.value.name
                    if right_type != fn.parameters[i]["type"]:
                        same_types = False
                        break
                    fn_scope.saveVar(
                        fn.parameters[i]["name"],
                        fn.parameters[i]["mut"],
                        arg.value,
                        arg.type,
                        self.line,
                        self.column,
                    )
                elif arg.type == Type.Vector:
                    if isinstance(fn.parameters[i]["type"], dict):
                        if isinstance(fn.parameters[i]["type"]["type"], str):
                            if "::" in fn.parameters[i]["type"]["type"]:
                                fn.parameters[i]["type"]["type"] = fn.parameters[i]["type"][
                                    "type"
                                ].split("::")[-1]
                        left_type = getNestedType(fn.parameters[i]["type"])
                    else:
                        left_type = fn.parameters[i]["type"].getNestedType()
                    if isinstance(arg.value.type, dict):
                        right_type = getNestedType(arg.value.type)
                    else:
                        if arg.value.type == Type.Struct:
                            right_type = "vec<" + arg.value.value.name + ">"
                        else:
                            right_type = "vec<" + arg.value.type.fullname + ">"
                    if left_type != right_type:
                        same_types = False
                        break
                    fn_scope.saveVar(
                        fn.parameters[i]["name"],
                        fn.parameters[i]["mut"],
                        arg.value,
                        arg.type,
                        self.line,
                        self.column,
                    )
                elif arg.type == Type.Array:
                    left_type = getNestedType(fn.parameters[i]["type"])
                    right_type = arg.getValue().getNestedType()
                    if fn.parameters[i]["type"]["size"] == -1:
                        left_type = fn.parameters[i]["type"]["type"].fullname
                        right_type = right_type.split("*")[-1]
                    if left_type != right_type:
                        same_types = False
                        break
                    fn_scope.saveVar(
                        fn.parameters[i]["name"],
                        fn.parameters[i]["mut"],
                        arg.value,
                        arg.type,
                        self.line,
                        self.column,
                    )
                else:
                    if (
                        isinstance(self.args[i]["value"], Literal)
                        and arg.type == Type.Int
                    ):
                        arg.type = (
                            Type.Usize
                            if fn.parameters[i]["type"] == Type.Usize
                            else Type.Int
                        )
                    if fn.parameters[i]["type"] != arg.type:
                        same_types = False
                        break
                    fn_scope.saveVar(
                        fn.parameters[i]["name"],
                        fn.parameters[i]["mut"],
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
                            return_type = retorno["value"].type
                            function_type = fn.type
                            if return_type == Type.Struct:
                                return_type = retorno["value"].value.name
                            elif (
                                return_type == Type.Vector or return_type == Type.Array
                            ):
                                if isinstance(retorno["value"].value.type, dict):
                                    return_type = getNestedType(
                                        retorno["value"].value.type
                                    )
                                else:
                                    return_type = retorno["value"].value.getNestedType()
                                function_type = getNestedType(fn.type)
                            if return_type == function_type:
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
