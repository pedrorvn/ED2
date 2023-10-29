# Requisito 03

Este arquivo contém os resultados da análise de 5 redes de grafos escolhidas. Abaixo estão os resultados e informações sobre cada uma das redes.

## Tabela de Resultados

A tabela a seguir apresenta os resultados da análise das cinco redes de grafos selecionadas. Cada linha representa uma rede de grafos diferente e fornece informações sobre o número de nós, o número de arestas, o coeficiente de assortatividade de grau, o número de componentes conectados, o maior componente conectado (GCC), e o coeficiente de agrupamento médio.

|                         | Number of nodes | Number of edges | Degree Assort. Coeff.| Connected Comp |   GCC   | Avg. Clust. Coeff. |
|-------------------------|---------------- |---------------- |--------------------- |----------------|---------|-------------------|
| **Math Overflow**       | 530602          | 706495          | -0.230555318         | 104            | 530297  | 0.0074213            |    
| **Amazon co-purchasing**| 262111          | 899792          | -0.002479342         | 1              | 262111  | 0.41978              |
| **Notre Dame**          | 325729          | 1117563         | -0.05261255          | 1              | 325729  | 0.23462              |
| **California Roads**    | 1965206         | 2766607         | 0.126041672          | 2638           | 1957027 | 0.0463703            |
| **Twitter Circles**     | 81306           | 1342310         | -0.03902312          | 1              | 81306   | 0.5653115            |

## Interpretação dos Resultados

### Math Overflow
A rede "Math Overflow" é caracterizada por um grande número de nós (530,602) e arestas (706,495). O coeficiente de assortatividade de grau negativo sugere que os nós tendem a se conectar com outros nós de grau diferente, resultando em uma rede não muito assortativa em termos de grau. A presença de 104 componentes conectados indica uma estrutura complexa, mas o maior componente conectado (GCC) engloba a maioria dos nós (530,297). O coeficiente de agrupamento médio é relativamente baixo (0.0074213), sugerindo uma baixa tendência ao agrupamento.

### Amazon co-purchasing
Nesta rede, observamos um número considerável de nós (262,111) e arestas (899,792). O coeficiente de assortatividade de grau próximo a zero sugere que os nós tendem a se conectar de maneira não sistemática em relação ao grau. A presença de apenas um componente conectado, que inclui todos os nós (262,111), indica que a rede é totalmente conectada. O coeficiente de agrupamento médio é relativamente alto (0.41978), indicando uma forte tendência ao agrupamento na rede.

### Notre Dame
A rede "Notre Dame" é caracterizada por um grande número de nós (325,729) e arestas (1,117,563). O coeficiente de assortatividade de grau negativo sugere que os nós tendem a se conectar com outros nós de grau diferente. Com apenas um componente conectado contendo todos os nós (325,729), a rede é fortemente conectada. O coeficiente de agrupamento médio é moderado (0.23462), indicando uma tendência ao agrupamento na rede.

### California Roads
Esta rede é muito grande, com um grande número de nós (1,965,206) e arestas (2,766,607). O coeficiente de assortatividade de grau positivo sugere que os nós têm uma tendência a se conectar com outros nós de grau semelhante. A presença de 2,638 componentes conectados reflete uma estrutura complexa, mas o maior componente conectado (GCC) engloba a maioria dos nós (1,957,027). O coeficiente de agrupamento médio é relativamente baixo (0.0463703), indicando uma baixa tendência ao agrupamento na rede.

### Twitter Circles
Nesta rede relativamente pequena, encontramos um número limitado de nós (81,306) e um grande número de arestas (1,342,310). O coeficiente de assortatividade de grau negativo sugere que os nós tendem a se conectar com outros nós de grau diferente. Com apenas um componente conectado que inclui todos os nós (81,306), a rede é altamente conectada. O coeficiente de agrupamento médio é relativamente alto (0.5653115), indicando uma forte tendência ao agrupamento na rede.



