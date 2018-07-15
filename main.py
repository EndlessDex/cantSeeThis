import tkinter as tk
import MainWindow as mw


class CantSeeThisApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.geometry("230x350")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

#        for F in (MainWindow):
#            frame = F(container, self)
#            self.frames[F] = frame
#            frame.grid(row=0, column=0, sticky="nsew")

        frame = mw.MainWindow(container, self)
        self.frames[mw.MainWindow] = frame
        frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(mw.MainWindow)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()


app = CantSeeThisApp()
app.mainloop()