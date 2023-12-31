import re
import csv

# Lê o arquivo CSV e extrai as informações em 'header' e 'rows'
with open('csv_and_dataproc/output_laptops.csv') as f:
    reader = csv.reader(f)
    rows = list(reader)
    header = rows[0]
    rows = rows[1:]


# Define a função 'row_price' para ser usada como chave na ordenação
def row_price(row):
    return row[-1]


class Inventory:
    # Inicializa a classe Inventory
    def __init__(self, csv_filename):
        # Lê o arquivo CSV e carrega as informações
        with open(csv_filename) as f:
            reader = csv.reader(f)
            rows = list(reader)
        self.header = rows[0]
        self.rows = rows[1:]

        # Converte os preços para inteiros
        for row in self.rows:
            row[-1] = int(row[-1])

        # Cria um dicionário para mapear IDs de laptops para linhas correspondentes
        self.id_to_row = {}
        for row in self.rows:
            self.id_to_row[row[0]] = row

        # Cria um conjunto de preços únicos
        self.prices = set()
        for row in self.rows:
            self.prices.add(row[-1])

        # Ordena as linhas por preço usando a função 'row_price' como chave
        self.rows_by_price = sorted(self.rows, key=row_price)

    # Método para obter um laptop por ID (busca linear)
    def get_laptop_from_id(self, laptop_id):
        for row in self.rows:
            if row[0] == laptop_id:
                return row
        return None

    # Método para obter um laptop por ID (busca rápida usando o dicionário 'id_to_row')
    def get_laptop_from_id_fast(self, laptop_id):
        if laptop_id in self.id_to_row:
            return self.id_to_row[laptop_id]
        return None

    # Método para verificar promoção de laptops (busca linear)
    def check_promotion_dollars(self, dollars):
        for row in self.rows:
            if row[-1] == dollars:
                return True
        for row1 in self.rows:
            for row2 in self.rows:
                if row1[-1] + row2[-1] == dollars:
                    return True
        return False

    # Método para verificar promoção de laptops (busca rápida usando o conjunto 'prices')
    def check_promotion_dollars_fast(self, dollars):
        if dollars in self.prices:
            return True
        for price in self.prices:
            if dollars - price in self.prices:
                return True
        return False

    # Método para encontrar um laptop por preço (busca binária)
    def find_laptop_with_price(self, target_price):
        range_start = 0
        range_end = len(self.rows_by_price) - 1
        while range_start < range_end:
            range_middle = (range_end + range_start) // 2
            value = self.rows_by_price[range_middle][-1]
            if value == target_price:
                return range_middle
            elif value < target_price:
                range_start = range_middle + 1
            else:
                range_end = range_middle - 1
        if self.rows_by_price[range_start][-1] != target_price:
            return -1
        return range_start

    # Método para encontrar o primeiro laptop mais caro (busca binária)
    def find_first_laptop_more_expensive(self, target_price):
        range_start = 0
        range_end = len(self.rows_by_price) - 1
        while range_start < range_end:
            range_middle = (range_end + range_start) // 2
            price = self.rows_by_price[range_middle][-1]
            if price > target_price:
                range_end = range_middle
            else:
                range_start = range_middle + 1
        if self.rows_by_price[range_start][-1] <= target_price:
            return -1
        return range_start

    # Método para encontrar o último laptop mais barato (busca binária)
    def find_last_laptop_cheaper(self, target_price):
        range_start = 0
        range_end = len(self.rows_by_price) - 1
        last_cheaper = -1  # Inicialmente, nenhum laptop mais barato é encontrado

        while range_start <= range_end:
            range_middle = (range_end + range_start) // 2
            price = self.rows_by_price[range_middle][-1]

            if price < target_price:
                last_cheaper = range_middle  # Atualiza o último laptop mais barato
                range_start = range_middle + 1
            else:
                range_end = range_middle - 1

        return last_cheaper

    # Método para encontrar laptops dentro de uma faixa de preços
    def find_laptops_in_range(self, min_price, max_price):
        if min_price > max_price:
            return -1
        min = self.find_first_laptop_more_expensive(min_price)
        max = self.find_last_laptop_cheaper(max_price)
        laptops_in_range = []
        for i in range(min, max):
            laptops_in_range.append(self.rows_by_price[i])
        if len(laptops_in_range) == 0:
            return -1
        return laptops_in_range

    # Método para encontrar o laptop mais barato com determinada RAM e memória
    def find_cheapest_laptop_with_ram_memory(self, target_ram, target_memory):
        for row in self.rows_by_price:
            if int(row[7]) == target_ram and int(row[8]) == target_memory:
                return row

        return -1  # Retorna -1 se nenhum laptop for encontrado

    # Método para encontrar laptops com as especificações mais baratas
    def find_cheapest_specs(self, ram_text, mem_text):
        # Extrai o valor e a unidade da RAM a partir do texto (exemplo: "8 GB")
        match = re.search(r'(\d+)\s*(TB|GB)', ram_text, re.IGNORECASE)
        if match:
            value = int(match.group(1))
            unit = match.group(2).lower()

            # Converte a unidade para GB, se necessário
            if unit == "tb":
                value *= 1000

            ram = value
        else:
            return -1  # Retorna -1 se não for possível analisar a RAM

        # Extrai o valor e a unidade da memória a partir do texto (exemplo: "256GB")
        match = re.search(r'(\d+)\s*(TB|GB)', mem_text, re.IGNORECASE)
        if match:
            value = int(match.group(1))
            unit = match.group(2).lower()

            # Converte a unidade para GB, se necessário
            if unit == "tb":
                value *= 1000

            memory = value
        else:
            return -1  # Retorna -1 se não for possível analisar a memória

        # Chama o método 'find_cheapest_laptop_with_ram_memory' com os valores extraídos
        return Inventory.find_cheapest_laptop_with_ram_memory(self, ram, memory)

