from inventory import Inventory

inventory = Inventory('csv_and_dataproc/output_laptops.csv')

start = input("Deseja buscar algum modelo (S ou N)? ")
if start == "N":
    print("Certo!")
while start == "S":
    p1 = input("Como deseja buscar? \n1 - Por faixa de preço (em euros); \n2 - O mais barato por RAM e memória\nR: ")
    if p1 == "1":
        minimo = input("Nestes campos digite apenas o valor\nDigite o menor valor desejado (€): ")
        maximo = input("Digite o maior valor desejado (€): ")
        laptops = inventory.find_laptops_in_range(int(minimo),int(maximo))
        if laptops == -1:
            print("Não há aparelhos nessa faixa de valor.")
        else:
            for line in laptops:
                linha = ' '.join(map(str, line))  # Converte os elementos em strings e junta-os com espaço
                print(linha)
    if p1 == "2":
        ram = input("Lembre de colocar a unidade (em GB ou TB)\nQual a quantidade de RAM desejado: ")
        memory = input("Qual a quantidade de Memória desejada: ")
        laptop = inventory.find_cheapest_specs(ram,memory)
        print(laptop)
    start = input("Deseja buscar outro modelo (S ou N)? ")
    



