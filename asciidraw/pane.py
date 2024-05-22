class ASCIIPane:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.pane = [[" " for _ in range(width)] for _ in range(height)]

    def __str__(self):
        return "\n".join(["".join(row) for row in self.pane])

    def __getitem__(self, key):
        return self.pane[key]

    def __setitem__(self, key, value):
        self.pane[key] = value
