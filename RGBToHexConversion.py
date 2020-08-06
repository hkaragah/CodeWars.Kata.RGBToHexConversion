# RGB To Hex Conversion

def rgb(r, g, b):

    def CheckInput(intake):
        if intake < 0:
            return 0
        elif intake > 255:
            return 255
        else:
            return intake

    def CheckQuotient(intake):
        if intake == 15:
            return "F"
        elif intake == 14:
            return "E"
        elif intake == 13:
            return "D"
        elif intake == 12:
            return "C"
        elif intake == 11:
            return "B"
        elif intake == 10:
            return "A"
        else:
            return str(intake)

    inputList = [r, g, b]
    output = ""

    for item in inputList:

        item = CheckInput(item)
        trail = []
        if item < 10:
            trail.append(item)
            trail.append(0)
        else:
            while item >= 16:
                trail.append(item % 16)
                item = item//16
            trail.append(item)

        for index in range(len(trail)-1, -1, -1):
            output += CheckQuotient(trail[index])

    return output

# Examples:
print(rgb(0,0,0))
print(rgb(255,255,255))










