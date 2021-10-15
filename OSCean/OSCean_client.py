import pyrebase
from pythonosc import udp_client

config = {
  "apiKey": "AIzaSyAQcvI05cb6U4nCbbsP2YQvRsQ5_b10Nho",
  "authDomain": "ocean2midi-default-rtdb.europe-west1.firebaseapp.com",
  "databaseURL": "https://ocean2midi-default-rtdb.europe-west1.firebasedatabase.app/",
  "storageBucket": "ocean2midi-default-rtdb.europe-west1.appspot.com"
}

def stream_handler(message):
    # print(message["event"]) # put
    # print(message["path"]) # /-K7yGTTEp7O549EzTYtI
    # print(message["temp_underwater"]) # {'title': 'Pyrebase', "body": "etc..."}
    print(message["data"]) # {'title': 'Pyrebase', "body": "etc..."}

    # if message["data"] == 1:
    # 	print ("Sending OSC to show content")
    # 	client.send_message("/Content/test/enabled", 1)

    # if message["data"] == 0:
    # 	print ("Sending OSC to hide content")
    # 	client.send_message("/Content/test/enabled", 0)

    client.send_message("/ocean2osc/aveiro/temperature",message["data"])

def stream_handler_light(message):
    # print(message["event"]) # put
    # print(message["path"]) # /-K7yGTTEp7O549EzTYtI
    print(message["data"]) # {'title': 'Pyrebase', "body": "etc..."}
    # print(message["light"]) # {'title': 'Pyrebase', "body": "etc..."}

    # if message["data"] == 1:
    # 	print ("Sending OSC to show content")
    # 	client.send_message("/Content/test/enabled", 1)

    # if message["data"] == 0:
    # 	print ("Sending OSC to hide content")
    # 	client.send_message("/Content/test/enabled", 0)

    client.send_message("/ocean2osc/aveiro/light",message["data"])


firebase = pyrebase.initialize_app(config)
db = firebase.database()

client = udp_client.SimpleUDPClient("127.0.0.1", 8000)



my_stream = db.child("aveiro/temp_underwater/").stream(stream_handler)
my_streamlight = db.child("aveiro/light/").stream(stream_handler_light)




# users = db.child("Test/testUser/touch").get()
# print(users.val())


