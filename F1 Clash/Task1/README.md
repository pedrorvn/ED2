# Projeto de Geração de Possibilidades de Setup de Carros (Task 1)

Esta tarefa visa criar todas as possíveis configurações de setup de carros para um jogo de corrida e gerar um histograma representando a distribuição do "Team Score" para essas configurações.

## Etapas Realizadas

1. **Classe `CarSetup`**: Foi criada uma classe para representar configurações de carros, com características como freios, motor, suspensão, asa dianteira, asa traseira e caixa de câmbio. Cada característica contribui com valores para métricas como velocidade, capacidade de curva, unidade de potência, confiabilidade e tempo médio de pit stop.

2. **Criação de Todas as Possibilidades**: Todas as combinações possíveis de características de carro foram geradas, resultando em um conjunto de configurações únicas. Para cada configuração, foi calculado o "Team Score" com base nas contribuições das características.

3. **Histograma do Team Score**: Um histograma foi criado usando a biblioteca `matplotlib` para representar a distribuição dos valores do "Team Score". As configurações com "Team Score" acima de um determinado limite (cutoff), neste exemplo foi utilizado 700, foram destacadas em um histograma exclusivo.

## Execução do Projeto

Para executar o projeto e visualizar o histograma:

1. Instale as bibliotecas necessárias, como `matplotlib`, `numpy`, e `scikit-learn`, usando o gerenciador de pacotes Python, como `pip`.

2. Execute o código Python fornecido para gerar todas as configurações de carros e calcular o "Team Score".

3. Um histograma será exibido, representando a distribuição do "Team Score" para as configurações acima do cutoff especificado.

4. Você pode personalizar o cutoff e outras configurações de visualização de acordo com suas preferências.

Este projeto permite explorar todas as possibilidades de setup de carros e visualizar como diferentes configurações afetam o desempenho do time no jogo de corrida.

- Histograma completo, com todas as configurações
![Histograma sem cutoff](https://github.com/pedrorvn/ED2/blob/65d4972c6b1f96b30a14bd0a7f17eb8d7388627d/images/Histograma_SemCutoff.png)

<br>

 - Histograma com configurações cujo TeamScore são superiores a 700.
![Histograma com cutoff de 700](https://github.com/pedrorvn/ED2/blob/65d4972c6b1f96b30a14bd0a7f17eb8d7388627d/images/Histograma_ComCutoff.png)


# Análise de Configurações de Setups no Jogo F1 Clash

Nesta tarefa, utilizamos a biblioteca NetworkX e a biblioteca Seaborn para analisar e visualizar as configurações de setups de carros no jogo F1 Clash. Nosso objetivo é entender a relação entre as configurações de setups e seus componentes, com foco no "Team Score" e no "Out Degree."

## O que é "Out Degree"?

No contexto deste projeto e do jogo F1 Clash, o "Out Degree" representa o número de componentes ou cartas que estão conectados a uma configuração específica de setup de carro. Em outras palavras, ele reflete quantos componentes individuais estão presentes em uma configuração de setup e têm um impacto direto nas estatísticas do carro.

Para jogadores do F1 Clash, o "Out Degree" é uma medida importante, pois indica a complexidade e a diversidade das configurações disponíveis. Quanto maior o "Out Degree" de uma configuração, mais componentes estão envolvidos, o que pode resultar em uma configuração mais versátil, capaz de lidar com diferentes aspectos da corrida, como velocidade, curvas, confiabilidade e gerenciamento de pneus.

## Passo a Passo da Análise

A análise é realizada da seguinte forma:

1. É criado um gráfico direcionado usando a biblioteca NetworkX, onde cada nó representa uma configuração de setup de carro. Configurações com um "Team Score" maior ou igual a um valor de corte (cutoff) são incluídas no gráfico.

2. Os setups de carros são avaliados com base em suas contribuições para diferentes componentes, como velocidade, curvas, unidade de potência, confiabilidade e tempo médio de pit stop. As configurações com "Team Score" acima do cutoff são adicionadas ao gráfico, e os componentes individuais (como freios, motor, suspensão, etc.) são conectados a essas configurações.

3. O tamanho dos nós no gráfico é determinado com base no "Team Score" ou no número de configurações que compartilham um componente. Os nós relacionados ao "Team Score" são destacados em vermelho, enquanto os nós relacionados ao "Out Degree" são destacados em preto.

4. O gráfico é desenhado usando a biblioteca NetworkX, com posições definidas pelo algoritmo de layout kamada_kawai.

5. Após o desenho do gráfico, o código obtém o "Out Degree" de cada nó relacionado aos setups e cria um gráfico da Função de Densidade de Probabilidade (PDF) desses valores usando a biblioteca Seaborn. A PDF mostra a distribuição dos "Out Degrees" entre as configurações de setups.

6. Os gráficos resultantes são exibidos para análise visual.

Esta análise ajuda os jogadores do F1 Clash a compreender a relação entre as configurações de setups e seus componentes, destacando o "Team Score" e a distribuição do "Out Degree." Isso pode auxiliar na tomada de decisões informadas ao escolher as configurações de carros, considerando a complexidade das configurações e o impacto direto dos componentes nas estatísticas do carro.


# Grafo Bipartido das Garrafinhas e Propriedades (Task3)

Nesta tarefa, um grafo bipartido é criado para representar as garrafinhas do jogo F1 Clash e suas propriedades correspondentes. O grafo é construído em Python usando a biblioteca NetworkX. Vamos entender os passos da solução:

1. **Criação do Grafo Bipartido:**

   - Primeiro, é criado um grafo bipartido vazio chamado `G2` usando o NetworkX.

2. **Adição de Nós e Arestas:**

   - As garrafinhas do jogo são iteradas a partir do dicionário `bottles`. Para cada garrafinha, um nó é adicionado ao grafo `G2` com a etiqueta `bipartite=0`, indicando que pertence ao grupo das "Garrafinhas."

   - Em seguida, as propriedades de cada garrafinha também são iteradas. Para cada propriedade, verifica-se se ela já existe no grafo `G2`. Caso não exista, um nó é adicionado ao grafo com a etiqueta `bipartite=1`, indicando que pertence ao grupo das "Propriedades." Uma aresta é criada entre a garrafinha e a propriedade, com o peso da aresta igual ao valor da propriedade.

3. **Organização de Grupos:**

   - Os nós do grafo `G2` são separados em dois grupos: "Garrafinhas" e "Propriedades." Isso é feito para facilitar a organização visual do grafo.

4. **Definição de Posições:**

   - Posições são definidas para os nós no grafo `G2`. Os nós do grupo das "Garrafinhas" são posicionados no grupo 1, enquanto os nós do grupo das "Propriedades" são posicionados no grupo 2.

5. **Consolidação de Arestas:**

   - Para evitar arestas duplicadas entre os mesmos pares de nós, as arestas são consolidadas. Isso é feito somando os pesos das arestas repetidas.

6. **Criação do Novo Grafo:**

   - Um novo grafo chamado `G3` é criado, e nós e arestas são adicionados a partir do grafo `G2`.

7. **Reorganização das Posições:**

   - As posições dos nós no grafo `G3` são redefinidas para refletir a estrutura de grupos e as posições previamente definidas.

8. **Visualização do Grafo:**

   - O grafo `G3` é desenhado com nós e arestas. Os nós do grupo das "Garrafinhas" são representados com a cor 'skyblue,' e o tamanho dos nós é proporcional ao número de arestas que eles têm com as propriedades (representado pelo atributo "weight" nas arestas).


