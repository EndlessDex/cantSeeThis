import tkinter as tk 

class AddOrEditUserWindow(tk.Frame): 

	def __init__(self, parent, controller):	
		tk.Frame.__init__(self, parent)
		self.firstName = tk.StringVar() 
		self.lastName = tk.StringVar()
		self.classificationEntry = tk.StringVar()
		self.createTextFields()	
		self.create_widgets()

	def create_widgets(self): 
		train_the_algorithm = tk.Button(self, text="Train the Algorithm", command=self.trainButton)
		train_the_algorithm.pack(side='bottom')

	def trainButton(self): 
		print("Train button was pushed")
		print(self.firstName.get())
		print(self.lastName.get())

	def createTextFields(self):
		firstNameLabel = tk.Label(self, text="First Name")
		firstNameLabel.grid(row=0, column=0)

		firstNameLabel.pack(side='left')
		# firstNameLabel.grid(row=1, column=2)

		firstNameEntry = tk.Entry(self, width=25)
		firstNameEntry["textvariable"] = self.firstName
		firstNameEntry.pack(side="left")


		lastNameLabel = tk.Label(self, text="Last Name")
		lastNameLabel.pack(side='left')

		lastNameEntry = tk.Entry(self, width=25)
		lastNameEntry["textvariable"] = self.lastName
		lastNameEntry.pack(side='left')


		classificationLabel = tk.Label(self, text="Classification Level")
		classificationLabel.pack(side='left')
		classificationLevels = {'Level 1', 'Level 2', 'Level 3', 'Level 4'}
		classificationVar = tk.StringVar()
		classificationVar.set('Level 1')
		classificationMenu = tk.OptionMenu(self, classificationVar, *classificationLevels)
		classificationMenu.pack(side='left')
	