
word = "donkey"

with open("tables/file.txt", "r") as f:
    content = f.read()
newcontent = content.replace("donkey","#####")


with open ("tables/file.txt","w") as f:
    f.write(newcontent)