# Requisito 02

Esta página contém os resultados da análise de 5 redes de grafos escolhidas. Abaixo estão os gráficos correspondentes para cada uma das redes, seguidos dos resultados.

## Rede 1: Math Overflow temporal network

![Gráfico 1 - Grau de Assortatividade](./images/degree_assortativity1.png)

### Resultados:
- É perceptível que a regressão linear formada é descrescente, o que denota que o coeficiente de assortatividade do grau é negativo. Representando que nós de graus menores tendem a fazer conexões com nós de graus maiores. Isso indica que a rede de interação do mathoverflow é uma rede dissortativa. A dissortatividade nesse contexto é evidenciada por alguns fatos, como o de que alguns membros do MathOverflow têm uma alta atividade no site, fazendo muitas perguntas e respostas já outros membros podem ter uma atividade relativamente baixa, com menos perguntas e respostas.

## Rede 2: Amazon product co-purchasing network, March 02 2003

![Gráfico 2 - Grau de Assortatividade](./images/degree_assortativity2.png)

### Resultados:
- Nesse caso, a regressão linear é praticamente constante, ou seja, não há uma assortatividade clara, o que indicaria um coeficiente de assortatividade do grau próximo à zero. Indicando nesse caso, que produtos que são comprados juntos na Amazon (na época que foram extraídas essas informações) não tendem a ter relação entre si, podendo ser de uma mesma categoria ou não.

## Rede 3: Notre Dame web graph

![Gráfico 3](./images/degree_assortativity3.png)

### Resultados:
- Aqui, novamente é perceptível que a regressão linear formada é levemente descrescente, e que o coeficiente de assortatividade do grau é próximo de zero, mas negativo. Representando que nós de graus menores tendem a fazer conexões com nós de graus maiores, representando uma rede dissortativa. Em redes de hiperlinks de sites de universidades, a dissortatividade ocorre porque a página inicial da universidade (a página principal) costuma ter muitos links para várias partes do site, como departamentos, programas acadêmicos, faculdades e recursos diversos. Essas páginas principais, que são ricas em links, têm um alto grau.

## Rede 4: California road network

![Gráfico 4](./images/degree_assortativity4.png)

### Resultados:
- Nessa análise, a regressão linear formada é levemente crescente, o coeficiente de assortatividade do grau é positivo. Representando que nós de graus maiores tendem a fazer conexões com nós de graus maiores, representando uma rede assortativa. Isso ocorre porque rodovias principais se ligam a outras de grande capacidade. No entanto, essa tendência não é dominante, e outros fatores práticos também influenciam a conectividade das rodovias, como a geografia e as necessidades de transporte. 

## Rede 5: Social circles - Twitter

![Gráfico 5](./images/degree_assortativity5.png)

### Resultados:
- A análise revelou que a rede de 'circles' no Twitter é dissortativa (regressão linear negativa), indicando que os perfis tendem a se conectar preferencialmente a outros com graus diferentes. Isso sugere diversidade nas conexões, resiliência a falhas e possíveis implicações no comportamento de interação na plataforma.

## Conclusão

Neste requisito, foram analisadas cinco redes de grafos e apresentados os resultados e gráficos correspondentes. Em resumo, redes podem exibir padrões de assortatividade e dissortatividade, dependendo das características e das conexões entre os nós. Portanto, a análise de assortatividade ou dissortatividade deve ser sempre considerada em relação às características específicas da rede em questão.
