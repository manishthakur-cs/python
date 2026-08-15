f = open("poem.txt")

content = f.read()

if ("twinkle" in content):
    print("twinke is present")
else:
    print("not present")
f.close()