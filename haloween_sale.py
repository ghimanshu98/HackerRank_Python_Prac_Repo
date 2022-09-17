def howManyGames(p, d, m, s):
    # Return the number of games you can buy
    bill = 0
    item = 0
    last_item = 0
    while(bill <= s):
        if item == 0:
            last_item = p
            bill = bill + p
            item += 1
        elif last_item <= m:
            last_item = last_item -d
            bill = bill + last_item
        elif last_item > m:
            bill = bill + m

    return item

print(howManyGames(20,3,6,70))
        
