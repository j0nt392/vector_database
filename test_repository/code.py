class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"

# Create some test vectors
v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)
v3 = Vector(-1, -2, -3)

# Print the vectors
print(v1)
print(v2)
print(v3)

# Add more vectors to the database
vectors = [v1, v2, v3]

# Iterate over the vectors and print them
for vector in vectors:
    print(vector)