import csv
import re

def convert_csv_prices_and_memory(csv_file):
    # Abra o arquivo CSV de entrada e crie um novo arquivo CSV para saída
    with open(csv_file, 'r') as input_file, open('output_laptops.csv', 'w', newline='') as output_file:
        reader = csv.DictReader(input_file)
        
        # Defina os nomes das colunas no arquivo de saída
        fieldnames = ["laptop_ID", "Company", "Product", "TypeName", "Inches", "ScreenResolution",
                      "Cpu", "Ram", "Memory", "Gpu", "OpSys", "Weight", "Price_euros"]
        
        writer = csv.DictWriter(output_file, fieldnames=fieldnames)
        
        # Escreva o cabeçalho no arquivo de saída
        writer.writeheader()
        
        # Processar cada linha do arquivo de entrada
        for row in reader:
            # Converter o preço para inteiro (arredondando)
            price_str = row["Price_euros"]
            price_int = int(round(float(price_str)))
            row["Price_euros"] = price_int
            
            # Processar a unidade de RAM (GB ou TB)
            ram = row["Ram"]
            if "GB" in ram:
                row["Ram"] = int(ram.split("GB")[0])
            elif "TB" in ram:
                row["Ram"] = int(ram.split("TB")[0]) * 1000
            
            # Processar a unidade de Memória (GB ou TB)
            memory = row["Memory"]
            memory_values = []
            for match in re.finditer(r'\d+', memory):
                value = int(match.group())
                if "TB" in memory:
                    if value < 15: #Pegando somente o valor que estava em TB
                        value *= 1000
                memory_values.append(value)
            
            total_memory = sum(memory_values)
            row["Memory"] = total_memory
            
            # Escrever a linha processada no arquivo de saída
            writer.writerow(row)
    
    print("Conversão concluída. Arquivo de saída 'output_laptops.csv' criado com os preços como inteiros e unidades de RAM/Memória processadas.")

# Chame a função e passe o nome do arquivo CSV de entrada
convert_csv_prices_and_memory('laptops.csv')

