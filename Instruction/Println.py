import re
from Util.Error import ERRORS_, Error
from Util.Expression import Expression
from Util.Instruction import Instruction
from Util.Retorno import Retorno, Type
from Util.Scope import Scope

CONSOLE_CONTENT: list[str] = []


class Println(Instruction):
    def __init__(self, line: int, column: int, values: list[Expression]):
        super().__init__(line, column)
        self.values = values

    def execute(self, scope: Scope) -> any:
        values_: list[Retorno] = []
        for value in self.values:
            values_.append(value.execute(scope))
        if len(values_) > 1:
            input_ = str(values_[0].getValue())
            output: str = ""
            isNone: bool = False
            if "{}" in input_ or "{:?}" in input_:
                fields = re.split(r"{}|{\:\?}", values_[0].getValue())
                for i, field in enumerate(fields):
                    if i != len(fields) - 1:
                        result = ""
                        if values_[i + 1] is None:
                            isNone = True
                            break
                        if isinstance(values_[i + 1].getValue(), bool):
                            result = str(values_[i + 1].getValue()).lower()
                        elif (values_[i + 1].getType() != Type.Array) and (
                            values_[i + 1].getType() != Type.Vector
                        ):
                            result = str(values_[i + 1].getValue())
                        else:
                            result = self.printLists(values_[i + 1])
                        output += field + result
                    else:
                        output += field
                if not isNone:
                    CONSOLE_CONTENT.append(output)
                else:
                    err = Error(
                        self.line,
                        self.column,
                        "El valor recibido no se puede imprimir",
                        scope.name,
                    )
                    ERRORS_.append(err)
            else:
                err = Error(
                    self.line,
                    self.column,
                    "El argumento de formato debe ser una cadena de formato",
                    scope.name,
                )
                ERRORS_.append(err)
        elif "{}" in str(values_[0].getValue()) or "{:?}" in str(values_[0].getValue()):
            err = Error(
                self.line,
                self.column,
                "Argumentos posicionales en la cadena de formato, pero no se le dieron argumentos",
                scope.name,
            )
            ERRORS_.append(err)
        else:
            if values_[0].getType() == Type.Str:
                CONSOLE_CONTENT.append(values_[0].getValue())
            else:
                err = Error(
                    self.line,
                    self.column,
                    "El argumento de formato debe ser una cadena de formato",
                    scope.name,
                )
                ERRORS_.append(err)

    def printLists(self, var: any) -> str:
        output = ""
        if var.getType() == Type.Array or var.getType() == Type.Vector:
            output += "["
            for i, val in enumerate(var.value.data):
                if val.getType() == Type.Array or val.getType() == Type.Vector:
                    if i != len(var.value.data) - 1:
                        output += self.printLists(val) + ", "
                    else:
                        output += self.printLists(val)
                else:
                    if i != len(var.value.data) - 1:
                        if val.getType() == Type.Str:
                            output += '"' + str(val.getValue()) + '", '
                        elif val.getType() == Type.Bool:
                            output += str(val.getValue()).lower() + ", "
                        else:
                            output += str(val.getValue()) + ", "
                    else:
                        if val.getType() == Type.Str:
                            output += '"' + val.getValue() + '"'
                        elif val.getType() == Type.Bool:
                            output += str(val.getValue()).lower()
                        else:
                            output += str(val.getValue())
            output += "]"
        return output
