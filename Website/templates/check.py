import sys
import time

from multiping import MultiPing


def Ping_Check():
    mp = MultiPing(["8.8.8.8", "8.8.4.4", "127.0.0.1", "1.1.1.1"])
    try:
        mp.send()
        time.sleep(10)
        responses, no_responses = mp.receive(1)
        for good_respond in responses:
            print("this address pinges successfully ", good_respond)
        if no_responses:
            for bad_respond in no_responses:
                print("Address ", bad_respond, "Wasnt pinged seccuessfully!")
                return sys.exit(2)
        else:
            print("All Good")
            sys.exit(0)
    except:
        Ping_Check()


while True:
    try:
        Ping_Check()
    except:
        pass
