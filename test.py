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
		# create_email().get('email')
		
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

# import asyncio
# import logging
# from xtempmail.aiomail import EMAIL, EmailMessage, Email
# log = logging.getLogger('xtempmail')
# log.setLevel(logging.INFO)
# app = Email(name='krypton', ext=EMAIL.MAILTO_PLUS)
# @app.on.message()
# async def baca(data: EmailMessage):
#     print(f"\tFrom: {data.from_mail}\n\tSubject: {data.subject}\n\tBody: {data.text}\n\tReply -> Delete")
#     ok = []
#     for i in data.attachments: # -> Forward attachmen
#         ok.append(( i.name, await i.download()))
#     if data.from_is_local:
#         await data.from_mail.send_message(data.subject, data.text, multiply_file=ok) # -> Forward message
#     await data.delete()  #delete message

# @app.on.message(lambda msg:msg.attachments)
# async def get_message_media(data: EmailMessage):
#     print(f'Attachment: {[i.name for i in data.attachments]}')

# @app.on.message(lambda x:x.from_mail.__str__().endswith('@gmail.com'))
# async def getGmailMessage(data: EmailMessage):
#     print(f'Gmail: {data.from_mail}')

# if __name__ == '__main__':
#     try:
#         loop = asyncio.new_event_loop()
#         loop.run_until_complete(app.listen())
#     except Exception:
#         asyncio.run(app.destroy())