from Util.Error import ERRORS_, Error
from Util.Expression import Expression
from Util.Retorno import Retorno, Type, getNestedType
from Util.Scope import Scope
from Util.Struct import Struct
from Util.Symbol import Symbol


class CreateStruct(Expression):
    def __init__(self, line: int, column: int, name: str, items: dict):
        super().__init__(line, column)
        self.name = name
        self.items = items

    def execute(self, scope: Scope) -> Retorno:
        struct_base = scope.getStruct(self.name)
        if struct_base is not None:
            struct = Struct(self.name, True)
            for key, value in self.items.items():
                if key in struct_base.items:
                    val = value.execute(scope)
                    if val.type == Type.Struct:
                        if val.value.name == struct_base.items[key].type:
                            sym = Symbol(key, True, val.value, val.type)
                            struct[key] = sym
                        else:
                            err = Error(
                                self.line,
                                self.column,
                                "Los tipos de struct no coinciden",
                                scope.getName(),
                            )
                            ERRORS_.append(err)
                    elif val.type == Type.Array or val.type == Type.Vector:
                        left_type = getNestedType(struct_base[key].type)
                        right_type = val.getValue().getNestedType()
                        if left_type == right_type:
                            sym = Symbol(key, True, val.value, val.type)
                            struct[key] = sym
                        else:
                            err = Error(
                                self.line,
                                self.column,
                                "Los tipos de array no coinciden",
                                scope.getName(),
                            )
                            ERRORS_.append(err)
                    elif struct_base[key].type == val.type:
                        sym = Symbol(key, True, val.value, val.type)
                        struct[key] = sym
                    else:
                        err = Error(
                            self.line,
                            self.column,
                            f"Tipos no compatibles para el miembro {key}",
                            scope.name,
                        )
                        ERRORS_.append(err)
                else:
                    err = Error(
                        self.line,
                        self.column,
                        f"Miembro {key} no encontrado en el struct {self.name}",
                        scope.name,
                    )
                    ERRORS_.append(err)
            return Retorno(struct, Type.Struct)
        else:
            err = Error(
                self.line,
                self.column,
                f"El Struct {self.name} no ha sido declarado",
                scope.name,
            )
            ERRORS_.append(err)
