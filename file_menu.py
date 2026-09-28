def file_read():
    try:
        filename = input("Enter Filename:")
        f = open(filename, "r")
        s = f.read()
        print(s)
        f.close()
    except:
        print("File does not exist")

def file_write():
    filename = input("Enter Filename:")
    f = open(filename, "w")
    n = input("write into file:")
    f.write(n)
    f.close()

def file_append():
    filename = input("Enter Filename:")
    f = open(filename, "a")
    n = input("append into file:")
    f.write(n)
    f.close()

def file_search():
    filename = input("Enter Filename:")
    f = open(filename, "r")
    s = f.read()
    word=input("Enter word to be searched:")
    if word in s:
        print("found")
    else:
        print("Not found")
    f.close()

def file_delete():
    import os
    filename = input("Enter Filename to delete:")
    os.remove(filename)

print("Menu Driven File Operations:")
print("1.File Read")
print("2.File Write")
print("3.File Append")
print("4.File Search")
print("5.File Delete")
print("6.Exit")

while(1):
    ch=int(input("Enter your choice:"))
    if ch==1:
        file_read()
    elif ch==2:
        file_write()
    elif ch==3:
        file_append()
    elif ch==4:
        file_search()
    elif ch==5:
        file_delete()
    elif ch==6:
        exit()
    else:
        print("Invalid choice")

