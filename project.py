from pathlib import Path



def readFileAndFolder():
    path = Path("")
    items = list(path.rglob("*"))
    for i,items in enumerate(items):
        print(f"{i+1} : {items}")

def createfile():
    try:
        readFileAndFolder()
        name=input("enter the name of the file you want to create: ")
        p = Path(name)
        if not p.exists():
            with open(p,"w") as fs:
                data = input("enter the data you want to write in the file: ")
                fs.write(data)
            print("file created successfully")  
        else:
            print("file already exists")      
    except Exception as e:
        print("an error occiured",e)   


def readfile():
    try:
        readFileAndFolder()
        name=input("enter the name of the file you want to read: ")
        p = Path(name)
        if p.exists() and p.is_file():
            with open(p,"r") as fs:
                data = fs.read()
                print(data)
            print("file read successfully")    
        else:
            print("file does not exists")      
    except Exception as e:
        print("an error occiured",e)   

def updatefile():
    try:
        readFileAndFolder()
        name=input("enter the name of the file you want to update: ")
        p = Path(name)
        if p.exists() and p.is_file():
           print("press 1 for changing the name of your file:-")
           print("press 2 for overwriting the data in your file:-")
           print("press 3 for appending the data in your file:-")
           choice = int(input("enter your choice: "))
           if choice == 1:
               newname = input("enter the new name of the file: ")
               p.rename(newname)
               print("file name changed successfully")
           if choice == 2:
               with open(p,"w") as fs:
                   data = input("enter the data you want to write in the file: ")
                   fs.write(data)
               print("file updated successfully")
        if choice == 3:
               with open(p,"a") as fs:
                   data = input("enter the data you want to append in the file: ")
                   fs.write(" "+data)
               print("file updated successfully")   

          
    except Exception as e:
        print("an error occiured",e)   



def deletefile():
    try:
        readFileAndFolder()
        name=input("enter the name of the file you want to delete: ")
        p = Path(name)
        if p.exists() and p.is_file():
            p.unlink()
            print("file deleted successfully")
        else:
            print("file does not exists")      
    except Exception as e:
        print("an error occiured",e)


print("press 1 for creating a file")
print("press 2 for reading a file")
print("press 3 for updating a file")
print("press 4 for deleting a file")

check = int (input("please enter your choice: "))

if check ==1:
    createfile()
elif check ==2:
    readfile()
elif check ==3:
    updatefile()
elif check ==4:
    deletefile()
else:
    print("invalid choice")