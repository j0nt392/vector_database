class NumberSquare:
    def __init__(self, number):
        self.number = number

    def calculate_square(self):
        return self.number ** 2
    def print_square(self):
        print(f"The square of {self.number} is {self.calculate_square()}")

# Instantiate the class
num_square = NumberSquare(5)

# Do something with the instance
num_square.print_square()