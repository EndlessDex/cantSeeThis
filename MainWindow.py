import tkinter as tk
import AddOrEditUserWindow as aw
from database.PeopleDatabase import PeopleDatabase

LARGE_FONT = ("Arial Black", 12)


class MainWindow(tk.Frame):
    def __init__(self, parent, controller, pdb):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.controller = controller
        self.pdb = pdb
        self.users = {}
        self.draw()

    def draw(self):
        # title
        label = tk.Label(self, text="Can't See This", font=LARGE_FONT)
        label.grid(row=0, columnspan=4)

        # user list
        scrollbar = tk.Scrollbar(self, orient="vertical")

        self.user_list = tk.Listbox(self, height=10, width=36, yscrollcommand=scrollbar.set, selectmode=tk.SINGLE)
        self.refresh_user_list()
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

        protection_label = tk.Label(self, text="Protection Mode")
        protection_label.grid(row=4, column=0, padx=1, pady=1)
        protection_modes = {"None", "Top-secret", "Secret"}
        self.protection_mode = tk.StringVar()
        self.protection_mode.set("None")
        protection_mode_dropdown = tk.OptionMenu(self, self.protection_mode, *protection_modes)
        protection_mode_dropdown.grid(row=4, column=1)

    def remove_user(self):
        selected = self.user_list.curselection()
        self.pdb.remove_person(self.users[selected])
        del self.users[selected]
        self.user_list.delete(selected)

    def edit_user(self):
        print("Edit user button pushed")
        if self.user_list.curselection(): 
            print("Trying to edit", self.user_list.get(self.user_list.curselection()))
            print(self.users[self.user_list.get(self.user_list.curselection())])
            self.controller.show_add_or_edit_user_window(self.users[self.user_list.get(self.user_list.curselection())])


    def enable_protection(self):
        print("Enable protection button pushed")

    def refresh_user_list(self):
        self.user_list.delete(0, tk.END)
        self.users = {}
        self._fill_user_list()

    def _fill_user_list(self):
        for user in self.pdb.get_people():
            self.users[user[0]] = user[1]
            self.user_list.insert(0, user[0])
