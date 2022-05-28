#class declaration: jungleBook.py
class Jungle:
    #constructor with default values
    def __init__(self, name="Unknown"): 
        self.visitorName = name

    def welcomeMessage(self):
        print("Hello %s, Welcome to the jungle" % self.visitorName)

class RateJungle(Jungle):
    def __init__(self, name, feedback):
        # feedback 1-10, 1 is highest
        self.feedback = feedback #public attribute

        #inherit the constructor of the class
        super().__init__(name)

# using parent class attribute i.e. visitorName
    def printRating(self):
        print("Thanks %s for your feedback" % self.visitorName)

