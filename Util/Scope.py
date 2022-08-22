from typing import Optional
from Util.Error import ERRORS_, Error
from Util.Module import BASES, TABLAS, Module
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
        self.modules = dict()

    def getGlobal(self):
        while self.anterior != None:
            self = self.anterior
        return self

    def getVar(self, name: str) -> Symbol:
        while True:
            if name in self.variables:
                return self.variables[name]
            if self.anterior == None:
                break
            self = self.anterior
        return None

    def saveVar(self, id: str, mut: bool, value: any, type: Type, line: int, col: int):
        self.variables[id] = Symbol(id, mut, value, type)
        SYMBOLS.append(ReportSymbol(id, self.name, type, "Variable", line, col))

    def saveStruct(self, name: str, items: Struct, line: int, col: int):
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
        while True:
            if name in self.structs:
                return self.structs[name]
            if self.anterior == None:
                break
            self = self.anterior
        return None

    def saveFunction(self, id: str, fn: dict, line: int, col: int):
        if id not in self.functions:
            self.functions[id] = Function(
                id, fn["parameters"], fn["code"], fn["type"], fn["public"]
            )
        else:
            err = Error(
                line,
                col,
                f"La función {id} ya existe.",
                self.name,
            )
            ERRORS_.append(err)

    def getFunction(self, name: str) -> Function:
        while True:
            if name in self.functions:
                return self.functions[name]
            if self.anterior == None:
                break
            self = self.anterior
        return None

    def saveModule(self, name: str, mod: dict, line: int, col: int):
        if name not in self.modules:
            self.modules[name] = Module(name, mod["scope"], mod["father"], mod["public"])
            if mod["father"] == "Global":
                BASES.append({"name": name, "tables": 0, "line": line})
            else:
                for base in BASES:
                    if base["name"] == mod["father"]:
                        base["tables"] += 1
                        break
                TABLAS.append({"name": name, "base": mod["father"], "line": line})
        else:
            err = Error(
                line,
                col,
                f"El módulo {name} ya existe.",
                self.name,
            )
            ERRORS_.append(err)
