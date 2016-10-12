import smtplib

server = smtplib.SMTP( "smtp.gmail.com", 587 )
server.starttls()
server.login('trond.skogland@gmail.com','Aft1post123')
server.sendmail('trond.skogland@gmail.com','ts@atea.no','Hello!')
