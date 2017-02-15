#!/usr/bin/env python
import csv
import html
import cgi
import cgitb; cgitb.enable()     # for troubleshooting

print("Content-Type: text/html") # HTTP header to say HTML is following
print()                          # blank line, end of headers

form = cgi.FieldStorage() # open form, get its values

#say  = html.escape(form["say"].value);
#to   = html.escape(form["to"].value);
user_first_name  = html.escape(form["user_first_name"].value);
user_last_name   = html.escape(form["user_last_name"].value);
user_mail = html.escape(form["user_mail"].value);
user_phone = html.escape(form["user_phone"].value);
#print(say, " ", to)


with open('cooldemocrats.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=' ',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    spamwriter.writerow(['Spam'] * 5 + ['Baked Beans'])
    spamwriter.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])



###########################################################