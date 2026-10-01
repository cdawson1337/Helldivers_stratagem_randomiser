import customtkinter
import random
from checkbox_frame import CheckboxFrame

warbond1 = ["A", "B", "C"]
warbond2 = ["D", "E", "F"]
warbond3 = ["G", "H", "I"]


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Helldivers Loadout Challenge")
        self.geometry("1280x720")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure((0,1), weight=1)
        self.configure(fg_color="yellow")

        self.checkbox_frame = CheckboxFrame(self, "Warbonds", values=["Warbond1", "Warbond2", "Warbond3"])
        self.checkbox_frame.grid(row=0, column=0, padx=(0, 10), pady=(10, 0), sticky="nsew")
        self.checkbox_frame.configure(fg_color="black")

        self.button = customtkinter.CTkButton(self, fg_color="black", text="Grab Challenge Loadout", command=self.randomization_button)
        self.button.grid(row=3, column=0, padx=10, pady=10, sticky="ew", columnspan=2)

    def Add_lists(self):
        total_stratagems = []
        if Warbond1.get() == 1:
            total_stratagems.extend(warbond1)
        if Warbond2.get() == 1:
            total_stratagems.extend(warbond2)
        if Warbond3.get() == 1:
            total_stratagems.extend(warbond3)
        return total_stratagems

    def randomization_button(self):
        strat_list = 
        for strat in range(4):
            while True:
                random_strat = random.choice(total_stratagems)
                if random_strat not in random_strats:
                    random_strat.append(random_strats)
                    break
        return random_strats

    
if __name__=="__main__":
    app = App()
    app.mainloop()