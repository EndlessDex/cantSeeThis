class MainWindow:
    def __init__(self):

    def create_widgets(self):
        user_list = tk.Listbox(self, height=10)
        user_list.pack()

        add_user_button = tk.Button(self, text="Add User", command=self.add_user)
        add_user_button.pack()

        remove_user_button = tk.Button(self, text="Remove User", command=self.remove_user)
        remove_user_button.pack()

        edit_user_button = tk.Button(self, text="Edit User", command=self.edit_user)
        edit_user_button.pack()

    def add_user(self):
        print("Add user pushed")

    def remove_user(self):
        print("Remove user button pushed")

    def edit_user(self):
        print("Edit user button pushed")