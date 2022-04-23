import smtplib
from datetime import date, timedelta
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def get_progress_characters(progress):
    progress_char = '▄'
    non_progress_char = '▁'
    progress_perc = progress * 100
    progress_steps = int(progress_perc / 10) + 1
    progress_string = ""

    for i in range(0, 11):
        added_char = progress_char if i < progress_steps else non_progress_char
        progress_string = progress_string + added_char
    progress_string = progress_string + " " + str(int(progress_perc)) + "%"
    return progress_string


def create_message():
    return_date = date(2021, 12, 18)
    starting_date = date(2021, 8, 27)
    today_date = date.today()
    days_total = (return_date - starting_date).days
    days_remaining = (return_date - today_date).days
    days_passed_by = (today_date - starting_date).days
    progress = float(days_passed_by) / days_total
    return "Hello my cutie,\n\n" + \
           "this is a quick update on the progress concerning my return.\n\n" + \
           "Already " + str(days_passed_by) + " days passed by, since we saw each other the last time.\n" + \
           "There are still " + str(days_remaining) + " days to go. \n" + \
           "Progress: " + get_progress_characters(progress) + "\n\n" + \
           "I love you. \n\n" + \
           "Tobi"


def check_next_reminder_date():
    reminder_date_file = open("./reminder_next_date.txt", "r")
    next_reminder_date = date.fromisoformat(reminder_date_file.read().strip())
    today_date = date.today()
    reminder_date_file.close()
    return next_reminder_date <= today_date


def update_reminder_file():
    today_date = date.today()
    next_week = today_date + timedelta(days=7)
    reminder_date_file = open("./reminder_next_date.txt", "w")
    reminder_date_file.write(str(next_week))
    reminder_date_file.close()


def send_reminder():
    msg = MIMEMultipart("alternative")
    msg['From'] = "your-email@hotmail.com"
    msg['To'] = "your-loved-ones-email@email.com"
    msg['Subject'] = "Any subject"
    text = MIMEText(create_message(), "plain")
    msg.attach(text)

    s = smtplib.SMTP("smtp.live.com", 587) # change this to the smtp server of your email service
    s.ehlo()
    s.starttls()
    s.ehlo()
    s.login('your-login@hotmail.com', 'your-passowrd')

    s.sendmail("your-email@hotmail.com", "your-loved-ones-email@email.com", msg.as_string())
    s.quit()
    update_reminder_file()


def main():
    if check_next_reminder_date():
        send_reminder()


if __name__ == "__main__":
    main()
