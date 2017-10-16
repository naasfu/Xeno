import requests, time, random, re, thread	
from time import sleep


proxy = {
		"http":"http://" + "127.0.0.1:80",  # If u don't want to use proxy/proxies add a  '#' without the '' at the beginning of the line
		#"https":"https://" + "127.0.0.1:80" # If u don't want to use proxy/proxies add a  '#' without the '' at the beginning of the line
		}
		
if proxy:
		print(time.strftime("[%H:%M:%S]") + " - Proxies Loaded")
else:
		print(time.strftime("[%H:%M:%S]") + " - No Proxies Loaded")

url = 'https://www.adidas.com/com/apps/mi_ultraboost_xeno/application/crm.php'
list1 = ["Beck","Glenn","Becker","Carl","Beckett","Samuel","Beddoes","Mick","Beecher","HenryWard","Beethoven","Ludwigvan","Begin","Menachem","Bell","Alexander","Graham","Belloc","Hilaire","Bellow","Saul","Benchley","Robert","Benenson","Peter","BenGurion","David","Benjamin","Walter","Benn","Tony","Bennington","Chester","Benson","Leana","Bent","Silas","Bentsen","Lloyd","Berger","Ric","Bergman","Ingmar","Berio","Luciano","Berle","Milton","Berlin","Irving","Berne","Eric","Bernhard","Sandra","Berra","Yogi","Berry","Halle","Berry","Wendell","Bethea","Erin","Bevan","Aneurin","Bevel","Ken","Biden","Joseph","Bierce","Am","Brose","Biko","Steve","Billings","Josh","Biondo","Frank","Birrell","Augustine","Black","Elk","Blair","Ro","Bert","Blair","Tony","Blake","William","Blakey","Art","Blalock","Jolene","Blanc","Mel","Blanc","Raymond","Blanchet","Cate","Blix","Hans","Blood","Rebecca"]

headers = {
		'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
		'Host': 'www.adidas.com',
		'Referer': 'https://www.adidas.com/us/mi_ultraboost_xeno',
}



print (time.strftime("[%H:%M:%S]") + " - XENO BOT // Dev. @FockNikeTalk")



#emailadd = raw_input("Email: ")

class GmailDotEmailGenerator:
  def __init__(self, email):
    self.__username__, self.__domain__ = email.split('@')
  def generate(self):
    return self.__generate__(self.__username__, self.__domain__)
  def __generate__(self, username, domain):
    emails = list()
    username_length = len(username)
    combinations = pow(2, username_length - 1)
    padding = "{0:0" + str(username_length - 1) + "b}"
    for i in range(0, combinations):
        bin = padding.format(i)
        full_email = ""

        for j in range(0, username_length - 1):
            full_email += (username[j]);
            if bin[j] == "1":
                full_email += "."
        full_email += (username[j + 1])
        emails.append(full_email + "@" + domain)
    return emails

def miadidas(emails):
    for email in \
		(GmailDotEmailGenerator(emails).generate())[:1000000]:
			payload = {
		'firstname': list1[random.randint(0, 99)], # Do Not change
		'lastname': list1[random.randint(0, 99)], # Do Not change
		'email': email,
		'dateOfBirth': '1995-01-02',
		'consent': 'Y',
		'gender': 'F',
		'market': 'US',
		'language': 'EN',
	}

			req = requests.post(url, data=payload, headers=headers, proxies=proxy)
			if any(re.findall(r'successfully', str(req.text), re.IGNORECASE)):
		            print(time.strftime("[%H:%M:%S]") + " - Succesfully entered" + " - " + email )
			else:
		           print(time.strftime("[%H:%M:%S]") + " - Could not enter" + " - " + email)

try:
   thread.start_new_thread( miadidas, ("youremail@gmail.com",) ) # CHANGE TO YOUR EMAIL GMAIL ONLY
   thread.start_new_thread( miadidas, ("yoursecondemail@gmail.com",) ) # add another gmail if u want, delete this line if not
   

except:
    print "Error: unable to start thread"
while 1:
    pass
