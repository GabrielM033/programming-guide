
class TypesSearchs:

    def __init__(self, list_order: list, number_search: int):
        self.list_order = list_order
        self.number_search = number_search

    def search_binarios(self):
        """
        Pesquisa binários se torna eficaz quando se trata
        de uma lista ordenada e de grande tamanho, pois vamos partir
        a lista ao meio e validar se o número desejado está acima ou abaixo,
        e assim localizamos a pesquisa bem mais rápido que um for simples.

        Returns:
            str: Notificação que localizou o número e a quantidade de tentativas.
        """

        start = 0
        end = len(self.list_order) - 1

        while start <= end:
            quite = (start + end) // 2

            if self.list_order[quite] == self.number_search:
                return quite

            elif self.number_search > self.list_order[quite]:
                start = quite + 1

            else:
                end = quite - 1
        return -1

    def search_simple(self) -> str:
        """
        Pesquisa simples é uma pesquisa mais "cara", pelo fato
        de passar item por item da lista, ou seja, se tiver 100
        index e meu número desejado for 100, vai ser preciso 100 tentativas
        para localizar o mesmo.
        A lógica é recomendada para lista curta e sem foco de ampliação ao longo do tempo.

        Returns:
            str: Notificação que localizou o número e a quantidade de tentativas.
        """

        data = self.list_order
        value_search = 10
        number_repetitions = 1

        for number_current in data:

            if number_current == value_search:
                return f"Localizei o número ({value_search}), precisei de {number_repetitions} tentativas!"
            else:
                number_repetitions += 1


if __name__ == "__main__":
    types_searchs = TypesSearchs([10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150], 90)
    # response = types_searchs.search_simple()
    response = types_searchs.search_binarios()

    print(response)
