import math

def diameter(radius):
    return float(radius) * 2
def circumference(radius):
    return 2 * math.pi * float(radius)
def area(radius):
    return math.pi * (float(radius) * float(radius))

radiusFile = open("06.01 Radius.txt","r")
radius = radiusFile.readline().strip()

print("{:>15} {:>15} {:>15} {:>15}".format("Radius","Diameter","Circumference","Area"))

while radius != "":
    print("{:>15.5f} {:>15.5f} {:>15.5f} {:>15.5f}".format(float(radius),diameter(radius),circumference(radius),area(radius)))
    radius = radiusFile.readline().strip()