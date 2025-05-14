class Worker:
    def __init__(self, name, surname, rate, days):
        self.name = name
        self.surname = surname
        self.rate = rate
        self.days = days

    def GetSalary(self):
        return self.rate * self.days

worker = Worker("Катя", "Майт", 3550, 21)
print(f"Зарплата {worker.name} {worker.surname}: {worker.GetSalary()} руб.")