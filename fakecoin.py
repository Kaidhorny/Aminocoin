import amino
import requests
from uuid import uuid4
import time
try:
    import colorama
except ModuleNotFoundError:
    os.system("pip install colorama")
    import colorama
try:
    import pyfiglet
except ModuleNotFoundError:
    os.system("pip install pyfiglet")
    import pyfiglet

colorama.init()
print(colorama.Fore.GREEN)
print(colorama.Style.BRIGHT)
f = pyfiglet.Figlet(font='slant')
print (f.renderText('TECH'))
f = pyfiglet.Figlet(font='slant')
print (f.renderText('VISION'))
f = pyfiglet.Figlet(font='digital')
print (f.renderText('Fake coins Bot'))
dec = '━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━' 
print("""
Youtube:
https://youtube.com/channel/UCPuZzOqlfpx_QTaC2yix7Pg

Discord Server:
https://discord.gg/YMfvAxm6zF
""")
print(dec)
print("\nCommand is .clear")
email=input("\nEnter Email: ")
password=input("\nEnter Password: ")
client=amino.Client()
client.login(email=email,password=password)
print("logged in")
n=input("\nCommunity/chat link : ")
print(dec)
print("\nJoining Chatrooms")
fok=client.get_from_code(n)
id=client.get_from_code(n).objectId
cid=fok.path[1:fok.path.index("/")]

subclient=amino.SubClient(comId=cid,profile=client.profile)
chts=subclient.get_public_chat_threads(type="recommended", start=0, size=100).chatId
for chats in chts:
	try:
		subclient.join_chat(chatId=chats)
	except Exception:
		pass
print(dec)
print("\nJoined all Chatrooms")
self=client.socket
def generate_transaction_id(self):
        return str(uuid4())

@client.event("on_text_message")
def on_text_message(data):
	ex=data.message.content
	cd=ex.split(' ')
	x=cd[0]
	c=cd[1:]
	if x.lower()==".coin":
		transaction=generate_transaction_id(self)
		print(transaction)
		try:
			for i in c:
				d=int(i)
				a=subclient.send_coins(coins=d, chatId=data.message.chatId, transactionId=transaction)
				subclient.send_message(chatId=data
				message.chatId,message=f"Sent {d} coins to Host")
		except Exception as e:
			print(e)
			pass

print(dec)
print("\n Bot ready")
def socketRoot():
	j=0
	while True:
		if j>=300:
			print("Updating socket.......")
			client.close()
			client.start()
			print("Socket updated")
			j=0
		j=j+1
		time.sleep(1)
socketRoot()