import sqlite3

class Student:
    def __init__(self, name, surname, mid_name, group, grades):
        self.name = name
        self.surname = surname
        self.mid_name = mid_name
        self.group = group
        self.grades = grades

class StudentDatabase:
    def __init__(self, db_name="students.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                first_name TEXT,
                last_name TEXT,
                middle_name TEXT,
                group_name TEXT,
                grade1 INTEGER,
                grade2 INTEGER,
                grade3 INTEGER,
                grade4 INTEGER
            )
        ''')
        self.conn.commit()

    def add_student(self, student):
        self.cursor.execute('''
            INSERT INTO students 
            (first_name, last_name, middle_name, group_name, grade1, grade2, grade3, grade4)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (student.name,
              student.surname,
              student.mid_name,
              student.group,
              *student.grades))
        self.conn.commit()

    def view_all_students(self):
        self.cursor.execute('SELECT * FROM students')
        return self.cursor.fetchall()

    def view_student(self, student_id):
        self.cursor.execute('SELECT * FROM students WHERE id = ?', (student_id,))
        student = self.cursor.fetchone()
        if student:
            avg = sum(student[5:9]) / 4
            return student, avg
        else:
            return None, None

    def edit_student(self, student_id, student: Student):
        self.cursor.execute('''
            UPDATE students
            SET first_name = ?, last_name = ?, middle_name = ?, group_name = ?, grade1 = ?, grade2 = ?, grade3 = ?, grade4 = ?
            WHERE id = ?
        ''', (student.name,
              student.surname,
              student.mid_name,
              student.group,
              *student.grades,
              student_id))
        self.conn.commit()

    def delete_student(self, student_id):
        self.cursor.execute('DELETE FROM students WHERE id = ?', (student_id,))
        self.conn.commit()

    def group_average(self, group_name):
        self.cursor.execute('SELECT grade1, grade2, grade3, grade4 FROM students WHERE group_name = ?', (group_name,))
        grades = self.cursor.fetchall()
        if grades:
            total = sum(sum(g) for g in grades)
            count = len(grades) * 4
            return total / count
        else:
            return None

    def close(self):
        self.conn.close()

def main():
    db = StudentDatabase()

    while True:
        print("\nСписок:")
        print("1. Добавить студента")
        print("2. Просмотреть всех студентов")
        print("3. Просмотреть одного студента")
        print("4. Редактировать студента")
        print("5. Удалить студента")
        print("6. Просмотреть средний балл группы")
        print("7. Выход")
        choice = input("Выберите действие: ")

        if choice == "1":
            fn = input("Имя: ")
            ln = input("Фамилия: ")
            mn = input("Отчество: ")
            group = input("Группа: ")
            grades = [int(input(f"Оценка {i+1}: ")) for i in range(4)]
            student = Student(fn, ln, mn, group, grades)
            db.add_student(student)

        elif choice == "2":
            students = db.view_all_students()
            for s in students:
                print(s)

        elif choice == "3":
            sid = int(input("ID студента: "))
            student, avg = db.view_student(sid)
            if student:
                print(student)
                print(f"Средний балл: {avg:.2f}")
            else:
                print("Студент не найден.")

        elif choice == "4":
            sid = int(input("ID студента: "))
            fn = input("Новое имя: ")
            ln = input("Новая фамилия: ")
            mn = input("Новое отчество: ")
            group = input("Новая группа: ")
            grades = [int(input(f"Новая оценка {i+1}: ")) for i in range(4)]
            student = Student(fn, ln, mn, group, grades)
            db.edit_student(sid, student)

        elif choice == "5":
            sid = int(input("ID студента для удаления: "))
            db.delete_student(sid)

        elif choice == "6":
            group = input("Введите название группы: ")
            avg = db.group_average(group)
            if avg is not None:
                print(f"Средний балл группы {group}: {avg:.2f}")
            else:
                print("Группа не найдена.")

        elif choice == "7":
            db.close()
            break

        else:
            print("Некорректный ввод, попробуйте снова.")

if __name__ == "__main__":
    main()