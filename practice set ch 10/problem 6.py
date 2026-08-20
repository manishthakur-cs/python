from random import randint

class train:
    def __init__(harry, trainno):
        harry.trainno = trainno
        
    def book(harry,fro,to):
        print(f"ticket is booked in train no :{harry.trainno}from {fro} to {to}")
        

    def getstatus(harry,trainno):
        print(f"train no: {harry.trainno} is running in time")
     
    def getfare(self, fro,to):
        print(f"ticket fare in train no: {harry.trainno} from {fro} to {to} is {randint(222,5555)}")


t = train(1299)
t.book("rampur", "udaipur")