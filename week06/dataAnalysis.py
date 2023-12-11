
# Allow the user to type in a year, then, find the average life expectancy for that year. Then find the country with the minimum and the one with the maximum life expectancies for that year.

lowest_expectancy = float(999)
highest_expectancy = float(1)
country = ''
lowest_country_year = 2500
highest_country_year = 1000
selected_year = 1000
count = 0
sum_age = 0
average_age = 0
highest_expec = 0
lowest_expec = 100
result_country1 = ''
result_country2 = ''

with open("life_expectancy.csv") as life:
    selected_year = int(input("Choose an year: "))
    next(life)
    for line in life:
        
        parts = line.split(",")

        entity = parts[0]
        cod = parts[1]
        year = int(parts[2])
        expectancy = float(parts[3])

        # print(f"{entity} - {cod} - {year} - {expectancy}")
        # lowest life expectancy
        if lowest_expectancy > expectancy:
            lowest_expectancy = expectancy
            lowest_country_year = year
            country = entity

        # hinghest life expectancy
        if highest_expectancy < expectancy:
            highest_expectancy = expectancy
            highest_country_year = year
            country = entity

        # average life expectancy for $selected_year
        if year == selected_year:
            sum_age = sum_age + expectancy
            count += 1
            # max and min values for $selected_year
            if expectancy > highest_expec:
                highest_expec = expectancy
                result_country1 = entity
            if expectancy < lowest_expec:
                lowest_expec = expectancy
                result_country2 = entity

    # year and country that has the lowest life expectancy
    print("# LOWEST LIFE EXPECTANCY #")
    print(f"COUNTRY: {country} - YEAR: {lowest_country_year}\n")

    # year and country that has the highest life expectancy
    print("# HIGHEST LIFE EXPECTANCY #")
    print(f"COUNTRY: {country} - YEAR: {highest_country_year}\n")

    # average of years for life expectancy == $selected_year
    average_age = sum_age/count
    print(f"# AVERAGE LIFE EXPECTANCY FOR {selected_year} #")
    print(f"AVERAGE IN THE WORLD - {'%2f' % average_age}\n")

    # max and min of years for life expectancy == $selected_year
    print(f"# MAX & MIN LIFE EXPECTANCY FOR {selected_year} #")
    print(f"The max life expectancy was in {result_country1} with - {highest_expec}")
    print(f"The min life expectancy was in {result_country2} with {lowest_expec}")