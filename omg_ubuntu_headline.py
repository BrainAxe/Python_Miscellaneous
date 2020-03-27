import requests
from bs4 import BeautifulSoup
# from twilio.rest import TwilioRestClient

# ====================================
#  Twilio Account Information
# ====================================

accountSID ='xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
authToken ='xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
myTwilioNumber = 'xxxxxxxxxx'
myCellPhone = 'xxxxxxxxxxx'



def textmyself(message):
    twilioCli = TwilioRestClient(accountSID, authToken)
    message = twilioCli.messages.create(body=message, from_=myTwilioNumber, to=myCellPhone)
    print("Message sent.")


def collect_headlines():
	r = requests.get("http://www.omgubuntu.co.uk/")
	soup = BeautifulSoup(r.content, "lxml")

	i = 1
	Topics = []
	Topics.append("OMG UBUNTU \n")

	for topic in soup.find_all("a",{"class": "layout__title-link"}):
		topic = topic.text.encode('utf-8', 'ignore').strip()
		topic = topic.decode('utf-8')
		T = "{:02}. {}".format(i,topic)
		Topics.append(T)
		i+=1


	headlines = "\n".join(Topics)
	print(headlines)
	#textmyself(headlines)


if __name__ == "__main__":
	collect_headlines()
