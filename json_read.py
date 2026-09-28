# import json

# f=open("data.json","r")
# content=json.load(f)
# print(content)
# print(content[0]['name'],content[0]['age'])
# f.close()

# WRITE
import json
content=[
    {"title":"book1","author":"john","price":200},
    {"title":"book2","author":"sam","price":300}
]
f=open("book.json","w")
json.dump(content,f)
f.close()
