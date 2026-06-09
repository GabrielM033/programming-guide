class StructuresTupla:

    def __init__(self, tupla_values):
        self.tupla_values = tupla_values

    # Coletando o primeiro valor da tupla.
    def get_tupla(self) -> str:

        tupla_current = self.tupla_values
        return_value = tupla_current[0]

        return f"A primeira posição é: {return_value}"

    # Criando uma nova tupla. A tupla é imutável, ou seja, não tem como editar.
    def new_tupla(self) -> str:

        tupla_current = self.tupla_values
        return_new_tupla = tupla_current + ("Catolico", )

        return f"A nova tupla é: {return_new_tupla}"


if __name__ == "__main__":

    data_tupla = ("Gabriel", 22, "Programador", "Brasileiro")

    structures_tupla = StructuresTupla(data_tupla)
    print(structures_tupla.get_tupla())
    print(structures_tupla.new_tupla())
