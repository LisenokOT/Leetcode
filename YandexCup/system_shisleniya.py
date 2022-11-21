def convert(temp):
    if temp == "+" or temp == "-":
        return 0
    if ord(temp)>=65:
        return ord(temp)-55
    return int(temp)

def mathem(left, right, ss):
    if len(left) == 1:
        temp = left
    else:
        if left[1] == "+":
            temp = int(left[0]) + int(left[2])
            if temp[0]==ss:
                temp[0]-ss
                temp[1]+=1


def main():
    left, right = map(str, input().split(" = "))
    left = left.split()
    right = right.split()
    ss = (max([convert(elem) + 1 for i in left + right for elem in i]))
    #mathem(left, right, ss)
    print (left[0][-1:])

if __name__ == "__main__":
    main()