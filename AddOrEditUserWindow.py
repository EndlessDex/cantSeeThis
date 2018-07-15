import tkinter as tk
import MainWindow as mw
from database.PeopleDatabase import PeopleDatabase
import recognize_faces


class AddOrEditUserWindow(tk.Frame):
    def __init__(self, parent, controller, pdb):
        tk.Frame.__init__(self, parent)
        print("init function")
        self.controller = controller
        self.pdb = pdb
        self.firstName = tk.StringVar()
        self.lastName = tk.StringVar()
        self.employeeId = tk.StringVar()
        self.clearanceVar = tk.StringVar()
        self.newUser = False
        self.createTextFields()
        self.create_widgets()
        self.create_back_button()
        self.create_save_button()

    def trainButton(self):
        print("Train button was pushed")
        recognize_faces.capture_faces(self.employeeId.get())

    def createTextFields(self):
        first_name_label = tk.Label(self, text="First Name")
        first_name_label.grid(row=0, column=0)
        first_name_entry = tk.Entry(self, width=25)
        first_name_entry["textvariable"] = self.firstName
        first_name_entry.grid(row=0, column=1, columnspan=2, padx=1, pady=1)

        last_name_label = tk.Label(self, text="Last Name")
        last_name_label.grid(row=1, column=0)
        lastNameEntry = tk.Entry(self, width=25)
        lastNameEntry["textvariable"] = self.lastName
        lastNameEntry.grid(row=1, column=1, columnspan=2)

        emplyeeIdLabel = tk.Label(self, text="Employee ID")
        emplyeeIdLabel.grid(row=2, column=0)
        employeeIdEntry = tk.Entry(self, width=15)
        employeeIdEntry["textvariable"] = self.employeeId
        employeeIdEntry.grid(row=2, column=1, columnspan=2)

        clearanceLabel = tk.Label(self, text="Clearance Level")
        clearanceLabel.grid(row=3, column=0)
        clearanceLevels = {'Secret', 'Top-secret', 'None'}
        self.clearanceVar.set('None')
        clearanceMenu = tk.OptionMenu(self, self.clearanceVar, *clearanceLevels)
        clearanceMenu.grid(row=3, column=1)

    def create_widgets(self):
        train_the_algorithm = tk.Button(self, text="Train the Algorithm", command=self.trainButton)
        train_the_algorithm.grid(row=4, column=1)

    def create_back_button(self):
        back_button = tk.Button(self, text="Back", command=self.controller.show_mainWindow)
        back_button.grid(row=4, column=0)

    def create_save_button(self):
        save_button = tk.Button(self, text="Save", command=self.save_user)
        save_button.grid(row=4, column=2)

    def go_back_to_main_window(self):
        mw.MainWindow.refresh_user_list()
        self.controller.show_frame(mw.MainWindow)

    def save_user(self):
        print(self.firstName.get())
        print(self.lastName.get())
        print(self.clearanceVar.get())
        name = self.firstName.get() + " " + self.lastName.get()
        facedata = 0
        if not self.newUser:
            print("User is being removed")
            print(self.pdb.remove_person(self.employeeId.get()))
        print(self.pdb.add_person(int(self.employeeId.get()), name, facedata, self.clearanceVar.get()))

    def load_user(self, employeeId):
        print("User " + str(employeeId) + " is being loaded")
        all_users = self.pdb.get_people()
        user_to_be_loaded = ()
        for pair in all_users:
            if pair[1] == employeeId:
                user_to_be_loaded = pair
        if user_to_be_loaded:
            name = user_to_be_loaded[0].split()
            self.firstName.set(name[0])
            self.lastName.set(name[-1])
            self.employeeId.set(user_to_be_loaded[1])
            clearanceVar = self.find_clearance(employeeId)
            self.clearanceVar.set(clearanceVar)

    def find_clearance(self, employeeId):
        clearanceVar = ""
        permissions = self.pdb.get_person_permissions(employeeId)

        if "Top-secret" in permissions:
            clearanceVar = "Top-secret"
        elif "Secret" in permissions:
            clearanceVar = "Secret"
        else:
            clearanceVar = "None"

        return clearanceVar


def refresh_window(self):
    self.firstName = tk.StringVar()
    self.lastName = tk.stringVar()
    self.employeeId = tk.stringVar()
    self.clearanceVar.set("None")
    self.newUser = True
