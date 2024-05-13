class Vector:
    """ Represents a 3-dimensional vector with x, y, and z coordinates. """

    def __init__(self, x, y, z):
        """
        Initializes a Vector object with x, y, and z coordinates.

        Parameters:
            x (int or float): The x coordinate of the vector.
            y (int or float): The y coordinate of the vector.
            z (int or float): The z coordinate of the vector.

        Raises:
            TypeError: If any of the input values is not an integer or float.
        """
        try:
            if isinstance(x, (int, float)) and isinstance(y, (int, float)) and isinstance(z, (int, float)):
                self.x = x
                self.y = y
                self.z = z
            else:
                raise TypeError("Input values for x, y, and z must be integers or floats.")
        except TypeError as e:
            print(f"Error initializing Vector: {e}")

    def __str__(self):
        """
        Returns a string representation of the vector.

        Returns:
            str: A string representation of the vector in the format (x, y, z).
        """
        return f"({self.x}, {self.y}, {self.z}) "

    def magnitude(self):
        """
        Calculates the magnitude of the vector.

        Returns:
            float: The magnitude of the vector.
        """
        return pow((self.x ** 2 + self.y ** 2 + self.z ** 2), 0.5)

vector_1 = Vector(1, 2, 3)
vector_2 = Vector(4, 5, 6)
vector_3 = Vector(-1, -2, -3)

print()
print("Vector 1:", vector_1)
print("Vector 2:", vector_2)
print("Vector 3:", vector_3)

vector_list = [vector_1, vector_2, vector_3]

print()
print("Vector list:")
for vector in vector_list:
    print(f"The magnitude of {vector} is {vector.magnitude()}")

