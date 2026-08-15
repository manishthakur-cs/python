d = {} # this is a empaty dictinary
marks = {
    "harry": 100,
    "rahul": 56,
    "rohan": 23,
    0: "harry"
}

print(marks.items())
print(marks.keys())
print(marks.values())
marks.update({"rohan": 99, "renuka": 100})
print(marks)
print(marks.get("rahul"))

print ( marks.get("harry")) #print none
print ( marks["harry"]) # return error