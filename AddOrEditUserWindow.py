import tkinter as tk 
import MainWindow as mw
from database.PeopleDatabase import PeopleDatabase


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
		self.createTextFields()	
		self.create_widgets()
		self.create_back_button()
		self.create_save_button()

	
	def trainButton(self): 
		print("Train button was pushed")
		print(self.firstName.get())
		print(self.lastName.get())

	def createTextFields(self):
		firstNameLabel = tk.Label(self, text="First Name")
		firstNameLabel.grid(row=0, column=0)
		firstNameEntry = tk.Entry(self, width=25)
		firstNameEntry["textvariable"] = self.firstName
		firstNameEntry.grid(row=0, column=1, columnspan=2, padx=1, pady=1)


		lastNameLabel = tk.Label(self, text="Last Name")
		lastNameLabel.grid(row=1, column=0)
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
		clearanceMenu.grid(row = 3, column = 1)

	def create_widgets(self): 
		train_the_algorithm = tk.Button(self, text="Train the Algorithm", command=self.trainButton)
		train_the_algorithm.grid(row=4, column=1)

	def create_back_button(self):
		back_button = tk.Button(self, text="Back", command=lambda:self.controller.show_frame(mw.MainWindow))
		back_button.grid(row=4, column=0)

	def create_save_button(self): 
		save_button = tk.Button(self, text="Save", command=self.save_user)
		save_button.grid(row=4, column=2)

	def save_user(self): 
		print(self.firstName.get())
		print(self.lastName.get())
		print(self.clearanceVar.get())
		name = self.firstName.get() + " " + self.lastName.get()
		facedata = 0
		print(self.pdb.add_person(int(self.employeeId.get()), name, facedata, self.clearanceVar.get()))






