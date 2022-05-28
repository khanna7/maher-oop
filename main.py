#main file

#import class Jungle from jungleBook.py
from jungleBook import Jungle, RateJungle

def main():

    #create object of class jungle
    r = RateJungle("Meher", 3)
    
    r.printRating()

    r.welcomeMessage()

if __name__ == '__main__':
    main()
