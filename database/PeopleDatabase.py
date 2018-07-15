import pandas as pd
import numpy as np
from pandas import DataFrame as df
from pandas import Series

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
        self.people_db = pd.read_excel(db_name, sheet_name=namesIdx)

    def get_permissions(self):
        """
        :return: A List of the strings of permissions.
        """
        return self.clearance_db.keys().tolist()

    def get_people(self):
        """
        :return: A list of (name, id) tuple pairs.
        """
        names = self.people_db["names"].tolist()
        ids = self.people_db["numbers"].tolist()
        return list(zip(names, ids))

    def has_permission(self, num, permission):
        # Check that the permission exists.
        if permission not in self.clearance_db.columns:
            return False

        # Uses pandas boolean indexing.
        person_has_permission = self.clearance_db[permission] == num
        return not self.clearance_db[person_has_permission].empty

    def set_person_permission(self, person, permission, remove=False):
        """
        Sets permission for a person (ID). If remove is True it removes that permission for person.
        Person and permission must exist.
        :param person:
        :param permission:
        :param remove:
        :return: True on success.
        """
        if remove:
            return self.remove_person_permission(person, permission)

        # TODO check that person and permission exists.

        # Check if nan is in that permission and fill it in:
        if not self.clearance_db[permission].hasnans:
            # No Nans, so append a row to the DB
            self.clearance_db = self.clearance_db.append(Series([np.nan],
                                                                   index=[permission]),
                                                         ignore_index=True)

        # Now find the nan and replace with the
        nanidx = self.clearance_db[permission] \
            .index[pd.isnull(self.clearance_db[permission])][0]

        self.clearance_db.ix[nanidx, permission] = person

        self._sync()
        return

    def remove_person_permission(self, person, permission):
        # Check that permission exists:
        if permission not in self.clearance_db.columns:
            return False

        clearance_col = self.clearance_db[permission]
        if clearance_col[clearance_col == person].empty:
            # person does not exist.
            return False

        # Now find the person and replace with NaN.
        personidx = clearance_col.index[clearance_col == person][0]
        self.clearance_db.ix[personidx, permission] = np.nan

        self._sync()

    def add_person(self, num, facedata, permissions=()):
        """
        Adds a new person with names of permission belonging to.
        :param  num: ID Number
        :param facedata: data used to recognize person.
        :param permissions: List of permission categories to add to.
        :return: True if successful. No changes are written if failed.
        """
        # Verify that all permissions exist.

        # Verify that num does not already exist.

        # Iterate through each permission (TODO this is bad).
        # ALSO TODO remove code duplication.
        for permission in permissions:
            # Check if nan is in that permission and fill it in:
            if not self.clearance_db[permission].hasnans:
                # No Nans, so append a row to the DB
                self.clearance_db = self.clearance_db.append(Series([np.nan],
                                                                       index=[permission]),
                                                             ignore_index=True)

            # Now find the nan and replace with the
            nanidx = self.clearance_db[permission] \
                .index[pd.isnull(self.clearance_db[permission])][0]

            self.clearance_db.ix[nanidx, permission] = num

        # Add person and facedata to an array somewhere.

        # Write to disk.
        self._sync()
        pass

    def add_permission(self, permission, people=()):
        """
        Adds a new permission category with names of people to add.
        :param permission: Name of permission.
        :param people: List of people (by ID Number) to add.
        :return: True if successful. No changes written on failure.
        """
        # Verify that the permission does not exist.
        if permission in self.clearance_db.columns:
            return False

        # TODO Verify that all the people are in the people database.

        # Create a new dataFrame
        dfnew = df({permission: list(people)})

        # Combine with existing dataFrame
        self.clearance_db = pd.concat([self.clearance_db, dfnew], axis=1)

        self._sync()
        pass

    def _sync(self):
        """
        Writes any changes back to file on disk.
        :return: True on success. Hopefully no changes written on failure.
        """
        pass
