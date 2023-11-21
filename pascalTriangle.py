amount = 15
ballAmount = 1
pyramid = [[ballAmount]]

for i in range(amount - 1):
    tI = i + 1
    pyramid.append([])
    for x in range(tI):
        x1 = 0
        if (x - 1 >= 0):
            x1 = pyramid[i][x -1] #/2 for percentages, nothing to get the fraction when added up
        x2 = 0
        if (x < len(pyramid[i])):
            x2 = pyramid[i][x] #/2 for percentages, nothing to get the fraction when added up
        pyramid[tI].append(x1 + x2)
    print(" ".join(str(item) for item in pyramid[tI]) + " Total: " + str(2**i))