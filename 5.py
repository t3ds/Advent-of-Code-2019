
def restore(intcode, j, k):
    #intcode[1] = j
    #intcode[2] = k
    i = 0
    while i < len(intcode):
        # print(i,intcode[i+1],intcode[i+2],intcode[intcode[i + 1]],intcode[intcode[i + 2]])
        curr = '{:0>4}'.format(str(intcode[i]))
        #if len(curr) < 4:
            #curr = "000" + curr

        if curr[2:4] != '03' or curr[2:4] != '04':
            if curr[1] == '0':
                a = intcode[intcode[i+1]]

            else:
                a = intcode[i+1]

            if curr[0] == '0':
                #print("code: " + str(intcode[i]) + " " + str(intcode[i+2]))
                b = intcode[intcode[i+2]]

            else:
                b = intcode[i+2]

        if curr[2:4] == '01':
            # print(1)
            intcode[intcode[i + 3]] = a + b
            i += 4

        if curr[2:4] == '02':
            # print(2)
            intcode[intcode[i + 3]] = a * b
            i += 4

        if curr[2:4] == '03':
            x = int(input("Opcode 3. Please Input Value"))
            intcode[intcode[i+1]] = x
            i += 2

        if curr[2:4] == '04':
            print(str(intcode[intcode[i+1]]))
            i += 2

        if curr[2:4] == '05':
            if a != 0:
                #print("b: " + str(b))
                i = b

            else:
                i += 3

        if curr[2:4] == '06':
            if a == 0:
                i = b

            else:
                i += 3

        if curr[2:4] == '07':
            if a < b:
                intcode[intcode[i+3]] = 1

            else:
                intcode[intcode[i + 3]] = 0

            i += 4

        if curr[2:4] == '08':
            if a == b:
                intcode[intcode[i + 3]] = 1

            else:
                intcode[intcode[i + 3]] = 0

            i += 4

        if curr[2:4] == 99:
            # print(99)
            break

        #print(str(i) + " " + str(intcode[i]))
    #return intcode[0]


if __name__ == "__main__":

    id = int(input())
    if id == 0:
        intcode = list(map(int, input().split(',')))

    elif id == 1:
        code = open('5_input.txt', 'r').readlines()
        for line in code:
            intcode = [int(num) for num in line.split(',')]


    #print(intcode)
    restore(intcode[:],0,0)
    # Part 1: Restore
    #print(restore(intcode[:], 0, 0))

    # Part 2: Producing Desired Input

    """score = 19690720
    for i in range(0, 100):
        for j in range(0, 100):
            if restore(intcode[:], i, j) == score:
                print(100 * i + j)"""
