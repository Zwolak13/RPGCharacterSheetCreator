import random
import tkinter as tk
from random import Random
from tkinter import ttk
from Save_To_File import save_character_to_file

class CharacterCreator(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Kreator Postaci RPG")
        self.geometry("700x300")
        self.resizable(False, False)

        # Ustawienie gridu
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        self.name_label = tk.Label(self, text="Imię postaci:")
        self.name_label.grid(row=0, column=0, sticky="w", padx=10, pady=5)

        self.name_input = tk.Entry(self)
        self.name_input.grid(row=1, column=0, padx=10, pady=5)

        self.race_label = tk.Label(self, text="Rasa:")
        self.race_label.grid(row=2, column=0, sticky="w", padx=10, pady=5)

        self.race_dropdown = ttk.Combobox(self, values=["Człowiek", "Elf", "Krasnolud", "Halfling", "Gnom", "Tiefling", "Dragonborn", "Ork"])
        self.race_dropdown.grid(row=3, column=0, padx=10, pady=5)
        self.race_dropdown.bind("<<ComboboxSelected>>", self.update_race_bonus)

        self.race_bonus_label = tk.Label(self, text="Bonusy rasy: Wybierz rasę, aby zobaczyć bonusy.")
        self.race_bonus_label.grid(row=4, column=0, padx=10, pady=5)

        self.class_label = tk.Label(self, text="Klasa:")
        self.class_label.grid(row=5, column=0, sticky="w", padx=10, pady=5)

        self.class_dropdown = ttk.Combobox(self, values=["Barbarzyńca", "Bard", "Kleryk", "Druid", "Wojownik", "Mnich", "Paladyn", "Łowca", "Łotrzyk", "Czarodziej", "Zaklinacz", "Mag"])
        self.class_dropdown.grid(row=6, column=0, padx=10, pady=5)

        self.submit_button = tk.Button(self, text="Zapisz postać", command=self.save_character)
        self.submit_button.grid(row=7, column=0, padx=10, pady=5)

        stats_label = tk.Label(self, text="Statystyki:")
        stats_label.grid(row=0, column=1, padx=10, pady=5)

        self.stats = {}
        row = 1
        for stat in ["Siła", "Zręczność", "Kondycja", "Inteligencja", "Mądrość", "Charyzma"]:
            stat_label = tk.Label(self, text=stat + ":")
            stat_value_label = tk.Label(self, text='\t0')
            stat_label.grid(row=row, column=1, sticky="w", padx=10, pady=5)
            stat_value_label.grid(row=row, column=1, padx=10, pady=5)
            self.stats[stat] = stat_value_label
            row += 1

        self.randomize_button = tk.Button(self, text="Losuj statystyki", command=self.randomize_stats)
        self.randomize_button.grid(row=row, column=1, padx=10, pady=5)


    def randomize_stats(self):
        # Bonusy dla ras
        race_bonuses = {
            "Człowiek": [1, 1, 1, 1, 1, 1],
            "Elf": [0, 2, 0, 0, 1, 0],
            "Krasnolud": [2, 0, 1, 0, 0, 0],
            "Halfling": [0, 2, 0, 0, 0, 1],
            "Gnom": [0, 1, 0, 2, 0, 0],
            "Tiefling": [0, 0, 0, 1, 0, 2],
            "Dragonborn": [2, 0, 0, 0, 0, 1],
            "Ork": [2, 1, 0, 0, 0, 0],
        }

        # Pobieranie aktualnych bonusów rasy
        selected_race = self.race_dropdown.get()
        current_bonuses = race_bonuses.get(selected_race)
        print(f"Bonusy dla rasy {selected_race}: {current_bonuses}")

        for i, stat in enumerate(self.stats):
            stats_rolls = []
            for _ in range(4):
                stats_rolls.append(random.randint(1, 6))
            stats_rolls.sort(reverse=True)
            stat_value = sum(stats_rolls[:3]) + current_bonuses[i]
            if current_bonuses[i] != 0:
                print(f"Dodano +{current_bonuses[i]} do {stat} o bazie {sum(stats_rolls[:3])}")
            self.stats[stat].config(text=str(stat_value))


    def update_race_bonus(self, event=None):
        race_bonuses = {
            "Człowiek": "Brak bonusów.",
            "Elf": "Bonusy: Zręczność +2, Mądrość +1.",
            "Krasnolud": "Bonusy: Siła +2, Kondycja +1.",
            "Halfling": "Bonusy: Zręczność +2, Charyzma +1.",
            "Gnom": "Bonusy: Inteligencja +2, Zręczność +1.",
            "Tiefling": "Bonusy: Charyzma +2, Inteligencja +1.",
            "Dragonborn": "Bonusy: Siła +2, Charyzma +1.",
            "Ork": "Bonusy: Siła +2, Zręczność +1.",
        }

        # Zaktualizowanie etykiety bonusów
        selected_race = self.race_dropdown.get()
        self.race_bonus_label.config(text=f"Bonusy rasy: {race_bonuses.get(selected_race)}")
        self.randomize_stats()

    def class_equipment(self):
        equipment = {
            "Barbarzyńca":["Skórzana Zbroja","Brón Dwuęczna",],
            "Bard":["Lekka Zbroja", "Wybrany Instrument"],
            "Kleryk":["Lekka Zbroja","Buława i Tarcza"],
            "Druid":["Skórzana Zbroja", "Drewniany Kostur"],
            "Wojownik":["Zbroja Płytowa", "Tarcza i Krótki Miecz"],
            "Mnich":["Lekka Zbroja","Drewniany Kij"],
            "Paladyn":["Zbroja Płytowa", "Długi Miecz Dwuręczny"],
            "Łowca":["Skórzana Zbroja","Łuk i Stzylet"],
            "Łotrzyk":["Skórzana Zbroja","Dwa Sztylety"],
            "Czarodziej":["Lekka Zbroja", "Różdżka i Księga"],
            "Zaklinacz":["Lekka Zbroja", "Magiczna Księga"],
            "Mag":["Lekka Zbroja", "Magiczny Kostur"]
        }
        return equipment.get(self.class_dropdown.get())

    def characters_details(self):
        race_details = {
            "Człowiek": [20,100,150,190,9],
            "Elf": [30,750,160,200,9],
            "Krasnolud": [50,350,120,140,7.5],
            "Halfling": [20,150,90,120,5],
            "Gnom": [30,500,90,120,5],
            "Tiefling": [20,140,160,190,9],
            "Dragonborn": [15,80,170,210,9],
            "Ork": [12,50,160,220,9]
        }
        character_details = race_details.get(self.race_dropdown.get())
        age = random.randint(character_details[0],character_details[1])
        height = random.randint(character_details[2],character_details[3])
        speed = character_details[4]
        return [age,height,speed]

    def get_stats_values(self):
        stats_values = []

        for stat in self.stats:
            stat_value = self.stats[stat].cget("text")
            stats_values.append(int(stat_value))

        return stats_values

    def save_character(self):
        character_data = {
            "name": self.name_input.get(),
            "race": self.race_dropdown.get(),
            "class": self.class_dropdown.get(),
        }
        stats =  self.get_stats_values()
        equipment = self.class_equipment()
        character_details=self.characters_details()
        save_character_to_file(stats,character_data,character_details,equipment)


if __name__ == "__main__":
    app = CharacterCreator()
    app.mainloop()
