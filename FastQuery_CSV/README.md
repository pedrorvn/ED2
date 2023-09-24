# Projeto: Consulta de Laptops em Arquivos CSV

## Descrição do Projeto

Esta implementação partiu de um projeto guiado da
plataforma [DataQuest](https://app.dataquest.io/c/86/m/481/guided-project%3A-building-fast-queries-on-a-csv/1/the-dat).
O projeto em questão consiste em desenvolver um programa que realiza consultas em arquivos CSV contendo informações
sobre notebooks. O arquivo CSV é tratado como um banco de dados e contém os seguintes campos para cada notebook:

- **ID:** Um identificador exclusivo para o laptop.
- **Company:** O nome da empresa que produz o laptop.
- **Product:** O nome do laptop.
- **TypeName:** O tipo de laptop.
- **Inches:** O tamanho da tela em polegadas.
- **ScreenResolution:** A resolução da tela.
- **CPU:** O processador do laptop.
- **RAM:** A quantidade de memória RAM no laptop.
- **Memory:** O tamanho do disco rígido.
- **GPU:** O nome da placa gráfica.
- **OpSys:** O nome do sistema operacional.
- **Weight:** O peso do laptop.
- **Price:** O preço do laptop.

## Funcionalidades Implementadas

No programa entregue, foram implementadas as seguintes funcionalidades:

1. **Busca por ID:** O usuário fornece um ID e o programa retorna o notebook referente ao ID

2. **Busca por preço:** O usuário fornece um valor e o programa retorna notebooks referentes ao valor fornecido

Além dessas funcionalidades, o programa final conta com duas implementações principais, que são o foco dessa entrega:

3. **Busca por Faixa de Preço:** O programa permite que o usuário especifique uma faixa de preço, e ele retornará todos
   os notebooks que se encaixam nessa faixa de preço.

4. **Busca por Aparelho Mais Barato com Certa RAM e Memória:** O programa também oferece a capacidade de buscar o laptop
   mais barato que atenda a critérios específicos de RAM e memória. O usuário pode fornecer valores desejados de RAM e
   memória, e o programa encontrará o laptop mais barato que corresponda a esses critérios.

Este projeto fornece uma maneira eficiente de pesquisar e filtrar laptops com base em critérios de preço, RAM e memória,
tornando mais fácil para os usuários encontrar os laptops que melhor atendem às suas necessidades.

## Discutindo a complexidade das funcionalidades

A seguir, vamos analisar a complexidade nas notações Big O, Big θ e Big Ω 
para cada um dos métodos da classe ``Inventory``.

### Busca por ID

`get_laptop_from_id`:

- **Complexidade no Pior Caso (Big O):** O(n) - O método percorre linearmente a lista de laptops. 
No pior caso, ele precisaria percorrer todos os elementos da lista `n` elementos.
- **Complexidade no Melhor Caso (Big Ω):** O(1) - No melhor caso, o id seria encontrado na primeira posição, 
ou seja, imediatamente ao iniciar a busca.
- **Complexidade Média (Big θ):** O(n) - A complexidade média depende da distribuição dos laptops na lista. 

Uma segunda abordagem seria: ao invés de percorrer a lista para achar o id, salvar previamente, durante a construção do
objeto, um dicionário com chave sendo o id e valor sendo o laptop. Assim, a busca seria feita em O(1), conforme o realizado
no método ``get_laptop_from_id_fast``.

### Busca por preço

`find_laptop_with_price(price)`

- **Complexidade no Pior Caso (Big O):** O(log n) - O método utiliza busca binária para encontrar um laptop por preço.
- **Complexidade no Melhor Caso (Big Ω):** O(1) - Se o preço desejado for encontrado imediatamente.
- **Complexidade Média (Big θ):** O(log n) - Como a busca binária é usada, a complexidade média é O(log n).

Uma segunda abordagem seria: ao invés de percorrer a lista para achar o preço, salvar previamente, durante a construção do
objeto, um set de preços. Assim, a busca seria feita em O(1), conforme o realizado
no método ``check_promotion_dollars_fast``.

### Busca por Faixa de Preço

Para efetuar a busca por faixa de preços, dados preços mínimo e máximo, foram implementados os seguintes métodos:

`find_first_laptop_more_expensive`

- **Complexidade no Pior Caso (Big O):** O(log n) - Também usa busca binária, semelhante ao método anterior.
- **Complexidade no Melhor Caso (Big Ω):** O(1) - Se o laptop mais caro for encontrado imediatamente.
- **Complexidade Média (Big θ):** O(log n) - A média de casos é O(log n) devido à busca binária.

`find_last_laptop_cheaper`

- **Complexidade no Pior Caso (Big O):** O(log n) - Mais uma vez, utiliza busca binária.
- **Complexidade no Melhor Caso (Big Ω):** O(1) - Se o laptop mais barato for encontrado imediatamente.
- **Complexidade Média (Big θ):** O(log n) - A busca binária leva a uma complexidade média de O(log n).

`find_laptops_in_range`

- Este método chama os métodos `find_first_laptop_more_expensive` e `find_last_laptop_cheaper`. Portanto, sua
complexidade geral depende desses métodos.
- Portanto, a complexidade no pior caso, no melhor caso e a complexidade média são as mesmas que os métodos
  chamados, ou seja, O(log n).

### Busca por Aparelho Mais Barato com Certa RAM e Memória

Para efetuar a busca por aparelho mais barato com certa RAM e memória, foram implementados os seguintes métodos:

`find_cheapest_laptop_with_ram_memory`

Este método itera sobre todos os laptops para encontrar aquele com a RAM e memória desejadas. A complexidade
depende do número de laptops a serem verificados.

- **Complexidade no Pior Caso (Big O):** O(n) - Se a busca precisar verificar todos os laptops.
- **Complexidade no Melhor Caso (Big Ω):** O(1) - Se o laptop desejado for o primeiro da lista.
- **Complexidade Média (Big θ):** O(n) - Em média, se for necessário verificar a maioria dos laptops.

`find_cheapest_specs`

Este método também envolve iteração sobre todos os laptops para verificar as especificações desejadas. A
complexidade depende do número de laptops a serem verificados.
- **Complexidade no Pior Caso (Big O):** O(n) - Se a busca precisar verificar todos os laptops.
- **Complexidade no Melhor Caso (Big Ω):** O(1) - Se o laptop desejado for o primeiro da lista.
- **Complexidade Média (Big θ):** O(n) - Em média, se for necessário verificar a maioria dos laptops.

## Desenvolvedores

- [Jordan Marques de Almeida Ramos](https://github.com/jordanmaramos)
- [Pedro Rêgo Vilar Neto](https://github.com/pedrorvn)







