class StructuresDict:

    def __init__(self, data_none, data_values):
        self.data_none = data_none
        self.data_values = data_values

    # Coletando um valor que pertence a chave informada.
    def get_dict(self) -> str:
        value_current = self.data_values
        return_value = value_current["nome"]

        return f"O valor {return_value} pertence a chave nome."

    # Criação de uma estrutura de dados dict do zero.
    def create_dict(self) -> dict:

        value_current = self.data_none
        value_current["nome"] = "Gabriel"
        value_current["profissao"] = "programador"
        value_current["estado"] = "São Paulo"

        return value_current

    # Atualizando o valor de uma chave existente e criando uma nova chave com valor.
    def update_dict(self) -> dict:

        value_current = self.data_values
        value_current["idade"] = 22
        value_current["pais"] = "Brasil"

        return value_current

    # Removendo uma chave e valor da estrutura de de dados.
    def delete_dict(self) -> str:

        value_current = self.data_values
        return_value = value_current.pop("idade")

        return f"Chave apagada: idade. Onde possuia o valor: {return_value}"


if __name__ == "__main__":

    data_one = {}
    data_two = {"nome": "Gabriel", "idade": 20}

    structures_dict = StructuresDict(data_one, data_two)
    print(structures_dict.get_dict())
    print(structures_dict.create_dict())
    print(structures_dict.update_dict())
    print(structures_dict.delete_dict())
