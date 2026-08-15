p1 = "make a lot of maoney"
p2 = "buy now"
p3 = "subscribe this"
p4 = "clic this"
 
massage = input ("enter your comment : ")

if((p1 in massage) or (p2 in massage) or (p3 in massage) or (p4 in massage)):
    print ("this comment is spam")

else:
    print("this is not spam")
