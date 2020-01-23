time = 705

place_of_work = "Salford"
town_of_home = "Bury"
commute = "Commuting"

if time >= 900:
    print(place_of_work)
elif time >= 800 and time <= 900:
    print(commute)
elif time >= 700 and time <= 800:
    print(town_of_home)