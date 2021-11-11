# importing the module
import sys
import csv
import os
import math


class Node:
    def __init__(self, val):
        self.l = None
        self.r = None
        self.v = val
        self.p = None


class Tree:
    def __init__(self):
        self.root = None

    def getRoot(self):
        return self.root

    def add(self, pb):
        print("Add func", pb)
        dip = []
        for i in range(5):
            if i == 0:
                dip.append(str(input("Enter name: ")))
            if i == 1:
                dip.append(str(input("Enter number: ")))
            if i == 2:
                dip.append(str(input("Enter e-mail address: ")))
            if i == 3:
                dip.append(str(input("Enter date of birth(dd/mm/yy): ")))
            if i == 4:
                dip.append(str(input("Enter category(Family/Friends/Work/Others): ")))

        if self.root is None:
            #self.root = Node(val)
            self.root = Node(dip[0])
            # print("root")
            pb.append(dip)
            return pb
        else:
            self._add(dip[0], self.root, dip)
            # print(self.root)
            return pb

    def _add(self, val, node, dip):
        # print("Val", val)
        if val < node.v:
            if node.l is not None:
                self._add(val, node.l, dip)
            else:
                node.l = Node(val)
                node.l.p = node
                pb.append(dip)
                # print("Left ", pb)
                # print('add', val, 'parent is ', node.l.p.v)
        else:
            if node.r is not None:
                self._add(val, node.r, dip)
            else:
                node.r = Node(val)
                node.r.p = node
                pb.append(dip)
                # print('add', val, 'parent is ', node.r.p.v)

    def find(self):
        name = str(input("Enter name that you want to search: "))
        if self.root is not None:
            return self._find(name, self.root)
        else:
            return print("Invalid search criteria")

    def _find(self, val, node):
        if val == node.v:
            for i in range(len(pb)):
                if val == pb[i][0]:
                    info = pb[i][1] + " " + pb[i][2] + " " + pb[i][3] + " " + pb[i][4]
            return print(node.v + " -> " + info)
        elif val < node.v and node.l is not None:
            return self._find(val, node.l)
        elif val > node.v and node.r is not None:
            return self._find(val, node.r)

    def printTree(self):
        if self.root is not None:
            self._printTree(self.root)

    def _printTree(self, node):
        if node is not None:
            self._printTree(node.l)
            print(str(node.v))
            for i in range(len(pb)):
                if str(node.v) == pb[i][0]:
                    print(pb[i][1], pb[i][2], pb[i][3], pb[i][4])
            self._printTree(node.r)


# this function will be the first to run as soon as the main function executes
def initial_phonebook():
    phone_book = []
    header = True
    #### To check wheter the contact book already existed or not
    if os.path.exists('ContactList_BST.csv'):
        # phone_book = pd.read_csv('ContactList.csv', header=None, index_col=0, squeeze=True).to_dict()
        with open('ContactList_BST.csv', 'r') as csvfile:
            csvReader = csv.reader(csvfile)
            next(csvReader)
            for row in csvReader:
                phone_book.append(row)

    # print(phone_book)
    return phone_book


def menu():
    # We created this simple menu function for
    # code reusability & also for an interactive console
    # Menu func will only execute when called
    print("********************************************************************")
    print("\t\t\tSMARTPHONE DIRECTORY", flush=False)
    print("********************************************************************")
    print("\tYou can now perform the following operations on this phonebook\n")
    print("1. Add a new contact")
    print("2. Search for a contact")
    print("3. Remove an existing contact")
    print("4. Delete all contacts")
    print("5. Display all contacts")
    print("6. Exit phonebook")

    # Out of the provided 6 choices, user needs to enter any 1 choice among the 6
    # We return the entered choice to the calling function wiz main in our case
    choice = int(input("Please enter your choice: "))
    return choice


def remove_existing(pb):
    # This function is to remove a contact's details from existing phonebook
    query = str(
        input("Please enter the name of the contact you wish to remove: "))
    # We'll collect name of the contact and search if it exists in our phonebook

    temp = 0
    # temp is a checking variable here. We assigned a value 0 to temp.

    for i in range(len(pb)):
        if query == pb[i][0]:
            temp += 1
            # Temp will be incremented & it won't be 0 anymore in this function's scope

            print(pb.pop(i))
            # The pop function removes entry at index i

            print("This query has now been removed")
            # printing a confirmation message after removal.
            # This ensures that removal was successful.
            # After removal we will return the modified phonebook to the calling function
            # which is main in our program

            return pb
    if temp == 0:
        # Now if at all any case matches temp should've incremented but if otherwise,
        # temp will remain 0 and that means the query does not exist in this phonebook
        print("Sorry, you have entered an invalid query. Please recheck and try again later.")
        return pb


def delete_all(pb):
    # This function will simply delete all the entries in the phonebook pb
    # It will return an empty phonebook after clearing
    return pb.clear()


def thanks():
    # A simple gesture of courtesy towards the user to enhance user experience
    print("********************************************************************")
    print("Thank you for using our Smartphone directory system.")
    print("Please visit again!")
    print("********************************************************************")
    sys.exit("Goodbye, have a nice day ahead!")


def writeCSV(pb):
    # header = set(i for b in map(dict.keys, pb.values()) for i in b)
    if not pb:
        if os.path.exists("ContactList_BST.csv"):
            os.remove("ContactList_BST.csv")
    else:
        header = ['Name', 'Phone', 'Email', 'DOB', 'Category']
        # with open("ContactList.csv", "w", newline="") as f:
        with open("ContactList_BST.csv", "w", newline='') as f:
            w = csv.writer(f)
            w.writerow(header)
            w.writerows(pb)


# Main function code
print("....................................................................")
print("Hello dear user, welcome to our smartphone directory system")
print("You may now proceed to explore this directory")
print("....................................................................")
# This is solely meant for decoration purpose only.
# You're free to modify your interface as per your will to make it look interactive

ch = 1
tree = Tree()
pb = initial_phonebook()
print(pb)
while ch in (1, 2, 3, 4, 5, 6):
    ch = menu()
    if ch == 1:
        pb = tree.add(pb)
    elif ch == 2:
        tree.find()
    elif ch == 3:
        pb = remove_existing(pb)
    elif ch == 4:
        pb = delete_all(pb)
    elif ch == 5:
        tree.printTree()
    elif ch == 6:
        writeCSV(pb)
        thanks()
    else:
        ch = menu()