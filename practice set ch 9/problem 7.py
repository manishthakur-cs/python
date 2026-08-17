


with open ("log.txt","r") as f:
    lines = f.readlines()

lineno = 1
for line in lines:
    if ("python" in line.lower()):
        print(f"yes , python is present. line no :{lineno}")
        break
    lineno += 1
else:
    print ("no , python is absent")

