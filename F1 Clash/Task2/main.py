import matplotlib.pyplot as plt
import networkx as nx
from Setup.cars_setup import CarSetup



# Lista para armazenar todos os setups possíveis
all_setups = []

# Lista para armazenar os valores do Team Score
team_scores = []

# Definindo o cutoff
cutoff = 880

# Gerar todas as combinações possíveis
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
                            "setup": setup,
                            "contributions": contributions
                        }
                        all_setups.append(setup_data)

                        # Calcular o Team Score
                        team_score = contributions["Speed"] + contributions["Cornering"] + contributions["Power Unit"] + contributions["Reliability"] + (contributions["Average Pit Stop Time"] / 0.02)
                        
                        # Armazenar o Team Score
                        if team_score>=cutoff:
                            team_scores.append(team_score)



# Plotar o histograma
'''
plt.hist(team_scores, bins=50, color='blue', edgecolor='black')
plt.xlabel("Team Score")
plt.ylabel("Número de Configurações")
plt.title(f"Histograma do Team Score (Limite = {cutoff})")
plt.show()
'''
# Criar um objeto de grafo
G = nx.Graph()

# Adicionar nós ao grafo com base nos dados do histograma
for i, valor in enumerate(team_scores):
    G.add_node(i, weight=valor)

# Adicionar arestas (conexões entre os nós)
for i in range(len(team_scores) - 1):
    G.add_edge(i, i + 1)

# Layout do gráfico
pos = nx.spring_layout(G)

# Obter pesos dos nós
node_weights = [G.nodes[n]['weight'] for n in G.nodes]

# Desenhar nós
nx.draw_networkx_nodes(G, pos, node_size=node_weights, node_color='b')

# Desenhar arestas
nx.draw_networkx_edges(G, pos, edgelist=G.edges, edge_color='gray')

# Adicionar rótulos aos nós
labels = {i: f'Node {i}\nWeight {node_weights[i]}' for i in G.nodes}
nx.draw_networkx_labels(G, pos, labels)

# Mostrar o gráfico
plt.axis('off')
plt.show()

