class Function:
    def __init__(self, id: str, parameters: list, code: any, type: any, public: bool):
        self.id = id
        self.parameters = parameters
        self.code = code
        self.type = type
        self.public = public
