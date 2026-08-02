import smtplib
import datetime as dt
import random
import pandas

my_email = os.environ.get("MY_EMAIL")
my_password = os.environ.get("MY_PASSWORD")

data = pandas.read_csv("birthdays.csv")
birthdays = data.to_dict(orient="records")

date_today = dt.datetime.now()

for record in birthdays:
    if int(record["month"]) == date_today.month and int(record["day"]) == date_today.day:
        random_number = random.randint(1,3)
        with open(f"letter_templates/letter_{random_number}.txt", "r") as file:
            msg = file.read()
            msg = msg.replace("[NAME]", record["name"])
        with smtplib.SMTP('smtp.gmail.com', 587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_password)
            connection.sendmail(from_addr=my_email, to_addrs=record["email"],
                                msg=f"Subject:Warm Birthday Wishes!\n\n{msg}")

