def day_256th_of_year(year):
    if (year>=1700) and (year <=1917):
        # follow julian calendar
        l = [31,28,31,30,31,30,31,31,30,31,30,31] # index+1represents the month number
        days = 0
        month = 0
        
        leap_year = False
        if (year%4==0):
            leap_year = True
        
        leap_day_added = False
        
        while(days<=256):  # finds month
            if(leap_year== True) and (leap_day_added == False): # it's a leap year
                days = days + l[month] + 1 # plus 1 for feb
                leap_day_added = True
            else:
                days = days + l[month]
            month = month+1

        temp = 0
        for i in range(month-1):
            temp = temp + l[i]

        if leap_year:
            temp = temp+1
        
        date = 256 - temp

        if (date<10):
            date = '0'+str(date)  
        
        if (month<10):
            month = '0'+str(month)
        print('{}.{}.{}'.format(date, month, year))
        
    elif (year == 1918):
        # transistion to gregorian
        l = [31,15,31,30,31,30,31,31,30,31,30,31]
        days = 0
        month = 0        
        while(days<=256):  # finds month
            days = days + l[month]
            month = month+1

        temp = 0
        for i in range(month-1):
            temp = temp + l[i]

        date = 256 - temp  
        if (date<10):
            date = '0'+str(date)  
        
        if (month<10):
            month = '0'+str(month)
        print('{}.{}.{}'.format(date, month, year))

    else:
        # gregorian
        l = [31,28,31,30,31,30,31,31,30,31,30,31] # index+1represents the month number
        days = 0
        month = 0
        
        leap_year = False
        if (year%400==0) or (year%4==0 and year%100!=0):
            leap_year = True
        
        leap_day_added = False
        
        while(days<=256):  # finds month
            if(leap_year== True) and (leap_day_added == False): # it's a leap year
                days = days + l[month] + 1 # plus 1 for feb
                leap_day_added = True
            else:
                days = days + l[month]
            month = month+1

        temp = 0
        for i in range(month-1):
            temp = temp + l[i]

        if leap_year:
            temp = temp+1
        
        date = 256 - temp  
        if (date<10):
            date = '0'+str(date)  
        
        if (month<10):
            month = '0'+str(month)
        
        print('{}.{}.{}'.format(date, month, year))
    
day_256th_of_year(2017)
day_256th_of_year(2016)
day_256th_of_year(1800)
day_256th_of_year(1918)