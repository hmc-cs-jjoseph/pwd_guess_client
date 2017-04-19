# Password guessing game


import os
import sys
import getpass
import socket
import time



def main():
    if len(sys.argv) < 2:
        port = 3001
    else:
        port = int(sys.argv[1])
    print("Welcome to the Mirai malware simulator!")
    print("In October 2016, many internet users in the US lost service for a day due to a huge DDoS attack,")
    print("mounted by a botnet of devices infected by the Mirai malware.")
    print("The Mirai malware found its way into hundreds of thousands of IoT devices using default passwords.")
    print()
    print("In this game, you're going to pretend you're a Mirai bot.")
    print("You'll be given two minutes to mount a dictionary attack on a 'device'.")
    print("The device accepts any of the login credentials that the Mirai bots used.")
    print("The object is to guess as many sets of credentials as you can!")
    print("We'll keep track of how many you get right.")
    print("Hint: the username 'root' will get you pretty far! ;)")
    print()
    name = input("Your name: ")

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("knuth.cs.hmc.edu", port))
    s.send(name.encode('UTF-8'))

    print("Waiting for others to join...")
    print()
    recvd = s.recv(1024)
    if recvd.decode('UTF-8') == "start":
        for i in range(3):
            print(3-i)
            time.sleep(1)
        print("Go!")
        while True:
            username = input("User: ")
            pwd = getpass.getpass()
            credentials = username + ":" + pwd
            s.send(credentials.encode('UTF-8'))
            recvd = s.recv(1024)
            if "success" in recvd.decode('UTF-8'):
                print("Welcome!")
            elif recvd.decode('UTF-8') == "repeat":
                print("You already guessed that.")
            elif "failure" in recvd.decode('UTF-8'):
                print("Access denied")
            if "end" in recvd.decode('UTF-8'):
                print("GAME OVER")
                break

    s.send("end".encode('UTF-8'))
    recvd = s.recv(1024)
    print()
    print(recvd.decode('UTF-8'))

    s.close()


if __name__ == "__main__":
    main()
