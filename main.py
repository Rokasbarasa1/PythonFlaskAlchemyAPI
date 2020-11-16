# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import pyodbc as pyodbc

from objects import Dog, Student, Course, Cat, DogSecond, Pet, Person


def get_settings():
    server = 'tcp:enviorment-server.database.windows.net'
    database = 'EnviormentDatabase'
    username = 'rokasbarasa1'
    password = 'Augis123*'
    cnxn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
    cursor = cnxn.cursor()
    cursor.execute('SELECT * FROM [EnviormentDatabase].[dbo].[Settings]')



def get_co2():
    server = 'tcp:enviorment-server.database.windows.net'
    database = 'EnviormentDatabase'
    username = 'rokasbarasa1'
    password = 'Augis123*'
    cnxn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
    cursor = cnxn.cursor()
    cursor.execute('SELECT top 1 * FROM [EnviormentDatabase].[dbo].[CarbonDioxideReading]')
    for row in cursor:
        print(row)


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("TESTING OF DOG CLASS")
    dogs_name = ["Rokas", "kaka"]
    dogs_age = [32, 99922]
    d = Dog(dogs_name[0], dogs_age[0])
    print(d.get_name())
    print(d.get_age())
    d2 = Dog(dogs_name[1], dogs_age[1])
    print(d2.get_name())
    print(d2.get_age())
    print("\nTESTING OF STUDENT AND COURSE CLASSES")
    s1 = Student("Tim", 19, 96)
    s2 = Student("fam", 53, 45)
    s3 = Student("Rpo", 44, 44)

    course1 = Course("History", 2)
    print(course1.add_student(s1))
    print(course1.add_student(s2))
    print(course1.add_student(s3))
    print(course1.get_average_grade())

    print("\nTESTING OF INHERITANCE")
    cat = Cat("kate", 32, "Brown")
    dog = DogSecond("Amsis", 2)
    animal = Pet("KAKA", 33)
    cat.show()
    dog.show()

    print("\nTESTING OF static ")
    p1 = Person("Tomas")
    p2 = Person("Rokas")
    p2.number_of_people = 2343
    p1.number_of_people = 22
    Person.number_of_people = 2003003
    print(p2.number_of_people)
    print(Person.number_of_people)
    print(p1.number_of_people)
    print(Person.get_number_of_people())

    print("\nTESTING OF CONNECTIONS TO DATABASE")
    print(get_settings())
    print(get_co2())
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
