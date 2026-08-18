class TiposPesquisas:

    def __init__(self, list_order: list, number_search: int):
        self.list_order = list_order
        self.number_search = number_search

    def pesquisa_binaria(self):
        """
        Pesquisa binária se torna eficaz quando se trata
        de uma lista ordenada e de grande tamanho, pois vamos partir
        a lista pela metade até localizar o número desejado.

        Returns:
            str: Notificação que localizou o número e a quantidade de tentativas.
        """

        # len() começa contabilizando do 1, por isso é feito o "-1".
        number_start = 0
        number_end = len(self.list_order) - 1

        repetition = 0

        while number_start <= number_end:
            position_number_index = (number_start + number_end) // 2

            if self.list_order[position_number_index] == self.number_search:
                repetition += 1
                return f"Foi preciso {repetition} tentativas até localizar o número {self.number_search}."

            elif self.number_search > self.list_order[position_number_index]:
                repetition += 1
                number_start = position_number_index + 1

            else:
                repetition += 1
                number_end = position_number_index - 1

    def pesquisa_simples(self) -> str:
        """
        Pesquisa simples é uma pesquisa mais "cara", pelo fato
        de passar item por item da lista, ou seja, se tiver 100
        index e meu número desejado for 100, vai ser preciso 100 tentativas
        para localizar o mesmo.
        A lógica é recomendada para lista curta e sem foco de ampliação ao longo do tempo.

        Returns:
            str: Notificação que localizou o número e a quantidade de tentativas.
        """

        repetition = 0

        for number_current in self.list_order:

            if number_current == self.number_search:
                repetition += 1
                return f"Foi preciso {repetition} tentativas até localizar o número {self.number_search}."
            else:
                repetition += 1


if __name__ == "__main__":
    types_searchs = TiposPesquisas([10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150], 90)
    response_pesquisa_simples = types_searchs.pesquisa_simples()
    print(f"Pesquisa Simples: {response_pesquisa_simples}")
    response_pesquisa_binaria = types_searchs.pesquisa_binaria()
    print(f"Pesquisa Binária: {response_pesquisa_binaria}")
