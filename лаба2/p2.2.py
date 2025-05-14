class Train:
    def __init__(self, destination, train_number, time):
        self.destination = destination
        self.train_number = train_number
        self.time = time

    def info(self):
        print(f"Пункт назначения: {self.destination}")
        print(f"Номер поезда: {self.train_number}")
        print(f"Время отправления: {self.time}")

train1 = Train("Томск", 67, "12:30")
train2 = Train("Новосибирск", 152, "15:45")

trains = [train1, train2]

number = int(input("Введите номер поезда: "))

found = False
for train in trains:
    if train.train_number == number:
        print("Информация о поезде:")
        train.info()
        found = True

if not found:
    print("Поезд не найден.")