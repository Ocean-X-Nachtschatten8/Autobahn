import requests
from time import sleep

URL = "http://192.168.1.63:8000/run/"

print("Öffne mit Firefox:")
print("http://192.168.1.63:8080/?action=stream")

def action(cmd):
    r = requests.get(URL,params = {"action": cmd})

def vorwärts(sekunden):
    action("forward")
    sleep(sekunden)
    action("stop")

def rechts():
    action("fwright")

def geradeaus():    
    action("fwstraight")
    

def links():
    action("fwleft")


def rückwärts(sekunden):
    action("backward")
    sleep(sekunden)
    action("stop")


#	if !(cmd in Set(["bwready","forward","backward","stop",
# 		            "fwready","fwleft","fwright", "fwstraight",
#		            "camready","camleft","camright","camup","camdown"]))
