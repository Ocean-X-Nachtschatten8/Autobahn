import requests
from time import sleep

URL = "http://192.168.1.63:8000/run/"

def action(cmd):
    r = requests.get(URL,params = {"action": cmd})


def vorwärz(sekunden):
    action("forward")
    sleep(sekunden)
    action("stop")

def rechts():
    action("fwright")

def geradeaus():    
    action("fwstraight")
    

def links():
    action("fwstraight")
def zurück(sekunden):
    action("backward")
    sleep(sekunden)
    action("stop")


#	if !(cmd in Set(["bwready","forward","backward","stop",
# 		            "fwready","fwleft","fwright", "fwstraight",
#		            "camready","camleft","camright","camup","camdown"]))
