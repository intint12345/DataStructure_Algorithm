import sys
import csv
#import pandas as pd
import os
#import itertools
import time


def initial_phonebook():
    phone_book = {}
    header = True
    #### To check wheter the contact book already existed or not
    if os.path.exists('./ContactList.csv'):
        # phone_book = pd.read_csv('ContactList.csv', header=None, index_col=0, squeeze=True).to_dict()
        filehandle = open('ContactList.csv')
        for line in filehandle.readlines():
            if header:
                header = False
                continue
            Name, Phone, Email, DOB, Category = line.strip().split(",")
            d_Name = phone_book.get(Name, {})
            """
            d_Category = d_Name.get(Category, {})
            d_DOB = d_Name.get(DOB, {})
            d_Email = d_Name.get(Email, {})
            d_Phone = d_Name.get(Phone, {})
            """
            d_Name['Phone'] = Phone
            d_Name['Email'] = Email
            d_Name['DOB'] = DOB
            d_Name['Category'] = Category
            phone_book[Name] = d_Name
    else:

        rows, cols = int(input("Please enter initial number of contacts: ")), 5

        for i in range(rows):
            contact = {}
            print("\nEnter contact %d details in the following order (ONLY):" % (i + 1))
            print("NOTE: * indicates mandatory fields")
            print("....................................................................")
            temp = []
            for j in range(cols):

                # We have taken the conditions for values of j only for the personalized fields
                # such as name, number, e-mail id, dob, category etc
                if j == 0:
                    temp.append(str(input("Enter name*: ")))

                    # We need to check if the user has left the name empty as its mentioned that
                    # name & number are mandatory fields.
                    # So implement a condition to check as below.
                    if temp[j] == '' or temp[j] == ' ':
                        sys.exit(
                            "Name is a mandatory field. Process exiting due to blank field...")
                        # This will exit the process if a blank field is encountered.

                if j == 1:
                    temp.append(str(input("Enter number*: ")))
                    # We do not need to check if user has entered the number because int automatically
                    # takes care of it. Int value cannot accept a blank as that counts as a string.
                    # So process automatically exits without us using the sys package.

                if j == 2:
                    temp.append(str(input("Enter e-mail address: ")))
                    # Even if this field is left as blank, None will take the blank's place
                    if temp[j] == '' or temp[j] == ' ':
                        temp[j] = None

                if j == 3:
                    temp.append(str(input("Enter date of birth(dd/mm/yy): ")))
                    # Whatever format the user enters dob in, it won't make a difference to the compiler
                    # Only while searching the user will have to enter query exactly the same way as
                    # he entered during the input so as to ensure accurate searches
                    if temp[j] == '' or temp[j] == ' ':
                        # Even if this field is left as blank, None will take the blank's place
                        temp[j] = None
                if j == 4:
                    temp.append(
                        str(input("Enter category(Family/Friends/Work/Others): ")))
                    # Even if this field is left as blank, None will take the blank's place
                    if temp[j] == "" or temp[j] == ' ':
                        temp[j] = None

            contact = {'Phone': temp[1], 'Email': temp[2], 'DOB': temp[3], 'Category': temp[4]}
            # By this step we are appending a list temp into a list phone_book
            # That means phone_book is a 2-D array and temp is a 1-D array
            phone_book[temp[0]] = contact
    ##print(phone_book)
    return phone_book


def display_all(pb):
    if not pb:
        # if display function is called after deleting all contacts then the len will be 0
        # And then without this condition it will throw an error
        print("Phonebook is empty.")
    else:
        for key, value in pb.items():
            print('Name: ', key, '->', value)


def checkExistingKey():
    check = True
    while check:
        name = str(input("Enter name: "))
        if pb.get(name) is not None:
            # name is a key, so we shouldn't insert the same name
            # To prevent the override the old key when inserting the same key
            print("This name is already exists, please try again")
            check = True
        elif not name:
            # name must not be null because it's key
            print("Name is required, please try again")
            check = True
        else:
            check = False
            return name


def add_contact(pb):
    # Adding a contact is the easiest because all you need to do is:
    # append another list of details into the already existing list
    dip = []
    for i in range(5):
        contact = {}
        if i == 0:
            inputName = checkExistingKey()
            # print("inputName: ", inputName)
            dip.append(inputName)
        if i == 1:
            dip.append(str(input("Enter number: ")))
        if i == 2:
            dip.append(str(input("Enter e-mail address: ")))
            if dip[i] == "" or dip[i] == ' ':
                dip[i] = None
        if i == 3:
            dip.append(str(input("Enter date of birth(dd/mm/yy): ")))
            if dip[i] == "" or dip[i] == ' ':
                dip[i] = None
        if i == 4:
            dip.append(
                str(input("Enter category(Family/Friends/Work/Others): ")))
            if dip[i] == "" or dip[i] == ' ':
                dip[i] = None
    print(dip)
    time_start = time.perf_counter_ns()
    contact = {'Phone': dip[1], 'Email': dip[2], 'DOB': dip[3], 'Category': dip[4]}
    pb[dip[0]] = contact
    time_end = time.perf_counter_ns()
    time_spent = time_end - time_start
    print("Time Usage: ", time_spent)
    # And once you modify the list, you return it to the calling function wiz main, here.
    return pb


def remove_existing(pb):
    # This function is to remove a contact's details from existing phonebook
   query = str(input("Please enter the name of the contact you wish to remove: "))
   rm_result = pb.pop(query, None)
   print(rm_result)
   
   if rm_result != None:
        print("This query has now been removed")
   else:
       print("Sorry, you have entered an invalid query.\Please recheck and try again later.")
   return pb


