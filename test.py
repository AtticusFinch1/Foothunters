from minuteinbox import create_email, get_inbox
from bs4 import BeautifulSoup
from time import sleep as s
import re
class verify_email():
	def create_new_email():
		minuteinbox = create_email()
		if minuteinbox:
			email = minuteinbox.get('email')
			first_name = minuteinbox.get('fname')
			last_name = minuteinbox.get('lname')
			company_name = minuteinbox.get('company')
			print('Current E-Mail: '+email+'\n'+'First & Last Name: '+first_name+' '+last_name+'\n'+'Company Name: '+company_name)
		# 2nd short way
		create_email().get('email')

		# get received email body
		while True:
			inbox = get_inbox()
			if inbox != None:
				subject = inbox.get('subject')
				sender = inbox.get('sender')
				raw_body = inbox.get('raw_body') # raw text body
				clean_body = inbox.get('clean_body') # bs4 parsed body
				print('\nNew E-Mail titled: "'+subject+'", from: '+sender)
				print('\n'+'E-Mail Body:'+'\n'+clean_body)
				regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
				url = re.findall(regex,clean_body)      
				result = [x[0] for x in url]
				return result
				print(result)
				break
			s(3)

e = verify_email
e.create_new_email()