import matplotlib.pyplot as plt
from Setup.cars_setup import CarSetup

# Lista para armazenar todos os setups possíveis
all_setups = []

# Lista para armazenar os valores do Team Score
team_scores = []

#Definindo o cutoff
cutoff = 700

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
                        if team_score >= cutoff:
                            team_scores.append(team_score)

# Plotar o histograma
plt.hist(team_scores, bins=50, color='blue', edgecolor='black')
plt.xlabel("Team Score")
plt.ylabel("Número de Configurações")
plt.title(f"Histograma do Team Score (Limite = {cutoff})")
plt.show()