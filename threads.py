from threading import *
from time import *
class Hello(Thread):
    def run(self):                               #The method name should be run only in threading
        for i in range(5):
            print("Hello")
            sleep(1)
class Hi(Thread):
    def run(self):
        for i in range(5):
            print("Hii")
            sleep(1)

s1=Hello()
s2=Hi()
s1.start()
sleep(0.2)
s2.start()

s1.join()                           #This will tell main thread to join once these two threads are over.
s2.join()

print("Bye!! Bye!!!")

