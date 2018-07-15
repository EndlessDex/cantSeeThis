# A script that quickly checks that a lot of the the PeopleDatabase API doesn't cause crashes
from database.PeopleDatabase import PeopleDatabase

# Usage: from pwd=cantSeeThis, python
# >>> import database.check_no_crash

pdb = PeopleDatabase("database/test.xlsx")

if pdb.has_permission(11, "Secret"):
    print("fail: ID 11 should not have secret clearance.")

if not pdb.has_permission(222, "Secret"):
    print("fail: ID 222 should have secret clearance.")

if pdb.has_permission(11, "Not a permission foobar"):
    print("fail: Permission Name should not exist.")

# Try to give 11 clearance:
pdb.set_person_permission(11, "Secret")

if not pdb.has_permission(11, "Secret"):
    print("fail: 11 should now have Secret clearance.")

pdb.remove_person_permission(11, "Secret")
if pdb.has_permission(11, "Secret"):
    print("fail: ID 11 should no longer have secret clearance.")

# Try to remove 11:
pdb.remove_person(11)
if 11 in [y for x, y in pdb.get_people()]:
    print("fail: ID 11 should have been removed")
if pdb.has_permission(11, "None"):
    print("fail: ID 11 should no longer have any clearance.")

pdb.add_person(11, facedata=000, permissions=("None",), name="Person B")
if 11 not in [y for x, y in pdb.get_people()]:
    print("fail: ID 11 should have been added")
if not pdb.has_permission(11, "None"):
    print("fail: ID 11 should have clearance again.")