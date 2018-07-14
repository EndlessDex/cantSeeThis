import tkinter as tk


class CantSeeThisApp(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        button = tk.Button(self, text="OK", command=self.callback)
        button.pack()

    def callback(self):
        print("Button clicked")


root = tk.Tk();
app = CantSeeThisApp(master=root)
app.mainloop()