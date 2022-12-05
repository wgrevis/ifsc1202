import math

def angle(a, b, c):
    #inner = pow(a, 2) + pow(b, 2) + pow(c, 2)
    #inner = inner / (2 * b * c)
    inner = c ** 2 - b ** 2 - a ** 2
    inner = inner / (-2.0 * a * b)
    return math.acos(inner) * (180 / math.pi) 




class Triangle():
    def __init__(self, s1, s2, s3):
        self.s1 = s1
        self.s2 = s2
        self.s3 = s3

    def Type(self):
        if self.s1 == self.s2 and self.s1 == self.s3:
            return "Equailateral"
        elif self.s1 == self.s2 or self.s1 == self.s3:
            return "Isocelese"
        else:
            return "Scalene"

    def Perimeter(self):
        return self.s1 + self.s2 + self.s3

    def Area(self):
        s = self.Perimeter() / 2
        return math.sqrt(s*(s - self.s1)*(s - self.s2)*(s - self.s3))

    def Angles(self):
        angles = []
        angles.append(angle(self.s1, self.s2, self.s3))
        angles.append(angle(self.s2, self.s1, self.s3))
        angles.append(angle(self.s3, self.s1, self.s2))
        return angles



print("{:<15}{:<15}{:<15}{:<15}{:<15}{:<15}{:<15}{:<15}{:<15}".format("Type", "Side 1", "Side 2", "Side 3", "Perimeter", "Area", "Angle 1", "Angle 2","Angle 3"))
file = open("Exam Three Triangles.txt" , 'r')
lines = file.readlines()

TriangleList = []

for line in lines:
    line = line.strip().split(",")
    line[0] = float(line[0])
    line[1] = float(line[1])
    line[2] = float(line[2])
    triangle = Triangle(line[0],line[1],line[2])
    TriangleList.append(triangle)
for triangle in TriangleList:
    print("{:<15}{:<15}{:<15}{:<15}{:<15}{:<15}{:<15}{:<15}{:<15}".format(triangle.Type(),triangle.s1 , triangle.s2, triangle.s3, triangle.Perimeter(), triangle.Area(), triangle.Angles()[0],triangle.Angles()[1], triangle.Angles()[2]))



file.close()