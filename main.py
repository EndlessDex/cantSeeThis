import tkinter as tk
import AddOrEditUserWindow as aw
import MainWindow as mw


class CantSeeThisApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.geometry("270x340")

        self.container = tk.Frame(self)
        self.container.pack(side="top", fill="both", expand=True)

        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (mw.MainWindow, aw.AddOrEditUserWindow):
           frame = F(self.container, self)
           self.frames[F] = frame
           frame.grid(row=0, column=0, sticky="nsew")

        # self.create_frame_dictionary()
        self.show_frame(mw.MainWindow)

    def create_frame_dictionary(self):
        frame = mw.MainWindow(self.container, self)
        frame.grid(row=0, column=0, sticky="nsew")
        self.frames[mw.MainWindow] = frame

        frame = aw.AddOrEditUserWindow(tk.Frame(self), self)
        frame.grid(row=0, column=0, sticky="nsew")
        self.frames[aw.AddOrEditUserWindow] = frame

    def show_frame(self, cont):
        if cont == aw.AddOrEditUserWindow: 
            print('bleh')
            fb = tk.Frame()
        print(self.frames)
        frame = self.frames[cont]
        frame.tkraise()
# <<<<<<< HEAD
#         frame = aw.AddOrEditUserWindow(container, self)
#         self.frames[AddOrEditUserWindow] = frame
#         frame.grid(row=0, column=0)
#         self.show_frame(AddOrEditUserWindow)
# =======
#         frame = mw.MainWindow(container, self)
#         self.frames[mw.MainWindow] = frame
#         frame.grid(row=0, column=0, sticky="nsew")
#         self.show_frame(mw.MainWindow)
# >>>>>>> 74c45726fab391bfc2b6384126e435f6371fa8be

	


app = CantSeeThisApp()
app.mainloop()