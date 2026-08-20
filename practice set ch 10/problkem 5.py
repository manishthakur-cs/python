from random import randint

class train:
    def __init__(self, trainno):
        self.trainno = trainno
        
    def book(self,fro,to):
        print(f"ticket is booked in train no :{self.trainno}from {fro} to {to}")
        

    def getstatus(self,trainno):
        print(f"train no: {self.trainno} is running in time")
     
    def getfare(self, fro,to):
        print(f"ticket fare in train no: {self.trainno} from {fro} to {to} is {randint(222,5555)}")


t = train(1299)
t.book("rampur", "udaipur")
        