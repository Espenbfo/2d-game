class Color:
    def __init__(self, r, g, b, raw=False):
        if not raw:
            self.r = r / 255
            self.g = g / 255
            self.b = b / 255
        else:
            self.r = r
            self.g = g
            self.b = b
        self.clamp()

    def rgb(self):
        return int(self.r * 255), int(self.g * 255), int(self.b * 255)

    def rgb_raw(self):
        return self.r, self.g, self.b

    def lighten(self, degree):
        return Color(
            self.r * degree,
            self.g * degree,
            self.b * degree,
            True)

    def gamma(self, degree):
        return Color(
            self.r + degree,
            self.g + degree,
            self.b + degree,
            True)

    def clamp(self):
        self.r = min(1, max(0, self.r))
        self.g = min(1, max(0, self.g))
        self.b = min(1, max(0, self.b))
