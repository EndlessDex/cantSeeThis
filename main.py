import tkinter as tk
import MainWindow

class CantSeeThisApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand = True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

#        for F in (MainWindow):
#            frame = F(container, self)
#            self.frames[F] = frame
#            frame.grid(row=0, column=0, sticky="nsew")

        frame = MainWindow(container, self)
        self.frames[MainWindow] = frame
        frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(MainWindow)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()


app = CantSeeThisApp()
app.mainloop()