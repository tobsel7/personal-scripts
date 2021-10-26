from datetime import date, timedelta

today = date.today()

f = open("./reminder_next_date.txt", "r+")
next_reminder_date = date.fromisoformat(f.read().strip())
print(next_reminder_date > today)
next_week = today + timedelta(days=7)
f.write(str(next_week))
