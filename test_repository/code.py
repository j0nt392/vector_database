class Vector:
    """
    Represents a 3-dimensional vector with x, y, and z coordinates.
    """

    def __init__(self, x_coordinate, y_coordinate, z_coordinate):
        """
        Initializes a Vector object with x, y, and z coordinates.

        Parameters:
            x_coordinate (int or float): The x coordinate of the vector.
            y_coordinate (int or float): The y coordinate of the vector.
            z_coordinate (int or float): The z coordinate of the vector.

        Raises:
            TypeError: If any of the input values is not an integer or float.
        """
        if isinstance(x_coordinate, (int, float)) and isinstance(y_coordinate, (int, float)) and isinstance(z_coordinate, (int, float)):
            self.x = x_coordinate
            self.y = y_coordinate
            self.z = z_coordinate
        else:
            raise TypeError("Input values for x, y, and z must be integers or floats.")

    def __str__(self):
        """
        Returns a string representation of the vector.

        Returns:
            str: A string representation of the vector in the format (x, y, z).
        """
        return f"({self.x}, {self.y}, {self.z})"

    def magnitude(self):
        """
        Calculates the magnitude of the vector.

        Returns:
            float: The magnitude of the vector.
        """
        return (self.x ** 2 + self.y ** 2 + self.z ** 2) ** 0.5


vector_1 = Vector(1, 2, 3)
vector_2 = Vector(4, 5, 6)
vector_3 = Vector(-1, -2, -3)

print("Vector 1:", vector_1)
print("Vector 2:", vector_2)
print("Vector 3:", vector_3)

vector_list = [vector_1, vector_2, vector_3]

print("Vector list:", [vector for vector in vector_list])

for vector in vector_list:
    print(f"The magnitude of {vector} is {vector.magnitude()}").