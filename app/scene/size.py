class Size(object):
    def __init__(self, width, height):
        self.__height = height
        self.__width = width

    def width(self):
        return self.__width

    def height(self):
        return self.__height

    def tuple(self):
        return self.width(), self.height()
