
def checkCases(num):

    num_str = str(num)
    adj = 0
    flag = 0
    temp = num_str[0]
    rep_count = 0

    for i in range(len(num_str)):

        if adj != 1:
            if num_str[i] == temp:
                rep_count += 1

            else:
                if rep_count == 2:
                    adj = 1

                else:
                    rep_count = 1
                    temp = num_str[i]

        #if i > 0 and num_str[i] == num_str[i-1]:
            #adj = 1
            #temp = num_str[i]

            #if (i<len(num_str)-1 and num_str[i] == num_str[i+1]) or (i == len(num_str)-1 and num_str[i] == num_str[i-2]):
                #adj = 0

        if i < len(num_str)-1 and num_str[i] > num_str[i+1]:
            flag = 1
            break

    if rep_count == 2:
        adj = 1
    if adj == 0 or flag == 1:
        return False

    else:
        return True


if __name__ == "__main__":

    #PUZZLE INPUT: 234208-765869

    x, y = input().strip().split('-')
    solutions = 0
    for num in range(int(x), int(y)+1):
        #print('hello')
        if checkCases(num):
            solutions += 1

    print(solutions)