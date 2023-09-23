from inventory import Inventory

inventory = Inventory('csv_and_dataproc/output_laptops.csv')
'''target_range = inventory.find_laptops_in_range(300,310)
for line in target_range:
    linha = ' '.join(map(str, line))  # Converte os elementos em strings e junta-os com espaço
    print(linha)'''

print(inventory.find_cheapest_laptop_with_ram_memory(8,128))

