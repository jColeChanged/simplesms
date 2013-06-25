#Free SMS Noticiations Via Email#

It turns out that most of the major carriers will allow you to send SMS messages to one of their customers via an <ten digit number>@<carrier domain>. Additional details about this can be found out  on [wikipedia](http://en.wikipedia.org/wiki/List_of_carriers_providing_Email_or_Web_to_SMS). This library has the bare minimum of functionality I needed to set up a program which would send me text messages via email.

#How To Use#

	import simplesms
	email_username = "username"
	email_password = "password"
	phone_number = "1234567890"
	phone_domain = "txt.att.net"

	sms = simplesms.Sms(email_username, email_password, phone_number, phone_domain)
	sms.send("text")
	sms.send("Another text")