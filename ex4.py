#ex3.py

#class declaration
class Jungle:
    #constructor with default values
    def __init__(self, name="Unknown"): 
        self.visitorName = name

    def welcomeMessage(self):
        print("Hello %s, Welcome to the jungle" % self.visitorName)

def main():
    #create object of class jungle
    j=Jungle("Maher")
    j.welcomeMessage()

    #create object of class jungle
    k=Jungle("")
    k.welcomeMessage()

if __name__ == '__main__':
    main()
