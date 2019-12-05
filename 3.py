

def plot(wire):
    x = 0
    y = 0
    iter = 0

    points = {}

    for step in wire:
        direction,distance = step[0], int(step[1:])

        for point in range(distance):

            if direction == "U":
                y += 1

            if direction == "L":
                x += 1

            if direction == "R":
                x += -1

            if direction == "D":
                y += -1

            iter += 1
            points[(x, y)] = iter

    return points


def findIntersections(path1,path2):
    return (set(path1.keys())) & (set(path2.keys()))


def manhattenDist(points):
    return [abs(x) + abs(y) for x,y in points]


def getLeast(path1,path2,intersections):
    return [path1[point] +  path2[point] for point in intersections]
if __name__ == "__main__":

    wires = open('3_input.txt', 'r').readlines()
    wire1 = wires[0].split(',')
    wire2 = wires[1].split(',')

    wire1_path = plot(wire1)
    wire2_path = plot(wire2)

    intersections = findIntersections(wire1_path, wire2_path)

    #PART 1:

    print(min(manhattenDist(intersections)))

    #PART 2:

    print(min(getLeast(wire1_path,wire2_path,intersections)))