def convert(num):
    if num == 1:
        return "I"
    elif num == 5:
        return "V"
    elif num == 10:
        return "X"
    elif num == 50:
        return "L"
    elif num == 100:
        return "C"
    elif num == 500:
        return "D"
    elif num == 1000:
        return "M"
    return None


def nearNum(num, bias, o_rank):
    answer1 = answer2 = None
    if convert(num) == None and num > 0:
        if bias <= 0 and num <= 1000:
            answer1 = nearNum(num + 1 * o_rank, bias - 1 * o_rank, o_rank)
        if bias >= 0:
            answer2 = nearNum(num - 1 * o_rank, bias + 1 * o_rank, o_rank)
        if answer1 is not None: 
            return answer1 
        return answer2
    else:
        val = bias // 10**(len(str(bias)) - 1)
        answer = convert(num)
        if bias > 3 * o_rank or bias < -1 * o_rank:
            return None
        elif num == 0:
            return ""
        elif bias >= 0:
            if bias != 0:
                return answer + convert(bias // val) * val
            return answer
        return convert(bias // val) + answer
    


def arabToRome(number):
    try:
        if type(int(number)) == int and 0 < int(number) < 4000:
            answer = ""
            count = len(number) - 1
            for num in number:
                answer += nearNum(int(num) * 10**count, 0, 10**(len(str(int(num) * 10**count)) - 1))
                count -= 1
            return answer
        if int(number) >= 4000:
            return "Максимальное число 3999"
        if int(number) < 0:
            return "Минимальное число 0"
        if int(number) == 0:
            return "N"
    except:
        return "Не число"



def main():
    print("Конвертор арабских чисел в римские!\nВведите число:")
    try:
        while True:
            print(arabToRome(input()))
    except:
        pass


if __name__ == "__main__":
    main()

