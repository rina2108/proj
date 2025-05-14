class Student:
    def __init__(self, last_name, birth_date, group_number, grades):
        self.last_name = last_name
        self.birth_date = birth_date
        self.group_number = group_number
        self.grades = grades

    def change_last_name(self, new_last_name):
        self.last_name = new_last_name

    def change_birth_date(self, new_birth_date):
        self.birth_date = new_birth_date

    def change_group_number(self, new_group_number):
        self.group_number = new_group_number

    def info(self):
        print(f"Фамилия: {self.last_name}")
        print(f"Дата рождения: {self.birth_date}")
        print(f"Номер группы: {self.group_number}")
        print(f"Успеваемость: {self.grades}")

student1 = Student("Каленова", "2000-05-07", "Группа-1", [5, 4, 5, 3, 4])
student2 = Student("Ромашенко", "2015-02-17", "Группа-2", [4, 4, 4, 5, 5])

student1.change_last_name("Сидоров")
student1.change_birth_date("2004-06-01")
student1.change_group_number("Группа-3")

students = [student1, student2]

search_last_name = input("Введите фамилию: ")
search_birth_date = input("Введите дату рождения (гггг-мм-дд): ")

found = False
for student in students:
    if student.last_name == search_last_name and student.birth_date == search_birth_date:
        print("Найден студент:")
        student.info()
        found = True

if not found:
    print("Студент не найден.")