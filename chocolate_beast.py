def helper(wrapper, wrappers_required):
    if wrappers_required <= wrapper:
        bar_got = int(wrapper/wrappers_required)
        wrappers_left = wrapper - (bar_got*wrappers_required)
        wrappers_left = bar_got+wrappers_left
        if wrappers_left >= wrappers_required:
            return bar_got + helper(wrappers_left, wrappers_required)
        else:
            return bar_got
    else:
        return 0

def chocolateFeast(money, bar_cost, wrappers_required):
    # Write your code here
    bar_bought = 0
    if money > bar_cost:
        bar_bought = int(money/bar_cost)
        return bar_bought + helper(bar_bought, wrappers_required)
    else:
        return 0
    
print(chocolateFeast(15,3,2))