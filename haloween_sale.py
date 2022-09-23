def howManyGames(first_item_cost, discount, m, spendable_money):
    # Return the number of games you can buy
    if spendable_money >= first_item_cost:
        bill = 0
        item = 0
        next_item_cost = 0
        while(bill < spendable_money):
            if item==0: # first item
                item += 1
                bill = bill + first_item_cost
                next_item_cost = first_item_cost - discount
                print(first_item_cost)
            elif next_item_cost > m:
                bill = bill + next_item_cost
                if bill <= spendable_money:
                    item += 1
                    print(next_item_cost)
                next_item_cost = next_item_cost - discount
            elif next_item_cost <= m:
                bill = bill +m
                if bill <= spendable_money:
                    item += 1
                    print(m)
        return item
    else:
        return 0

# print(howManyGames(20,3,6,85))
print(howManyGames(100,19,1,180))