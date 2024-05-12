class Vector:
    """
    This class represents a 3-dimensional vector with x, y, z components.
    """

    def __init__(self, x, y, z):
        """
        Initializes a Vector object with given x, y, z components.
        :param x: x component of the vector
        :param y: y component of the vector
        :param z: z component of the vector
        """
        # Check if the input values are valid
        if isinstance(x, (int, float)) and isinstance(y, (int, float)) and isinstance(z, (int, float)):
            self.x = x
            self.y = y
            self.z = z
        else:
            raise TypeError("Input values must be numeric")

    def __str__(self):
        """
        Returns a string representation of the vector in the format (x, y, z).
        :return: string representation of the vector
        """
        return f"({self.x}, {self.y}, {self.z})"

    def magnitude(self):
        """
        Calculates the magnitude of the vector.
        :return: magnitude of the vector
        """
        return (self.x ** 2 + self.y ** 2 + self.z ** 2) ** 0.5


# Create three vectors
vector_1 = Vector(1, 2, 3)
vector_2 = Vector(4, 5, 6)
vector_3 = Vector(-1, -2, -3)

# Print the vectors
print("Vector 1:", vector_1)
print("Vector 2:", vector_2)
print("Vector 3:", vector_3)

# Create a list of vectors
vector_list = [vector_1, vector_2, vector_3]

# Print the list of vectors
print("Vector list:", [vector for vector in vector_list])

# Print the magnitude of each vector
for vector in vector_list:
    print(f"The magnitude of {vector} is {vector.magnitude()}")