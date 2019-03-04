from statistics import mean as m

userDict = {'username':'password','Mac':'Med'}
gradeDict = {'Alex':[92,76,88], 'Jeff':[78,88,93], 'Sam':[89,92,93]}
cont = False

def main():
    print('\n\tWelcome to the Super Wonderful Amazing Grading (SWAG) System!\n')
    print('\t[1] - Enter Grades')
    print('\t[2] - Add or Remove Student')
    print('\t[3] - Student Average Grades')
    print('\t[4] - Exit\n')
    choice = input('What would you like to do today? (Enter a number): ')

    if choice == '1':
        print('\nEnter Grades')
        while True:
            EnterGrades()
    elif choice == '2':
        print('\nAdd or Remove a Student')
        while True:
            AoR()
    elif choice == '3':
        print('\nAverage Grades')
        Avg()
    elif choice == '4':
        print('Goodbye\n')
        GetSignedIn()
    else:
        print('That\'s not a choice, try again')
        


def EnterGrades():
    print(gradeDict)
    student = input('Student Name: ')
    grade = input('Grade: ')
    print('Adding Grade...')
    if student in gradeDict:
        gradeDict[student].append(grade)
        print(gradeDict)
        Cont()
    else:
        print('''That name is not registered, please return to menu to add or enter a different student''')
        Cont()



def AoR():
    print(gradeDict)
    action = input('Would you like to Add or Remove? ')
    if action == 'Add' or action == 'add' or action == 'A' or action == 'a' or action == 'ad' or action == 'Ad':
        print('Please add a student')
        add = input('Student name: ')
        grade = input('Enter grade: ')
        gradeDict[add] = grade
        print(gradeDict)
        print('Student and grade added.\n')
        Cont()
    elif action == 'Remove' or action == 'remove' or action == 'R' or action == 'r':
        print('Who would you like to remove?')
        remove = input('Student name: ')
        if remove in gradeDict:
            print('Removing Student...')
            del gradeDict[remove]
            print(gradeDict)
            print('Student removed.')
            Cont()
        else:
            print('Student not recognized.')
            Cont()
    else:
        print('Command not recognized.')
        Cont()


def Avg():
    for eachStudent in gradeDict:
        gradeList = gradeDict[eachStudent]
        avgGrade = m(gradeList)

        print(eachStudent, 'has an average grade of: ',avgGrade)
        
                

    
def Cont():
    Return = input('\nReturn to Main Menu? Y/N: ')
    if Return == 'Y' or Return == 'y':
        print('Returning to Main Menu...')
        main()
    elif Return == 'N' or Return == 'n':
        cont = True
    else:
        print('Command not recognized.')
        Cont()



def GetSignedIn():
    user = input('Username: ')
    password = input('Password: ')
    if user in userDict:
        if userDict[user] == password:
            print('Welcome ' +user)
            while True:
                main()
        else:
            print('Try again or else I\'m calling the FBI')
            GetSignedIn()
    else:
        print('Try again or else I\'m calling the FBI')
        GetSignedIn()

GetSignedIn()



    
