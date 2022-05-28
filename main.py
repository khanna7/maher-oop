#main file

#import class Jungle from jungleBook.py
from jungleBook import Jungle, RateJungle
from scarySound import Animal, Bird

def main():

    #create object of class jungle
    r = RateJungle("Meher", 3)
    
    r.printRating()

    r.welcomeMessage()

    a=Animal()
    b=Bird() 

    a.scarySound()
    b.scarySound()

if __name__ == '__main__':
    main()
