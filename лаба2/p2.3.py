class Numbers:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def show(self):
        print("Число a:", self.a)
        print("Число b:", self.b)

    def change(self, new_a, new_b):
        self.a = new_a
        self.b = new_b

    def sum(self):
        return self.a + self.b

    def max_value(self):
        return max(self.a, self.b)

nums = Numbers(3, 7)
nums.show()
print("Сумма:", nums.sum())
print("Максимум:", nums.max_value())

nums.change(10, 2)
nums.show()
print("Сумма:", nums.sum())
print("Максимум:", nums.max_value())