months = {
        "January": 1,
        "February": 2,
        "March": 3,
        "April": 4,
        "May": 5,
        "June": 6,
        "July": 7,
        "August": 8,
        "September": 9,
        "October": 0,
        "November": 11,
        "December": 12
        }

while True:
    user_input = input("Date: ")

    try:
        month, day, year = user_input.split(sep='/')

        month = int(month)
        day = int(day)
        year = int(year)

        if 0 < month <= 12 and 0 < day <= 31:
            print(f"{year}-{month:02}-{day:02}")
            break
        else:
            continue

    except ValueError:
        month_day, year = user_input.split(sep=',')
        year = year.lstrip()
        month, day = month_day.split()
    
        month = months[month]
        year = int(year)
        day = int(day)
        
        if 0 < day <= 31:
            print(f"{year}-{month:02}-{day:02}")
            break
        else:
            continue


