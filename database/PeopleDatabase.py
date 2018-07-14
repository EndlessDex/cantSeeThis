import pandas as pd

# Lazy constants:
clearanceIdx = "clearance"
namesIdx = "people"

# Example usage:
# from database.PeopleDatabase import PeopleDatabase
# pdb = peopleDatabase("database/test.xlsx");


class PeopleDatabase:
    """A simple wrapper for interacting with the people database."""

    def __init__(self, db_name):

        # TODO enforce this is valid string, valid DB.
        self.db_name = db_name
        self.clearance_db = pd.read_excel(db_name, sheet_name=clearanceIdx)

    def get_permissions(self):
        return self.clearance_db.keys().tolist()

    def has_permission(self, num, permission):
        # Check that the permission exists.
        if self.clearance_db[self.clearance_db.str.contains(permission)].empty:
            return False

        # Uses pandas boolean indexing.
        person_has_permission = self.clearance_db[permission] == num
        return not self.clearance_db[person_has_permission].empty

    def add_person(self, num, facedata, permissions=()):
        """
        Adds a new person with names of permission belonging to.
        :param  num: ID Number
        :param facedata: data used to recognize person.
        :param permissions: List of permission categories to add to.
        :return: True if successful. No changes are written if failed.
        """
        self._sync()
        pass

    def add_permission(self, permission, people=()):
        """
        Adds a new permission category with names of people to add.
        :param permission: Name of permission.
        :param people: List of people to add.
        :return: True if successful. No changes written on failure.
        """
        self._sync()
        pass

    def _sync(self):
        """
        Writes any changes back to file on disk.
        :return: True on success. Hopefully no changes written on failure.
        """
        pass
