from time import asctime


class Error(Exception):
    def __init__(self, line: int, column: int, description: str, env: str):
        self.line = line
        self.column = column
        self.env = env
        self.description = description
        self.type = type
        self.time = asctime()

    def __str__(self) -> str:
        return f"Error: {self.description}.\n$ Línea: {self.line} - Columna: {self.column}"


ERRORS_: list[Error] = list()
