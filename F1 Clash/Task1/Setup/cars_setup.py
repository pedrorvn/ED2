class CarSetup:
    def __init__(self, brakes, engine, suspension, front_wing, rear_wing, gearbox):
        self.brakes = brakes
        self.engine = engine
        self.suspension = suspension
        self.front_wing = front_wing
        self.rear_wing = rear_wing
        self.gearbox = gearbox

    def calculate_contributions(self):
        contributions = {
            "speed": 0,
            "cornering": 0,
            "power_unit": 0,
            "reliability": 0,
            "avg_pit_stop_time": 0
        }

        # Define as contribuições para cada opção de cada parâmetro
        engine_contributions = {
            "Cloudroar": (26, 24, 50, 27, 0.55),
            "Avalanche": (34, 22, 25, 21, 0.35),
            "The Rover": (27, 25, 28, 24, 0.53),
            "Twinburst": (16, 29, 18, 17, 0.51),
            "Enigma": (16, 13, 23, 25, 0.69),
            "Nova": (31, 13, 15, 16, 0.71),
            "Brute Force": (21, 19, 36, 18, 0.63),
            "Starter": (1, 1, 1, 1, 1)
        }
        contributions["speed"] += engine_contributions[self.engine][0]
        contributions["cornering"] += engine_contributions[self.engine][1]
        contributions["power_unit"] += engine_contributions[self.engine][2]
        contributions["reliability"] += engine_contributions[self.engine][3]
        contributions["avg_pit_stop_time"] += engine_contributions[self.engine][4]

        brakes_contributions = {
            "Wildcore": (36, 23, 33, 22, 0.59),
            "Suspense": (20, 32, 23, 21, 0.37),
            "The Warden": (26, 28, 27, 25, 0.43),
            "Onyx": (26, 23, 25, 50, 0.49),
            "Axiom": (14, 34, 18, 15, 0.67),
            "Crisis SL": (27, 16, 18, 19, 0.51),
            "Essence": (14, 13, 12, 25, 0.76),
            "Starter": (1, 1, 1, 1, 1)
        }
        contributions["speed"] += brakes_contributions[self.brakes][0]
        contributions["cornering"] += brakes_contributions[self.brakes][1]
        contributions["power_unit"] += brakes_contributions[self.brakes][2]
        contributions["reliability"] += brakes_contributions[self.brakes][3]
        contributions["avg_pit_stop_time"] += brakes_contributions[self.brakes][4]

        suspension_contributions = {
            "Sigma": (32, 28, 30, 29, 0.39),
            "Presence": (23, 26, 24, 22, 0.2),
            "Horizon": (22, 36, 24, 37, 0.53),
            "Radiance": (25, 17, 26, 19, 0.65),
            "Icon V3": (17, 13, 16, 23, 0.54),
            "Rodeo": (23, 22, 15, 14, 0.69),
            "The Equator": (20, 19, 18, 21, 0.61),
            "Starter": (1, 1, 1, 1, 1)
        }
        contributions["speed"] += suspension_contributions[self.suspension][0]
        contributions["cornering"] += suspension_contributions[self.suspension][1]
        contributions["power_unit"] += suspension_contributions[self.suspension][2]
        contributions["reliability"] += suspension_contributions[self.suspension][3]
        contributions["avg_pit_stop_time"] += suspension_contributions[self.suspension][4]
        
        front_wing_contributions = {
            "Virtue": (23, 50, 27, 24, 0.49),
            "Thunderclap": (35, 23, 21, 33, 0.55),
            "Trailblazer": (21, 23, 42, 20, 0.57),
            "Zeno": (25, 23, 22, 26, 0.53),
            "The Vagabond": (31, 20, 23, 21, 0.35),
            "Feral Punch": (13, 15, 22, 21, 0.73),
            "The Scout": (13, 27, 15, 14, 0.73),
            "Starter": (1, 1, 1, 1, 1)
        }
        contributions["speed"] += front_wing_contributions[self.front_wing][0]
        contributions["cornering"] += front_wing_contributions[self.front_wing][1]
        contributions["power_unit"] += front_wing_contributions[self.front_wing][2]
        contributions["reliability"] += front_wing_contributions[self.front_wing][3]
        contributions["avg_pit_stop_time"] += front_wing_contributions[self.front_wing][4]

        rear_wing_contributions = {
            "Typhoon": (50, 27, 26, 23, 0.53),
            "Transcendence": (24, 22, 36, 37, 0.53),
            "Freeflare": (21, 33, 20, 22, 0.37),
            "The Patron": (23, 21, 19, 37, 0.61),
            "The Wasp": (16, 24, 23, 14, 0.69),
            "The Matador": (19, 16, 18, 17, 0.72),
            "Phantom-X": (26, 15, 12, 11, 0.76),
            "Starter": (1, 1, 1, 1, 1)
        }
        contributions["speed"] += rear_wing_contributions[self.rear_wing][0]
        contributions["cornering"] += rear_wing_contributions[self.rear_wing][1]
        contributions["power_unit"] += rear_wing_contributions[self.rear_wing][2]
        contributions["reliability"] += rear_wing_contributions[self.rear_wing][3]
        contributions["avg_pit_stop_time"] += rear_wing_contributions[self.rear_wing][4]

        gearbox_contributions = {
            "Voyage": (23, 28, 22, 27, 0),
            "Vector": (24, 38, 22, 36, 0.55),
            "Kick Shift": (18, 19, 29, 19, 0.45),
            "Verdict": (33, 18, 20, 30, 0.63),
            "Spectrum": (20, 25, 21, 23, 0.53),
            "Swiftcharge": (14, 23, 22, 16, 0.71),
            "Switch-R-OO": (12, 13, 11, 14, 0.47),
            "Starter": (1, 1, 1, 1, 1)
        }
        contributions["speed"] += gearbox_contributions[self.gearbox][0]
        contributions["cornering"] += gearbox_contributions[self.gearbox][1]
        contributions["power_unit"] += gearbox_contributions[self.gearbox][2]
        contributions["reliability"] += gearbox_contributions[self.gearbox][3]
        contributions["avg_pit_stop_time"] += gearbox_contributions[self.gearbox][4]

        return contributions

    # Lista de todas as opções para cada característica
    brakes_options = ["Wildcore", "Suspense", "The Warden", "Onyx", "Axiom", "Crisis SL", "Essence", "Starter"]
    engine_options = ["Cloudroar", "Avalanche", "The Rover", "Twinburst", "Enigma", "Nova", "Brute Force", "Starter"]
    suspension_options = ["Sigma", "Presence", "Horizon", "Radiance", "Icon V3", "Rodeo", "The Equator", "Starter"]
    front_wing_options = ["Virtue", "Thunderclap", "Trailblazer", "Zeno", "The Vagabond", "Feral Punch", "The Scout", "Starter"]
    rear_wing_options = ["Typhoon", "Transcendence", "Freeflare", "The Patron", "The Wasp", "The Matador", "Phantom-X", "Starter"]
    gearbox_options = ["Voyage", "Vector", "Kick Shift", "Verdict", "Spectrum", "Swiftcharge", "Switch-R-OO", "Starter"]



