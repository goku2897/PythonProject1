class AreaReact:
    def __init__(self,l,b):
        self.l = l
        self.b = b

    def calculate_Area(self):
        return self.l * self.b


area1 = AreaReact(10,20)
area2 = AreaReact(30,40)

area1.calculate_Area()
print(area1.calculate_Area())