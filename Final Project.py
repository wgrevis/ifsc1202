class Sketch():
    def __init__(self, size):
        self.size = size
        self.xpos = 0
        self.ypos = 0
        self.direction = 'U'
        self.pen = 'U'
        self.canvas = []

        for i in range(0, size):
            temp = []

            for x in range(0, size):
                temp.append(' ')
            self.canvas.append(temp)
    def printsketch(self):

        lastRowCol = self.size

        for r in range(-1, lastRowCol):
            for c in range(-1, lastRowCol):
                if r == -1 or r == lastRowCol - 1:
                    if c == -1 or c == lastRowCol - 1:
                        print('+', end='')
                    else:
                        print('-', end='')
                elif c == -1 or c == lastRowCol - 1:
                    print('|', end='')
                else:
                    # print(r, c)
                    print(self.canvas[r][c], end='')
            print()
        print("\nX = {:}  Y = {:}  Direction = {:}".format(self.xpos, self.ypos, self.direction))
    def penup(self):
        self.pen = 'U'
    def pendown(self):
        self.pen = 'D'
    def turnleft(self):
        if self.direction == 'U':
            self.direction = 'L'
        elif self.direction == 'L':
            self.direction = 'D'
        elif self.direction == 'D':
            self.direction = 'R'
        else:
            self.direction = 'U'
    def turnright(self):
        if self.direction == 'U':
            self.direction = 'R'
        elif self.direction == 'R':
            self.direction = 'D'
        elif self.direction == 'D':
            self.direction = 'L'
        else:
            self.direction = 'U'
    def move(self, distance):
        for i in range(0, distance):
            if self.pen == 'D':
                self.canvas[self.xpos][self.ypos] = '*'

            if self.direction == 'U':
                self.xpos += 1
            elif self.direction == 'L':
                self.ypos -= 1
            elif self.direction == 'D':
                self.xpos -= 1
            else:
                self.ypos += 1
            

file = open("CShape.txt", 'r')

line = int(file.readline().strip())

sketch = Sketch(line)

firstTime = True

while line != "":
    if firstTime:
        line = file.readline().strip()
        firstTime = False
        continue

    if ',' in line:
        line = line.split(',')
        distance = int(line[1])

        sketch.move(distance)
    else:
        cmd = int(line)

        if cmd == 1:
            sketch.penup()
        elif cmd == 2:
            sketch.pendown()
        elif cmd == 3:
            sketch.turnright()
        elif cmd == 4:
            sketch.turnleft()
        elif cmd == 6:
            sketch.printsketch()

    line = file.readline().strip()