import csv
import random
import chatecter_creation

# Function to get the list of available characters from the CSV file
def get_character_list():
    characters = []
    with open("battle_simulator/characters.csv", "r", newline="") as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row
        for row in reader:
            characters.append(row[0].capitalize())  # Capitalize names
    return characters


# Function to select a character, avoiding those in the excluded list
def select_character(excluded=[]):
    characters = [char for char in get_character_list() if char not in excluded]
    prompt = "Select which character you would like to play as" if not excluded else "Selecting CPU's character..."
    print(prompt)
    for i, name in enumerate(characters):
        print(f"({i+1}) {name}")
    while True:
        try:
            selection = int(input("Please type the number corresponding to your selection: "))
            if 1 <= selection <= len(characters):
                return characters[selection - 1]
            else:
                print("Invalid selection. Please choose a valid number.")
        except ValueError:
            print("Please enter a whole number.")

# Function to calculate attack damage, considering dodge chance, defense, and critical hits
def attack_damage(attacker, attacker_stats, defender_stats):
    base_damage = random.randint(attacker_stats["attack_min"], attacker_stats["attack_max"])
    if random.randint(1, 100) <= defender_stats["dodge_chance"]:
        print(f"{attacker} attacks, but the opponent dodges!")
        return 0
    
    # Check for critical hit
    if random.randint(1, 100) <= attacker_stats["crit_chance"]:
        crit_damage = base_damage * 2
        print(f"{attacker} does {base_damage} damage, but gets a random crit doubling it to {crit_damage} damage!")
        base_damage = crit_damage
    
    damage_blocked = base_damage * (defender_stats["defense"] / 100)
    return max(1, int(base_damage - damage_blocked))

# Function to handle PvE battle sequence
def pve_battle():
    # Function to load character stats from the CSV file
    def load_character_stats(character_name):
        with open("battle_simulator/characters.csv", "r", newline="") as file:
            reader = csv.reader(file)
            next(reader)  # Skip header row
            for row in reader:
                if row[0].lower() == character_name.lower():
                    return {
                        "hp": 100,
                        "attack_min": int(int(row[4]) // 2),  # Convert strength to int before division
                        "attack_max": int(row[4]),      # Max attack is the full strength stat
                        "defense": int(row[5]),
                        "dodge_chance": int(row[3]),    # Dodge chance now based on speed
                        "crit_chance": int(row[6])      # Critical hit chance
                    }
        return None
    characters = get_character_list()
    if len(characters) < 2:
        print("Not enough characters available! Returning to the main menu...")
        return  # This will return to the main menu loop

    print("Player character selection:")
    player = select_character()
    player_stats = load_character_stats(player)

    print("CPU character is being selected...")
    cpu = select_character(excluded=[player])
    cpu_stats = load_character_stats(cpu)

    print(f"You selected {player}. The CPU will use {cpu}.")
    #checks if your turn is being skiped 
    skip_turn = False
    while player_stats["hp"] > 0 and cpu_stats["hp"] > 0:
        if not skip_turn:
            print(f"\n{player}'s Turn! Current HP: {player_stats['hp']}\n(1) Normal Attack\n(2) Power Attack (Deals more damage but skips next turn\n(3) Heal (+15 HP)")
            
            while True:
                choice = input("Choose an action: ")
                # a new way i foud of checking user input without using try 
                if choice in ["1", "2", "3"]:
                    break
                print("Invalid choice, please select again.")
            
            if choice == "1":
                damage = attack_damage(player, player_stats, cpu_stats)
                cpu_stats["hp"] -= damage
                print(f"{player} attacks {cpu} for {damage} damage!")
            elif choice == "2":
                damage = (player_stats["attack_max"] + 5)  # Stronger attack
                cpu_stats["hp"] -= damage
                print(f"{player} performs a power attack on {cpu} for {damage} damage but will skip the next turn!")
                skip_turn = True
            elif choice == "3":
                player_stats["hp"] = min(100, player_stats["hp"] + 15)
                print(f"{player} heals 15 HP!")
        else:
            print(f"{player} skips this turn due to the power attack!")
            skip_turn = False
        #checks if the cpu is dead, if it is the players charecter wins, and gains a level
        if cpu_stats["hp"] <= 0:
            print(f"{cpu} has been defeated! {player} wins!")
            chatecter_creation.level_up_character(player.lower())
            break

        print(f"\n{cpu}'s Turn! Current HP: {cpu_stats['hp']}")
        cpu_choice = random.choice(["1", "1", "2", "3"])  # radom choice maker for the cpu, it has 2 1's so the cpu is more likley to do a light attack
        if cpu_choice == "1":
            damage = attack_damage(cpu, cpu_stats, player_stats)
            player_stats["hp"] -= damage
            print(f"{cpu} attacks {player} for {damage} damage!")
        elif cpu_choice == "2":
            damage = (cpu_stats["attack_max"] + 5)  # Stronger attack
            player_stats["hp"] -= damage
            print(f"{cpu} performs a power attack on {player} for {damage} damage but will skip the next turn!")
            skip_turn = True
        elif cpu_choice == "3":
            cpu_stats["hp"] = min(100, cpu_stats["hp"] + 15)
            print(f"{cpu} heals 15 HP!")

        #checks if the player is dead, if the player is dead, then the cpu's charecter wins, and gains a level for winning.
        if player_stats["hp"] <= 0:
            print(f"{player} has been defeated! {cpu} wins!")
            chatecter_creation.level_up_character(cpu.lower()) 
            break

# Start a PvE battle
#pve_battle()
