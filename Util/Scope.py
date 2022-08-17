from typing import Optional
from Util.Error import ERRORS_, Error
from .Function import Function
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

    def saveFunction(self, id: str, fn, line: int, col: int):
        scope = self
        if scope.anterior != None:
            err = Error(
                line,
                col,
                f"La funcion {id} no puede ser definida en el ambiente global.",
                scope.name,
            )
            ERRORS_.append(err)
        if id not in scope.functions:
            self.functions[id] = Function(id, fn["parameters"], fn["code"])
        else:
            err = Error(
                line,
                col,
                f"La función {id} ya existe.",
                self.name,
            )
            ERRORS_.append(err)

    def getFunction(self, id: str) -> Function:
        scope = self
        while True:
            if id in self.functions:
                return self.functions[id]
            scope = scope.anterior
            if scope == None:
                break
        return None
