import tkinter as tk
import AddOrEditUserWindow as aw
import MainWindow as mw
from database.PeopleDatabase import PeopleDatabase


class CantSeeThisApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        self.pdb = PeopleDatabase("database/test.xlsx");

        tk.Tk.__init__(self, *args, **kwargs)
        self.geometry("370x340")

        self.container = tk.Frame(self)
        self.container.pack(side="top", fill="both", expand=True)

        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        # for F in (mw.MainWindow, aw.AddOrEditUserWindow):
        #    frame = F(self.container, self)
        #    self.frames[F] = frame
        #    frame.grid(row=0, column=0, sticky="nsew")

        self.create_frame_dictionary()
        self.show_frame(mw.MainWindow)

    def create_frame_dictionary(self):
        frame = mw.MainWindow(self.container, self, self.pdb)
        frame.grid(row=0, column=0, sticky="nsew")
        self.frames[mw.MainWindow] = frame

        frame = aw.AddOrEditUserWindow(self.container, self, self.pdb)
        frame.grid(row=0, column=0, sticky="nsew")
        self.frames[aw.AddOrEditUserWindow] = frame

    def show_frame(self, cont):
        print(self.frames)
        frame = self.frames[cont]
        frame.tkraise()

    def show_mainWindow(self): 
        frame = self.frames[mw.MainWindow]
        frame.refresh_user_list()
        frame.tkraise()

    def show_add_or_edit_user_window(self, employeeId = 0): 
        frame = self.frames[aw.AddOrEditUserWindow]
        if employeeId: 
            frame.load_user(employeeId)
        else: 
            frame.refresh_window()
            #Add User
        frame.tkraise()

app = CantSeeThisApp()
app.mainloop()