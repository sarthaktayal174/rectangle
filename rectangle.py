class Rectangle:
    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width

    def __iter__(self):
        # Yields length in the specified dictionary format
        yield {'length': self.length}
        # Yields width in the specified dictionary format
        yield {'width': self.width}


# Example Usage:
rectangle = Rectangle(length=10, width=5)
for dimension in rectangle:
    print(dimension)
