class Person:
    def __init__(self, name="Unknown", age=0):
        self.name = name
        self.age = age
        print(f"Создан объект: {self.name}, возраст {self.age}")

    def __del__(self):
        print(f"Объект {self.name} удален")

    def display(self):
        print(f"Имя: {self.name}, Возраст: {self.age}")

person1 = Person("Алиса", 30)
person1.display()

person2 = Person()
person2.display()

del person1
del person2