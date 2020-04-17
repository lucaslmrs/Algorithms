class Customer:
    def __init__(self, name: str, cpf: str):
        self.__name = name
        self.__cpf = cpf

    @property
    def name(self):
        return self.__name

    @property
    def cpf(self):
        return self.__cpf
