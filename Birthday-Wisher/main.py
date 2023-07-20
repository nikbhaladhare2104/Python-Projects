import smtplib

my_email = "YOUR EMAIL ID"
password = "PASSWORD"

with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs="RECEIVER'S MAIL ID",
        msg="Subject:Hello\n\nThis is the body of the mail."
    )
