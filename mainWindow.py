import tkinter as tk


LARGE_FONT = ("Arial Black", 12)


class MainWindow(tk.Frame):
    users = {"John Doe": "John Doe", "Jane Smith": "Jane Smith", "Someother Guy": "Someother Guy"}

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.draw()

    def draw(self):
        # title
        label = tk.Label(self, text="Can't See This", font=LARGE_FONT)
        label.place(x=45, y=10, in_=self)

        # user list
        scrollbar = tk.Scrollbar(self, orient="vertical")
        user_list = tk.Listbox(self, height=10, width=32, yscrollcommand=scrollbar.set)
        scrollbar.config(command=user_list.yview)
        self._fill_user_list(user_list)
        user_list.place(x=10, y=50, in_=self)
        scrollbar.place(x=205, y=50, in_=self)


        # buttons
        firstRow = 220
        secondRow = 250

        add_user_button = tk.Button(self, text="Add User", command=self.add_user)
        add_user_button.place(x=10, y=firstRow, in_=self)

        remove_user_button = tk.Button(self, text="Remove User", command=self.remove_user)
        remove_user_button.place(x=75, y=firstRow, in_=self)

        edit_user_button = tk.Button(self, text="Edit User", command=self.edit_user)
        edit_user_button.place(x=160, y=firstRow, in_=self)

        enable_button = tk.Button(self, text="Enable Protection", command=self.enable_protection)
        enable_button.place(x=60, y=secondRow, in_=self)

    def add_user(self):
        print("Add user pushed")

    def remove_user(self):
        print("Remove user button pushed")

    def edit_user(self):
        print("Edit user button pushed")

    def enable_protection(self):
        print("Enable protection button pushed")

    def _fill_user_list(self, user_list):
        for user in self.users.keys():
            user_list.insert(0, user)
