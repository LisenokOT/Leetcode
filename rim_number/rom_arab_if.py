def arabToRom(arab):
    arab = int(arab)
    a = ""
    if (arab // 1000 != 0):
        a += "M" * int(arab / 1000)
        arab = arab % 1000
    if (arab // 900 != 0):
        a += "CM"
        arab = arab % 900
    if (arab // 500 != 0):
        a += "D" * int(arab / 500)
        arab = arab % 500
    if (arab // 400 != 0):
        a += "CD"
        arab = arab % 400
    if (arab // 100 != 0):
        a += "C" * int(arab / 100)
        arab = arab % 100
    if (arab // 90 != 0):
        a += "XC"
        arab = arab % 90
    if (arab // 50 != 0):
        a += "L" * int(arab / 50)
        arab = arab % 50
    if (arab // 40 != 0):
        a += "XL"
        arab = arab % 40
    if (arab // 10 != 0):
        a += "X" * int(arab / 10)
        arab = arab % 10
    if (arab // 9 != 0):
        a += "IX"
        arab = arab % 9
    if (arab // 5 != 0):
        a += "V" * int(arab / 5)
        arab = arab % 5
    if (arab // 4 != 0):
        a += "IV"
        arab = arab % 4
    a += "I" * int(arab / 1)
    return a


def main():
    print(arabToRom(3))


if __name__ == ("__main__"):
    main()