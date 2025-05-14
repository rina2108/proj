class Counter:
    def __init__(self, value=0):
        self.value = value

    def more(self):
        self.value += 1

    def less(self):
        self.value -= 1

    def value(self):
        return self.value

counter1 = Counter()
print("Начальное значение counter1:", counter1.value)
counter1.more()
print("После увеличения:", counter1.value)
counter1.less()
print("После уменьшения:", counter1.value)

counter2 = Counter(10)
print("Начальное значение counter2:", counter2.value)
counter2.less()
print("После уменьшения:", counter2.value)
counter2.more()
print("После увеличения:", counter2.value)