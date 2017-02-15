#!/usr/bin/env python
import csv
import html
import cgi
import cgitb; cgitb.enable()     # for troubleshooting

form = cgi.FieldStorage() # open form, get its values

user_first_name  = html.escape(form["user_first_name"].value);
user_last_name   = html.escape(form["user_last_name"].value);
user_mail = html.escape(form["user_mail"].value);
user_phone = html.escape(form["user_phone"].value);

with open('cooldemocrats.csv', 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({'first_name': user_first_name, 'last_name': user_last_name, 'email': user_mail, 'phone': user_phone})

###########################################################