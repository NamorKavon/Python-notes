from datetime import datetime, date

age = date.today()-date(1996,9,17)

print(age.days)

days = (age.days)  

years = days / 365  

print("Number of years is: ");  

print(years)
