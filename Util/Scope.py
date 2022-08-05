from typing import Optional
from Util.Error import ERRORS_, Error
from Util.Retorno import Type
from Util.Struct import Struct
from Util.Symbol import SYMBOLS, ReportSymbol, Symbol


class Scope:
    def __init__(self, anterior: Optional["Scope"], name: str):
        self.anterior = anterior
        self.name = name
        self.variables = dict()
        self.structs = dict()
        self.functions = dict()
        self.methods = dict()

    def getGlobal(self):
        scope = self
        while scope.anterior != None:
            scope = scope.anterior
        return scope

    # TODO: no se puedan definir el ambiente global
    def getVar(self, id: str) -> Symbol:
        scope = self
        while True:
            if scope.variables.get(id) != None:
                return scope.variables.get(id)
            scope = scope.anterior
            if scope == None:
                break
        return None

    def saveVar(self, id: str, mut: bool, value: any, type: Type, line: int, col: int):
        scope = self
        while scope != None:
            if self.variables.get(id) != None:
                variable = scope.variables.get(id)
                if variable.isMutable():
                    if variable.getType() == type:
                        scope.variables.update(id, Symbol(id, value, type))
                        SYMBOLS.append(
                            ReportSymbol(id, scope.name, type, "Variable", line, col)
                        )
                        break
                    else:
                        raise Exception(
                            Error(
                                line,
                                col,
                                f"Los tipos no coinciden: se esperaba {variable.type.fullname} y se recibio {type.fullname}",
                                scope.name,
                            )
                        )
                else:
                    raise Exception(
                        Error(
                            line,
                            col,
                            f"{id} no es una variable mutable, no se puede modificar.",
                            scope.name,
                        )
                    )
            scope = scope.anterior
        scope = self
        scope.variables[id] = Symbol(id, mut, value, type)
        SYMBOLS.append(ReportSymbol(id, scope.name, type, "Variable", line, col))

    def saveStruct(self, name: str, items: dict, line: int, col: int):
        if name not in self.structs:
            self.structs[name] = items
        else:
            err = Error(
                line,
                col,
                f"La estructura {name} ya existe.",
                self.name,
            )
            ERRORS_.append(err)
            raise Exception(err)

    def getStruct(self, name: str) -> Struct:
        scope = self
        while True:
            if scope.structs.get(name) != None:
                return scope.structs.get(name)
            scope = scope.anterior
            if scope == None:
                break
        return None
