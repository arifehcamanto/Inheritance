import sys
from student import *
from teacher import *

students = []
teachers = []


def addStudents():

    while True:

        print()
        print('Stud = Add Student')
        print('Teach = Add Teacher')
        print()

        add = input('What would you like to include? ')
        add = add.upper()

        print()

        if add == 'Stud':

            id = input('Enter student id: ')
            last_name = input('Enter student last name: ')
            first_name = input('Enter student first name: ')
            middle_name = input('Enter student middle name: ')
            type = input('Enter student Type: ')
            course = input('Enter student Course: ')
            year = input('Enter student Year: ')
            section = input('Enter student Section: ')
            print('----------------------------')
            filipino = int(input('Input grade filipino: '))
            math = int(input('Input grade math: '))
            science = int(input('Input grade science: '))
            english = int(input('Input grade english: '))

            stud = Grade(filipino, math, science, english)
            stud.id = id
            stud.last_name = last_name
            stud.first_name = first_name
            stud.middle_name = middle_name
            stud.type = type
            stud.course = course
            stud.year = year
            stud.section = section

            students.append(stud)


        elif add == 'Teach':

            id = input('Enter teacher id: ')
            last_name = input('Enter teacher last name: ')
            first_name = input('Enter teacher first name: ')
            middle_name = input('Enter teacher middle name: ')
            type = input('Enter teacher type: ')
            print('----------------------------')
            department = input('Input Department: ')
            position = input('Input Position: ')
            subject = input('Input Subject: ')

            tch = Load(subject)
            tch.department = department
            tch.position = position
            tch.id = id
            tch.last_name = last_name
            tch.first_name = first_name
            tch.middle_name = middle_name
            tch.type = type

            teachers.append(tch)


        else:
            menu()

        print()
        ans = input('Do you want to add another? [y/n]: ')
        ans = ans.lower()

        if (ans != 'y'):
            break


        menu()

def deleteRecord():

    print()
    print('Stud - Delete from Student')
    print('Teach = Delete from Teacher')
    print('DTeach - Delete Teachers')
    print('DSstud - Delete Students')
    print('DAll - Delete All')
    print()

    delete = input('Which record do you want to delete? ')
    delete = delete.upper()

    if delete == 'Stud':
        i = int(input('Enter index: '))
        students.pop(i)

    elif delete == 'Teach':
        i = int(input('Enter index: '))
        teachers.pop(i)

    elif delete == 'DTeach':
        teachers.clear()

    elif delete == 'DStud':
        students.clear()

    elif delete == 'DAll':
        students.clear()
        teachers.clear()

    else:
        deleteRecord()


    menu()



def searchRecord():

    print()
    print('Stud - Search Student')
    print('Teach - Search Teacher')
    print()

    search = input('What are you looking for? ')
    search = search.upper()

    if search == 'Stud':


        i = int(input('Enter index: '))

        print(f'{i} \t | {students[i].getType()} \t | {students[i].getName()} \t | {students[i].getID()} \t | {students[i].get_yr_course_sec()} \t | {students[i].get_average()}')

    elif search == 'Teach':
        i = int(input('Enter index: '))
        print(f'{i} \t | {teachers[i].getType()} \t | {teachers[i].getName()} \t | {teachers[i].getID()} \t | {teachers[i].get_dep_pos()} \t | {teachers[i].get_sub()}')

    else:
        searchRecord()

    menu()




def displayRecords():

    print()
    print('Stud - Display Student')
    print('Teach - Display Teacher')
    print('All - Display All')
    print()

    display = input('What information do you want to see?: ')
    display = display.upper()

    if display == 'Stud':
        print()
        print('----------------------------------------------------------------------------------')
        i = 0
        for s in students:
            print(f'{i} \t | {s.getType()} \t | {s.getName()} \t | {s.getID()} \t | {s.get_yr_course_sec()} \t | {s.get_average()}')
            i += 1
        print('----------------------------------------------------------------------------------')

    elif display == 'Teach':
        print()
        print('----------------------------------------------------------------------------------')
        i = 0
        for t in teachers:
            print(f'{i} \t | {t.getType()} \t | {t.getName()} \t | {t.getID()} \t | {t.get_dep_pos()} \t | {t.get_sub()}')
            i += 1
        print('----------------------------------------------------------------------------------')

    elif display == 'All':
        print()
        print('----------------------------------------------------------------------------------')

        i = 0
        for s in students:
            print(f'{i} \t | {s.getType()} \t | {s.getName()} \t | {s.getID()} \t | {s.get_yr_course_sec()} \t | {s.get_average()}')
            i += 1

       
        i = 0
        for t in teachers:
            print(f'{i} \t | {t.getType()} \t | {t.getName()} \t | {t.getID()} \t | {t.get_dep_pos()} \t | {t.get_sub()}')
            i += 1
        print('----------------------------------------------------------------------------------')


    else:
        displayRecords()

    menu()




def menu():

    print()
    print()
    print('::Menu::')
    print('DRec - delete record        SRec - search record')
    print('ARec - add record           DAll - display all')
    print()

    choice = input('Enter an action: ')
    choice = choice.upper()

    if (choice == 'DRec'):
        deleteRecord()
    elif (choice == 'ARec'):
        addStudents()
    elif(choice == 'SRec'):
        searchRecord()
    elif (choice == 'DAll'):
        displayRecords()
    else:
        menu()


    print()

menu()