from collections import deque


class StructuresArray:

    # Lista: Se trata de uma estrutura de dados.
    def __init__(self, data_structures) -> list:
        """
        Apresentação de uma estrutura de dados array,
        assim representando uma lista.

        Args:
            data_structures (list): Estrutura de dados array.
        """

        self.data_structures = data_structures

    # Fila: O primeiro index a ser inserido será o primeiro a sair (FIFO).
    def fila(self):
        """
        Vamos executar um cenário de fila e retornar um array criado.

        Returns:
            _array_: Estrutura de dados array.
        """

        array_fila = deque()

        array_fila.append("jatinho")
        array_fila.append("triciclo")

        array_fila.popleft()

        return array_fila

    # Pilha: O último index a ser inserido será o primeiro a sair.
    def pilha(self):
        """
        Vamos executar um cenário de pilha e retornar um array.

        Returns:
            _array_: Estrutura de dados array.
        """

        array_pilha = self.data_structures

        array_pilha.append("navio")

        array_pilha.pop()

        return array_pilha


if __name__ == "__main__":
    """
    Condicionamento que define a lista(array) no método construtor.
    Posteriormente basta chama o método que deseja executar.
    """

    my_array = ["moto", "carro", "barco"]

    structures_array = StructuresArray(my_array)
    response_pilha = structures_array.pilha()
    response_fila = structures_array.fila()

    print(response_fila)
    print(response_pilha)
