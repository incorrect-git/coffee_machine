class Sphere:
    # finish class Sphere here
    PI = 3.1415
    volume = 0

    def __init__(self, radius):
        self.radius = radius
        self.volume = (4 / 3) * self.PI * pow(self.radius, 3)
