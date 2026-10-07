'''
import customtkinter

class CheckboxFrame(customtkinter.CTkScrollableFrame):
    def __init__(self, master, title, values):
        super().__init__(master)
        self.grid_columnconfigure(0, weight=1)
        self.values = values
        self.title = title
        self.checkboxes = []

        self.title = customtkinter.CTkLabel(self, text=self.title, fg_color="black", corner_radius= 6)
        self.title.grid(row=0, column=0, padx=10, pady=(10,0), sticky="ew")

        for i, value in enumerate(self.values):
            checkbox = customtkinter.CTkCheckBox(self, text=value)
            checkbox.grid(row=i+1, column =0, padx=10, pady=(10,0), sticky="w")
            self.checkboxes.append(checkbox)
            
        
    def get(self):
        checked_checkboxes = []
        for checkbox in self.checkboxes:
            if checkbox.get() == 1:
                checked_checkboxes.append(checkbox.cget("text"))
        return checked_checkboxes
'''

"""
check_vars = []

        for name in containers:
            var = ctk.StringVar(value = "")
            cb = ctk.CTkCheckBox(
                app,
                text=name,
                variable=var,
                onvalue=name,
                offvalue=""
            )
            cb.pack(anchor="w", padx=20, pady=5)
            check_vars.append(var)
    
    def get_checked():
        pool = []
        for var in check_vars:
            name = var.get()
            if name != "":
                pool.extend(containers[name])
        return pool
    
    def randomize():
        pool = get_checked()
        picks = random.sample(pool, 4)
        print(picks)

    def button():
        button = ctk.CTkButton(app, text="Randomize", command=randomize)
        button.pack(pady=20)
"""

