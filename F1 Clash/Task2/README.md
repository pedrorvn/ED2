# Projeto de Geração de Possibilidades de Setup de Carros (Task 1)

Este projeto visa criar todas as possíveis configurações de setup de carros para um jogo de corrida e gerar um histograma representando a distribuição do "Team Score" para essas configurações.

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

