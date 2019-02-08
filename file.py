name=input("enter your name")
myfile= open("myfile.txt","w")
myfile.write(name)
myfile.close()