class StructuresArray:

    def __init__(self, data_none, data_values):
        self.data_none = data_none
        self.data_values = data_values

    # Coletando o primeiro index do array.
    def get_array(self) -> str:

        value_current = self.data_values
        return_value = value_current[0]

        return f"O valor do index 0 é: {return_value}"

    # Criando um array do zero.
    def create_array(self) -> list:

        value_current = self.data_none
        value_current.append("Python")
        value_current.append("Java")
        value_current.append("SQL")

        return value_current

    # Atualizando o index existente e inserindo um novo index no array.
    def update_array(self) -> list:

        value_current = self.data_values
        value_current[1] = 22
        value_current.append("Catolico")

        return value_current

    # Excluindo o último index e um index desejado.
    def delete_array(self) -> str:

        value_current = self.data_values
        value_current.pop()
        value_current.remove("Gabriel")

        return f"Array após usar o pop e remove: {value_current}"


if __name__ == "__main__":

    data_none = []
    data_values = ["Gabriel", 20, "Programador", "Brasileiro"]

    structures_array = StructuresArray(data_none, data_values)
    print(structures_array.get_array())
    print(structures_array.create_array())
    print(structures_array.update_array())
    print(structures_array.delete_array())
