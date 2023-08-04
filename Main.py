from Student import *
from Hash import *
from TrieTree import *


def Insertion(tree, hAsh):

    # getting information from user

    print("please insert name")
    name = input()

    print("please insert student number")
    num = int(input())

    print("please insert gpa")
    gpa = input()
    print("please insert major")
    major = input()

    # making a student object
    st = Student(name, num, gpa, major)

    # check for existing in tree ( checking for same student number )
    if tree.search(num) is False:

        # add to hash table
        value = hAsh.hash(num, st)

        # add to Trie Tree
        tree.insert(num, value)
        print("insertion completed successfully")
        print()
        print()
        print()
    else:
        print("student is already exist")
        print()
        print()
        print()


def Edit(tree, hAsh):
    print("please insert student number")

    # get student number from user
    number = int(input())

    while True:
        print("please insert student number")

        # find prefix of number for suggestion ( hash keys )
        keys = tree.preSearch(number)

        if keys is None:
            print("student not found")
            print()
            print()
            print()
            return

        # show suggestion to user
        for i in range(len(keys)):
            print(str(i + 1) + "- " + str(hAsh.table[keys[i]].StudentNumber))

        # exit if it was to suggestion
        if len(keys) == 0:
            print("student not found")
            print()
            print()
            print()
            return

        # get new student number or select from suggestion
        print("please choose your student number or input new one")
        number = int(input())
        if number <= len(keys):
            break

    # get student's object from hash table
    obj = hAsh.table[keys[number - 1]]

    while True:

        # edition panel
        print("please choose option which has to be changed")
        print("1- Name : " + obj.Name)
        print("2- Student number: " + str(obj.StudentNumber))
        print("3- GPA: " + str(obj.GPA))
        print("4- Major: " + str(obj.Major))
        print("5- delete student")
        print("6- exit")
        print()

        selection = int(input())

        # change name
        if selection == 1:
            print("please insert new Name")
            name = input()
            obj.Name = name

        # change student number
        if selection == 2:

            print("please insert new number")

            # get new number
            new_number = int(input())

            # check for similarity
            if tree.search(new_number) is False:

                # delete previous number from key
                tree.Delete(str(obj.StudentNumber))

                # change student number in object
                obj.StudentNumber = new_number

                # make new hash key
                new_key = hAsh.hash(new_number, obj)

                # insert new student number and key to tree
                tree.insert(new_number, new_key)
                print("operation complete successfully")
                print()
            else:
                print("number is already exist")
                print()

        # change GPA
        if selection == 3:
            print("please insert new GPA")
            gpa = int(input())
            obj.GPA = gpa

        # change major
        if selection == 4:
            print("please insert new major")
            major = input()
            obj.Major = major

        # delete student
        if selection == 5:

            # remove hash value from tree
            hAsh.table[tree.GetKey(obj.StudentNumber)] = None

            # delete student number from tree
            tree.Delete(str(obj.StudentNumber))
            print("Deletion finished successfully")
            print()
            print()
            print()
            break

        if selection == 6:
            print("exiting....")
            print()
            print()
            print()
            break


# make hash table
HashTable = Hash(105)

# make trie tree
Trie = TrieTree()

while True:
    print("welcome")
    print("please choose your operation")
    print("1- Insert new student    2- Search for student")
    inn = int(input())

    if inn == 1:

        # run insertion method
        Insertion(Trie, HashTable)

    else:

        # run edition method
        Edit(Trie, HashTable)
