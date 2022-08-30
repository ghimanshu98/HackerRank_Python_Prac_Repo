def saveThePrisoner(prisioner, toffee, chair):
    # Write your code here
    rounds = int(toffee/prisioner)
    toffee = toffee - rounds*prisioner
    if toffee==0 and chair == 1:
        return prisioner
    elif prisioner-chair+1 < toffee:
        temp = prisioner-chair+1
        toffee = toffee - temp
        return toffee
    else:
        return chair+toffee-1

# result = saveThePrisoner(94431605, 679262176, 5284458)
print(saveThePrisoner(11, 32020900, 6))
# result = saveThePrisoner(999999998, 999999998, 1)
result = saveThePrisoner(5, 2, 1)
print(str(result) + '\n')