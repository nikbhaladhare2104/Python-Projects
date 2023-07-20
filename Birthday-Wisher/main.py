import smtplib

my_email = "nikbhaladhare2104@gmail.com"
password = "sksgjywmkixlkcdd"

with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs="nihalsodhi112000@gmail.com",
        msg="Subject:Hello\n\nThis is the body of the mail."
    )
