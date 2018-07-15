import tkinter as tk
# import MainWindow
import AddOrEditUserWindow

class CantSeeThisApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand = True)

        container.grid_rowconfigure(1, weight=1)
        container.grid_columnconfigure(1, weight=1)

        self.frames = {}

#        for F in (MainWindow):
#            frame = F(container, self)
#            self.frames[F] = frame
#            frame.grid(row=0, column=0, sticky="nsew")

        frame = AddOrEditUserWindow.AddOrEditUserWindow(container, self)
        self.frames[AddOrEditUserWindow] = frame
        frame.grid(row=0, column=0)
        self.show_frame(AddOrEditUserWindow)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()


app = CantSeeThisApp()
# app.geometry("500x500")
app.mainloop()