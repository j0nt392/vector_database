# Define a Vector class to represent 3-dimensional vectors
class Vector:
    """
    A class to represent 3-dimensional vectors.

    Attributes:
        x (float): The x-coordinate of the vector.
        y (float): The y-coordinate of the vector.
        z (float): The z-coordinate of the vector.
    """

    def __init__(self, x, y, z):
        """
        Initialize a Vector object with given x, y, and z coordinates.

        Parameters:
            x (float): The x-coordinate of the vector.
            y (float): The y-coordinate of the vector.
            z (float): The z-coordinate of the vector.
        """
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        """
        Return a string representation of the vector.

        Returns:
            str: A string representing the vector in the format (x, y, z).
        """
        return f"({self.x}, {self.y}, {self.z})"


# Create some test vectors
v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)
v3 = Vector(-1, -2, -3)

# Print the vectors
print(v1)
print(v2)
print(v3)

# Add more vectors to the vector database
vector_list = [v1, v2, v3]

# Iterate over the vectors and print them
for vector in vector_list:
    print(vector)