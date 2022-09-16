def taumBday(b, w, bc, wc, z):
    # Write your code here
    bg_cost = 0
    wg_cost = 0
    if bc > wc+z:
        bg_cost = b*(wc+z)
    elif bc <= wc+z:
        bg_cost = b*bc
    if wc > bc+z:
        wg_cost = (bc+z)*w
    elif wc<= bc+z:
        wg_cost = wc*w
    
    return bg_cost+wg_cost

# print(taumBday(3,5,3,4,1))
print(taumBday(7,7,4,2,1))