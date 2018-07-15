import tkinter as tk
import AddOrEditUserWindow as aw

LARGE_FONT = ("Arial Black", 12)


class MainWindow(tk.Frame):
    users = {"John Doe": "John Doe", "Jane Smith": "Jane Smith", "Someother Guy": "Someother Guy"}
    user_list = None

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.controller = controller
        self.draw()

    def draw(self):
        # title
        label = tk.Label(self, text="Can't See This", font=LARGE_FONT)
        label.grid(row=0, columnspan=4)

        # user list
        scrollbar = tk.Scrollbar(self, orient="vertical")


        self.user_list = tk.Listbox(self, height=10, width=36, yscrollcommand=scrollbar.set, selectmode=tk.SINGLE)
        self._fill_user_list()
        self.user_list.grid(row=1, padx=(1, 0), columnspan=3)

        scrollbar.config(command=self.user_list.yview)
        scrollbar.grid(row=1, column=3, padx=(0, 10), sticky=tk.N + tk.S)

        # buttons
        add_user_button = tk.Button(self, text="Add User", command=lambda:self.controller.show_frame(aw.AddOrEditUserWindow))
        add_user_button.grid(row=2, column=0, padx=(10, 1), pady=10)

        remove_user_button = tk.Button(self, text="Remove User", command=self.remove_user)
        remove_user_button.grid(row=2, column=1, padx=1, pady=10)

        edit_user_button = tk.Button(self, text="Edit User", command=self.edit_user)
        edit_user_button.grid(row=2, column=2, padx=1, pady=10)

        enable_button = tk.Button(self, text="Enable Protection", command=self.enable_protection)
        enable_button.grid(row=3, column=1, padx=1, pady=10)

    def add_user(self):
        print("Add user pushed")

    def remove_user(self):
        print("Remove user button pushed")
        self.user_list.delete(self.user_list.curselection())

    def edit_user(self):
        print("Edit user button pushed")
        print("Trying to edit", self.user_list.get(self.user_list.curselection()))

    def enable_protection(self):
        print("Enable protection button pushed")

    def _fill_user_list(self):
        for user in self.users.keys():
            self.user_list.insert(0, user)
