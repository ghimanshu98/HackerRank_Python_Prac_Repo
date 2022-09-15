def viralAdvertising(days):
    # Write your code here
    day_count = 1
    liked = 0
    cum_liked = 0
    shared = 5
    while(day_count <= days):
        liked = int(shared/2)
        cum_liked = cum_liked + liked
        shared = liked*3
        day_count += 1

    return cum_liked


print(viralAdvertising(5))