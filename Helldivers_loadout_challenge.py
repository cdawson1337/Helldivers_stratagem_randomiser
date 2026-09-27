#When program is ran, start with printing the first stratagem and on the next line ask input for "Do You have this strategem?" if
#not then just reroll the one instead of all them printed at once. 
#Potential upgrades for later include adding a gui that also includes the icon for the stratagem. and building a macro key to use in game.


import random

STRATAGEMS = ["Orbital Precision Strike", "Orbital Gatling Barrage", "Orbital Gas Strike", "Orbital 120MM HE Barrage", "Orbital Airburst Strike",
"Orbital Smoke Strike", "Orbital EMS Strike", "Orbital 380MM HE Barrage", "Orbital Walking Barrage", "Orbital Laser", "Orbital Napalm Barrage",
"Orbital Railcannon Strike", "Eagle Gas Airstrike", "Eagle Strafing Run", "Eagle Airstrike", "Eagle Cluster Bomb", "Eagle Smoke Strike", "Eagle Napalm Airstrike",
"Eagle 110MM Rocket Pods", "Eagle 500KG Bomb", "MG-43 Machine Gun", "EAT-17 Expendable Anti-Tank", "M-105 Stalwart", "LAS-98 Laser Cannon", "APW-1 Anti-Material Rifle", "GR-8 Recoilless Rifle",
"GL-21 Grenade Launcher", "FLAM-40 Flamethrower", "MG-206 Heavy Machine Gun", "AC-8 Autocannon", "LAS-99 Quasar Cannon", "RL-77 Airburst Rocket Launcher", "MLS-4X Commando", 
"FAF-14 Spear", "RS-422 Railgun", "StA-X3 W.A.S.P Launcher", "CQC-20 Breaching Hammer", "PLAS-45 Epoch", "MGX-42 Bullet Storm", "S-11 Speargun", "CQC-9 Defoliation Tool", "GL-52 De-Escalator",
"EAT-700 Expendable Napalm", "TX-41 Sterilizer", "EAT-411 Leveller", "GL-28 Belt-fed Grendade Launcher", "B/MD C4 Pack", "MS-11 Solo Silo", "B/FLAM-80 Cremator", "M-1000 Maxigun", "CQC-1 One True Flag",
"40-K Meltagun", "B-1 Supply Pack", "LIFT-850 Jump Pack", "SH-20 Ballistic Shield Backpack", "AX/AR-23 Guard Dog", "AX/LAS-5 Rover", "SH-32 Shield Generator Pack", "SH-51 Directional Shield",
"AX/FLAM-75 Hot Dog", "B-100 Portable Hellbomb", "AX/ARC-3 K-9", "LIFT-860 Hover Pack", "AX/TX-13 Dog Breath", "LIFT-182 Warp Pack", "M-103 Supply FRV", "TD-110 Maelstrom", "M-104 Incenerator FRV",
"EXO-49 Emancipator Exosuit", "EXO-45 Patriot Exosuit", "M-102 Gunner FRV", "TD-220 Bastion MK XVI", "EXO-55 Breakthrough Exosuit", "EXO-51 Lumberer Exosuit", "A/MG-43 Machine Gun Sentry",
"A/G-16 Gatling Sentry", "A/AC-8 Autocannon Sentry", "A/M-12 Mortar Sentry", "A/MLS-4X Rocket Sentry", "A/ARC-3 Tesla Tower", "A/M-23 EMS Mortar Sentry", "A/LAS-98 Laser Sentry", "A/FLAM-40 Flame Sentry",
"A/GM-17 Gas Mortar Sentry", "MD-6 Anti-Personnel Minefield", "MD-14 Incendiary Mines", "MD-17 Anti-Tank Mines", "FX-12 Shield Generator Relay", "E/MG-101 HMG Emplacement", "E/GL-21 Grenadier Battlement",
"MD-8 Gas Mines", "E/AT-12 Anti-Tank Emplacement"]



def stratagem_randomization(STRATAGEMS: list) -> list:
    random_strats = []
    for strat in range(4):
        while True:
            random_strat = random.choice(STRATAGEMS)
            if random_strat in random_strats:
                continue
            choice = input(f"Do you have {random_strat} unlocked? ")
            if choice.lower() == "yes":
                print("Choosing next stratagem...")
                random_strats.append(random_strat)
                break
            if choice.lower() == "no":
                continue 
            else:
                print("Please answer yes or no.")
    return print(f"Your stratagems are:{random_strats}")


stratagem_randomization(STRATAGEMS)



