def libraryFine(d1, m1, y1, d2, m2, y2):
    # Write your code here
    if y1<y2:
        return 0
    elif y1 == y2:
        if m1<m2:
            return 0
        elif m1 == m2:
            if d1 <= d2:
                # no charge
                return 0
            elif d1 > d2:
                return 15 * (d1-d2)
        elif m1 > m2:
            return 500 * (m1-m2)
    elif y1 > y2:
        return 10000


print(libraryFine(9,6,2015,6,6,2015))