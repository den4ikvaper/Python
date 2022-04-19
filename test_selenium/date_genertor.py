from datetime import datetime, date, timedelta

for i in range(1095):
    date_time = (date(1997, 1, 1) + timedelta(days=i)).strftime("%Y.%m.%d")
    with open("birthday_dates.txt", mode="a") as file:
        file.write(f"{date_time}\n")
