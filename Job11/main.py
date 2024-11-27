def time_to_text(minutes):
    heures = minutes // 60
    minutesSimple = minutes % 60
    print(f"{heures} heures et {minutesSimple} minutes")

minutes = int(input("Rentrez un nombre qu'en minutes (exemple : 232) : "))

time_to_text(minutes)