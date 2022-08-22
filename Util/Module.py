from typing import Optional


class Module:
    def __init__(self, name: str, scope: any, father: Optional[str], public: bool):
        self.name = name
        self.scope = scope
        self.father = father
        self.public = public


TABLAS: list[dict] = list()
BASES: list[dict] = list()
