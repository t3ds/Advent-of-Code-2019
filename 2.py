def restore(intcode,j,k):
    intcode[1] = j
    intcode[2] = k
    for i in range(0, len(intcode), 4):
        #print(i,intcode[i+1],intcode[i+2],intcode[intcode[i + 1]],intcode[intcode[i + 2]])
        if intcode[i] == 1:
            #print(1)
            intcode[intcode[i + 3]] = intcode[intcode[i + 1]] + intcode[intcode[i + 2]]


        if intcode[i] == 2:
            #print(2)
            intcode[intcode[i + 3]] = intcode[intcode[i + 1]] * intcode[intcode[i + 2]]
            

        if intcode[i] == 99:
            #print(99)
            break
    return intcode[0]
if __name__ == "__main__":

    intcode = list(map(int,input().split(',')))

    #Part 1: Restore
    print(restore(intcode[:],12,2))

    #Part 2: Producing Desired Input

    score = 19690720
    for i in range(0,100):
        for j in range(0,100):
            if restore(intcode[:],i,j) == score:
                print(100*i+j)
