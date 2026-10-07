#When program is ran, start with printing the first stratagem and on the next line ask input for "Do You have this strategem?" if
#not then just reroll the one instead of all them printed at once. 
#Potential upgrades for later include adding a gui that also includes the icon for the stratagem. and building a macro key to use in game.


import random

STRATAGEMS = ["Orbital Precision Strike", "Orbital Gatling Barrage", "Orbital Gas Strike", "Orbital 120MM HE Barrage", "Orbital Airburst Strike",
"Orbital Smoke Strike", "Orbital EMS Strike", "Orbital 380MM HE Barrage", "Orbital Walking Barrage", "Orbital Laser", "Orbital Napalm Barrage",
"Orbital Railcannon Strike", "Eagle Gas Airstrike", "Eagle Strafing Run", "Eagle Airstrike", "Eagle Cluster Bomb", "Eagle Smoke Strike", "Eagle Napalm Airstrike",
"Eagle 110MM Rocket Pods", "Eagle 500KG Bomb", "MG-43 Machine Gun", "EAT-17 Expendable Anti-Tank", "M-105 Stalwart", "LAS-98 Laser Cannon", "APW-1 Anti-Material Rifle", "GR-8 Recoilless Rifle",
"GL-21 Grenade Launcher", "FLAM-40 Flamethrower", "MG-206 Heavy Machine Gun", "AC-8 Autocannon", "LAS-99 Quasar Cannon", "RL-77 Airburst Rocket Launcher", "MLS-4X Commando", 
"FAF-14 Spear", "RS-422 Railgun", "StA-X3 W.A.S.P Launcher", "B-1 Supply Pack", "LIFT-850 Jump Pack", "SH-20 Ballistic Shield Backpack", "AX/AR-23 Guard Dog", "AX/LAS-5 Rover", "SH-32 Shield Generator Pack",
"EXO-49 Emancipator Exosuit", "EXO-45 Patriot Exosuit", "M-102 Gunner FRV", "TD-220 Bastion MK XVI", "A/MG-43 Machine Gun Sentry",
"A/G-16 Gatling Sentry", "A/AC-8 Autocannon Sentry", "A/M-12 Mortar Sentry", "A/MLS-4X Rocket Sentry", "A/ARC-3 Tesla Tower", "A/M-23 EMS Mortar Sentry", 
"MD-6 Anti-Personnel Minefield", "MD-14 Incendiary Mines", "MD-17 Anti-Tank Mines", "FX-12 Shield Generator Relay", "E/MG-101 HMG Emplacement", "E/GL-21 Grenadier Battlement",
"MD-8 Gas Mines"]

WARBONDS = {
    "Chemical Agents": ["TX-41 Sterilizer", "AX/TX-13 Dog Breath"],
    "Urban Legends": ["SH-51 Directional Shield", "A/FLAM-40 Flame Sentry", "E/AT-12 Anti-Tank Emplacement"],
    "Servants of Freedom": ["B-100 Portable Hellbomb"],
    "Borderline Justice": ["LIFT-860 Hover Pack"],
    "Masters of Ceremony": ["CQC-1 One True Flag"],
    "Force of Law": ["GL-52 De-Escalator", "AX/ARC-3 K-9"],
    "Control Group": ["PLAS-45 Epoch", "A/LAS-98 Laser Sentry", "LIFT-182 Warp Pack"],
    "Dust Devils": ["S-11 Speargun", "EAT-700 Expendable Napalm", "MS-11 Solo Silo"],
    "Python Commandos": ["AX/FLAM-75 Hot Dog", "CQC-9 Defoliation Tool", "M-1000 Maxigun"],
    "Redacted Regiment": ["B/MD C4 Pack"], 
    "Siege Breakers": ["CQC-20 Breaching Hammer", "EAT-411 Leveller", "GL-28 Belt-Fed Grenade Launcher"],
    "Entrenched Division": ["A/GM-17 Gas Mortar Sentry", "B/FLAM-80 Cremator"], 
    "EXO Experts": ["MGX-42 Bullet Storm", "EXO-51 Lumberer Exosuit", "EXO-55 Breakthrough Exosuit"], 
    "Castellan's Creed": ["40-K Meltagun"]
}



def main():
    randomize = stratagem_randomization()
    print(f"""=============================
    Your challenge loadout is: {randomize}
    Now go spread Democracy!""")


def list_creation():
    list_numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14,]
    input_list = []
    final_input = []
    print("""=============================
    Select the Warbonds you own:
    =============================
    1. Chemical Agents
    2. Urban Legends
    3. Servants of Freedom
    4. Borderline Justice
    5. Masters of Ceremony
    6. Force of Law
    7. Control Group
    8. Dust Devils
    9. Python Commandos
    10. Redacted Regiment
    11. Siege Breakers
    12. Entrenched Division
    13. EXO Experts
    14. Castellan's Creed
    =============================""")
    for num in range(len(input_list)):
        input_list = input("select by choosing *number* followed by a comma or '0' for all Warbonds: "). split()
        if input_list[num] not in list_numbers:
            raise Exception("Please input only numbers 0-14")
        if input_list[num] != 0 and input_list[num] in list_numbers:
            final_input.append(input_list[num])
        if input_list[num] == 0 and len(input_list) == 1:
            final_input.append(input_list[num])
        if input_list[num] == 0 and len(input_list) > 1:
            raise Exception("Please print either 0 or 1-14 seperated by commas")
    return final_input
                
def combine_lists():
    inputs = list_creation()
    num_to_strat = []
    if 0 in inputs and len(inputs) == 1:
        num_to_strat = list(WARBONDS.values())
    else:
        for number in range(len(inputs)):
            num_to_strat.append(WARBONDS[number+1])
    strat_list = STRATAGEMS.extend(num_to_strat)
    return strat_list

def stratagem_randomization():
    final_list = combine_lists()
    return_list = []
    for strat in range(4):
        while True:
            random_strat = random.choice(final_list)
            if random_strat in return_list:
                continue
            else:
                return_list.append(random_strat)
                break
    return return_list



if __name__=="__main__":
    main()