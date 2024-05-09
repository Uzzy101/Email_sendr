import datetime as dt
import pandas
import random
import smtplib


my_email = 'your_email'
my_password = 'your_password'

today = dt.datetime.now()

today_month = today.month
today_day = today.day

today = (today_month, today_day)

birthdays = pandas.read_csv('birthdays.csv')
birthdays_dict = {(data_row.month, data_row.day): data_row for (index, data_row) in birthdays.iterrows()}

if today in birthdays_dict:
    birthday_boy = birthdays_dict[today]
    rand_number = random.randint(1, 3)
    file_path = f'letter_templates/letter_{rand_number}.txt'
    with open(file_path, mode='r') as letter:
        content = letter.read()
        new_letter = content.replace('[NAME]', birthday_boy['name'])

    email = birthday_boy.email

    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=email,
                            msg=f"Subject:Happy Birthday\n\n{new_letter}",
                            )