def delete_all(pb):
    # This function will simply delete all the entries in the phonebook pb
    # It will return an empty phonebook after clearing
    return pb.clear()


def search_existing(pb):
    # This function searches for an existing contact and displays the result
    print("=" * 50)
    choice = int(input("Enter search criteria\n\n1. Name\n2. Number\n3. Email-id\n4. DOB\n5. Category(Family/Friends/Work/Others)\
    \nPlease enter: "))
    # We're doing so just to ensure that the user experiences a customized search result

    temp = []
    check = -1

    if choice == 1:
        # This will execute for searches based on contact name
        query = str(
            input("Please enter the name of the contact you wish to search: "))
        time_start = time.perf_counter_ns()
        for key, value in pb.items():
            if key.find(query) != -1:
                print('Name: ', key, '->', value)
                check = check + 1
        time_end = time.perf_counter_ns()
        time_spent = time_end-time_start

    elif choice == 2:
        # This will execute for searches based on contact number
        query = str(
            input("Please enter the number of the contact you wish to search: "))
        time_start = time.perf_counter_ns()
        for key, value in pb.items():
            if value['Phone'].find(query) != -1:
                print('Name: ', key, '->', value)
                check = check + 1
        time_end = time.perf_counter_ns()
        time_spent = time_end-time_start

    elif choice == 3:
        # This will execute for searches based on contact's e-mail address
        query = str(input("Please enter the e-mail ID of the contact you wish to search: "))
        time_start = time.perf_counter_ns()
        for key, value in pb.items():
            if value['Email'].find(query) != -1:
                print('Name: ', key, '->', value)
                check = check + 1
        time_end = time.perf_counter_ns()
        time_spent = time_end-time_start

    elif choice == 4:
        # This will execute for searches based on contact''s date of birth
        query = str(input("Please enter the DOB (in dd/mm/yyyy format ONLY)\
            of the contact you wish to search: "))
        time_start = time.perf_counter_ns()
        for key, value in pb.items():
            if value['DOB'].find(query) != -1:
                print('Name: ', key, '->', value)
                check = check + 1
        time_end = time.perf_counter_ns()
        time_spent = time_end-time_start

    elif choice == 5:
        # This will execute for searches based on contact category
        query = str(
            input("Please enter the category of the contact you wish to search: "))
        time_start = time.perf_counter_ns()
        for key, value in pb.items():
            if value['Category'].find(query) != -1:
                print('Name: ', key, '->', value)
                check = check + 1
        # All contacts under query category will be shown using this feature
        time_end = time.perf_counter_ns()
        time_spent = time_end-time_start

    else:
        time_start = time.perf_counter_ns()
        # If the user enters any other choice then the search will be unsuccessful
        print("Invalid search criteria")
        time_end = time.perf_counter_ns()
        time_spent = time_end-time_start
        
        return -1
        
    # returning -1 indicates that the search was unsuccessful

    # all the searches are stored in temp and all the results will be displayed with
    # the help of display function

    if check == -1:
        print(f'Time Usage: {time_spent}')
        return -1
        # returning -1 indicates that the query did not exist in the directory
    else:
        # display_all(temp)
        print(f'Time Usage: {time_spent}')
        return check
        # we're just returning a index value wiz not -1 to calling function just to notify
        # that the search worked successfully


def thanks():
    # A simple gesture of courtesy towards the user to enhance user experience
    print("********************************************************************")
    print("Thank you for using our Smartphone directory system.")
    print("Please visit again!")
    print("********************************************************************")
    sys.exit("Goodbye, have a nice day ahead!")


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


def writeCSV(pb):
    # header = set(i for b in map(dict.keys, pb.values()) for i in b)
    if not pb:
        if os.path.exists("./ContactList.csv"):
            os.remove("ContactList.csv")
    else:
        header = ['Phone', 'Email', 'DOB', 'Category']
        # with open("ContactList.csv", "w", newline="") as f:
        with open("ContactList.csv", "w", newline="") as f:
            w = csv.writer(f)
            w.writerow(['Name', *header])
            for a, b in pb.items():
                w.writerow([a] + [b.get(i, '') for i in header])

    # with open('ContactList.csv', 'w') as csvfile:
    #    # keep key-value in the same row
    #    writer = csv.writer(csvfile)
    #    for key, value in pb.items():
    #        writer.writerow([key, value])
    # writer = csv.DictWriter(csvfile, fieldnames=pb.keys())
    # writer.writeheader()
    # writer.writerow(pb)


# Main function code
print("....................................................................")
print("Hello dear user, welcome to our smartphone directory system")
print("You may now proceed to explore this directory")
print("....................................................................")
# This is solely meant for decoration purpose only.
# You're free to modify your interface as per your will to make it look interactive


ch = 1
pb = initial_phonebook()
while ch in (1, 2, 3, 4, 5, 6):
    ch = menu()
    if ch == 1:
        pb = add_contact(pb)
    elif ch == 2:
        d = search_existing(pb)
        if d == -1:
            print("The contact does not exist. Please try again")
    elif ch == 3:
        pb = remove_existing(pb)
    elif ch == 4:
        pb = delete_all(pb)
    elif ch == 5:
        display_all(pb)
    elif ch == 6:
        writeCSV(pb)
        thanks()
    else:
        ch = menu()
