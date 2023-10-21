import matplotlib.pyplot as plt
from Setup.cars_setup import CarSetup
import networkx as nx
import seaborn as sns
from Setup.bottles import bottles
from nxviz import CircosPlot
from Setup.drivers import drivers
import itertools

""" ###################### TAREFA 1 ######################"""

# Lista para armazenar todos os setups possíveis
all_setups = []

# Lista para armazenar os valores do Team Score
team_scores = []

# Definindo o cutoff
cutoff = 880

# Gerar todas as combinações possíveis
setup_id = 'Setup '
id_count = 0
for brakes in CarSetup.brakes_options:
    for engine in CarSetup.engine_options:
        for suspension in CarSetup.suspension_options:
            for front_rear in CarSetup.front_wing_options:
                for rear_wing in CarSetup.rear_wing_options:
                    for gearbox in CarSetup.gearbox_options:
                        setup = CarSetup(brakes, engine, suspension, front_rear, rear_wing, gearbox)
                        contributions = setup.calculate_contributions()

                        # Armazenar configuração e contribuições como um dicionário
                        setup_data = {
                            "id": setup_id + str(id_count),
                            "setup": setup,
                            "contributions": contributions
                        }
                        all_setups.append(setup_data)
                        id_count += 1

                        # Calcular o Team Score
                        team_score = contributions["speed"] + contributions["cornering"] + contributions["power_unit"] + \
                                     contributions["reliability"] + (contributions["avg_pit_stop_time"] / 0.02)

                        # Armazenar o Team Score
                        if team_score >= cutoff:
                            team_scores.append(team_score)

# Plotar o histograma
plt.figure(figsize=(8, 6))  # Ajuste o tamanho da figura para o histograma
plt.hist(team_scores, bins=50, color='blue', edgecolor='black')
plt.xlabel("Team Score")
plt.ylabel("Número de Configurações")
plt.title(f"Histograma do Team Score (Limite = {cutoff})")
plt.show()  # Mostra o histograma

""" ###################### TAREFA 2 ######################"""
# Crie um gráfico direcionado
G1 = nx.DiGraph()

# Dicionário para manter a contagem de ocorrências de cada configuração
config_count = {}

# Adicione os nós ao gráfico baseado no Team Score que é maior que o cutoff e crie arestas
for setup_data in all_setups:
    contributions = setup_data["contributions"]
    score = (contributions["speed"] +
             contributions["cornering"] +
             contributions["power_unit"] +
             contributions["reliability"] +
             (contributions["avg_pit_stop_time"] / 0.02))
    if score >= cutoff:
        setup_id = setup_data["id"]
        G1.add_node(setup_id, setup=setup_data["setup"], score=score)

        # Adiciona arestas entre o setup e seus componentes e mantém a contagem
        for component in ["brakes", "engine", "suspension", "front_wing", "rear_wing", "gearbox"]:
            component_value = setup_data["setup"].__dict__[component]
            if component_value not in G1:
                G1.add_node(component_value, score=0)
                config_count[component_value] = 1
            else:
                config_count[component_value] += 1
            G1.add_edge(setup_id, component_value)

# Atualize os tamanhos dos nós
sizes = [
    G1.nodes[node]['score'] * 10 if 'score' in G1.nodes[node] and G1.nodes[node]['score'] else config_count[node] * 100 for
    node in G1.nodes()]

colors = ['red' if 'score' in G1.nodes[node] and G1.nodes[node]['score'] else 'black' for node in G1.nodes()]

# Desenhe o gráfico
plt.figure(figsize=(15, 15))  # Ajuste o tamanho da figura para o gráfico nx
pos = nx.kamada_kawai_layout(G1)  # Use o layout kamada_kawai
nx.draw(G1, pos, with_labels=True, node_size=sizes, node_color=colors, font_size=8, alpha=0.7)
plt.title("Relação entre Configurações e Componentes")
plt.show()  # Mostra o gráfico nx

# Obter "Out Degree" dos vértices associados aos setups
out_degrees = [deg for node, deg in G1.out_degree() if 'score' in G1.nodes[node]]

# Criar o gráfico da Função de Densidade de Probabilidade (PDF) usando Seaborn
plt.figure(figsize=(10, 6))
sns.kdeplot(out_degrees, fill=True)
plt.title('PDF do "Out Degree" dos setups')
plt.xlabel('Out Degree')
plt.ylabel('Densidade')
plt.show()

""" ###################### TAREFA 3 ######################"""

# 1. Cria o grafo bipartido
G2 = nx.Graph()

# Adicionando os nós e arestas ao grafo bipartido
for bottle, attributes in bottles.items():
    G2.add_node(bottle, bipartite=0)
    for attr, value in attributes.items():
        if not G2.has_node(attr):
            G2.add_node(attr, bipartite=1)
        G2.add_edge(bottle, attr, weight=value)

# Separando os nós em dois grupos: garrafinhas e propriedades
bottle_nodes = [n for n, d in G2.nodes(data=True) if d['bipartite'] == 0]
attribute_nodes = [n for n, d in G2.nodes(data=True) if d['bipartite'] == 1]

# Definindo posições para os nós
pos = dict()
pos.update((node, (1, index)) for index, node in enumerate(bottle_nodes))
pos.update((node, (2, index)) for index, node in enumerate(attribute_nodes))

# Consolidar as arestas repetidas e calcular o número de arestas entre cada par de nós
edge_weights = {}
for (u, v, data) in G2.edges(data=True):
    if (u, v) not in edge_weights:
        edge_weights[(u, v)] = data['weight']
    else:
        edge_weights[(u, v)] += data['weight']

# Criar um novo grafo com as arestas consolidadas
G3 = nx.Graph()
G3.add_nodes_from(G2.nodes(data=True))
for (u, v), weight in edge_weights.items():
    G3.add_edge(u, v, weight=weight)

# Definindo posições para os nós (como antes)
pos = dict()
pos.update((node, (1, index)) for index, node in enumerate(bottle_nodes))
pos.update((node, (2, index)) for index, node in enumerate(attribute_nodes))

# Desenhando o grafo
plt.figure(figsize=(15,15))
nx.draw(G3, pos, with_labels=True, node_size=700, node_color='skyblue', font_size=10)
labels = nx.get_edge_attributes(G3, 'weight')
nx.draw_networkx_edge_labels(G3, pos, edge_labels=labels)
plt.title("Grafo Bipartido das Garrafinhas e Propriedades")
plt.show()


""" ###################### TAREFA 4 ######################"""

#Vamos ficar devendo essa tarefa, pois não conseguimos fazer.