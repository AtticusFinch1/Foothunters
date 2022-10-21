from Config.config import TestData
from minuteinbox import create_email, get_inbox
from time import sleep as s
import re
import requests


class generalActions():
    def create_new_email():
        minuteinbox = create_email()
        data = {}
        if minuteinbox:
            email = minuteinbox.get('email')
            first_name = minuteinbox.get('fname')
            last_name = minuteinbox.get('lname')
            company_name = minuteinbox.get('company')
            data['email'] = email
            data['first_name'] = first_name
            data['last_name'] = last_name
            data['company_name'] = company_name
            data['password'] = 'password'
            print('Current E-Mail: '+email+'\n'+'First & Last Name: ' +
                  first_name+' '+last_name+'\n'+'Company Name: '+company_name)
        return data
        # get received email body

    def get_inbox():
        inbox = get_inbox()
        if inbox != None:
            subject = inbox.get('subject')
            sender = inbox.get('sender')
            raw_body = inbox.get('raw_body')  # raw text body
            clean_body = inbox.get('clean_body')  # bs4 parsed body
            print('\nNew E-Mail titled: "'+subject+'", from: '+sender)
            print('\n'+'E-Mail Body:'+'\n'+clean_body)
            regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
            url = re.findall(regex, clean_body)
            mail = [x[0] for x in url]
        return mail
        s(3)

    def get_user_id(self, username):
        client = requests.Session()
        payload = {
            "username": username
        }
        response = client.post(TestData.BASE_URL +
                               'api/players/get', data=payload, verify=False)
        print(response.json()["player"]["id"])
        return response.json()["player"]["id"]

    def get_followers_ids(self, fb_cookie):
        cookie = {"fb_session": fb_cookie}
        id_notifications = []
        r = requests.get(TestData.BASE_URL + 'api/user/notifications',
                         cookies=cookie, verify=False)
        print(r)
        for i in range(len(r.json()["notifications"]["data"])):
            try:
                notification_mode = (
                    r.json()["notifications"]["data"][i]["data"]["mode"])
                if notification_mode == "follow":
                    follower_id = (
                        r.json()["notifications"]["data"][i]["data"]["user_id"])
                    id_notifications.append(follower_id)
            except KeyError:
                print("No such key")
            return id_notifications

    def new_players_all(self):
        response = requests.post(
            TestData.BASE_URL + "api/app/present", verify=False)
        new_users = (response.json()["users"]["new"])
        new_users_list = {}
        for i in range(len(new_users)):
            username = (new_users[i]["username"])
            lastName = (new_users[i]["profile"]["lastName"])
            new_users_list[username] = lastName
        return new_users_list

    