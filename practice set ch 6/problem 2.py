math = int(input("enter your mark : "))
physics = int(input("enter your mark : "))
chemistery = int(input("enter your mark : "))

total_percentage = (100)* (physics+chemistery+math)/300

if(total_percentage>=40 and math>=33 and physics>=33 and chemistery>=33):
    print("you are pass", total_percentage)


else:
     print("you are fail" , total_percentage)


