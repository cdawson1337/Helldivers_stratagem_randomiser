import customtkinter as ctk
import random

app = ctk.CTk()

# container name -> list of values it contributes
containers = {
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

check_vars = []

for name in containers:
    var = ctk.StringVar(value="")
    cb = ctk.CTkCheckBox(
        app,
        text=name,
        variable=var,
        onvalue=name,    # container name when checked
        offvalue=""
    )
    cb.pack(anchor="w", padx=20, pady=5)
    check_vars.append(var)

def get_checked():
    pool = []
    for var in check_vars:
        name = var.get()
        if name != "":
            pool.extend(containers[name])   # add every value in the container
    return pool

def randomize():
    pool = get_checked()
    picks = random.sample(pool, min(4, len(pool)))  # avoids an error if pool < 4
    print(picks)

button = ctk.CTkButton(app, text="Randomize", command=randomize)
button.pack(pady=20)

app.mainloop()