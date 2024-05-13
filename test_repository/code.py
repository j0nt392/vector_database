
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
        """
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        """ Returns a string representation of the vector. """

        return "({0}, {1}, {2})".format(self.x, self.y, self.z)

    def magnitude(self):
        """
        Calculates the magnitude of the vector.

        Returns:
            float: The magnitude of the vector.
        """
        return sum([x ** 2 for x in (self.x, self.y, self.z)]) ** 0.5

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
    print("The magnitude of {} is {:.2f}".format(vector, vector.magnitude()))