import os
from datetime import date
today = date.today()
os.system("cls")


file1 = open("resume.txt","a+")#append mode 
print(""" \n\n
Please type in what did you do today
\n\n""")




while True:
    
    message = input(">>")
    if(message=="exit()"):
        exit()

    if(message=="read logs"):
         
        print("\n***LOGS***\n\n")
        file1 = open("resume.txt","r+")  
        print(file1.read())


    a=input("\n\nWould you like to enter into logs :- ")
    
    if(a=="yes"):
        today = str(today)
        log = today + ":- " + message +'\n'
        file1.write(log) 
        file1.close()
        exit()
    
    if(a=='message'):
        print("\n\n",message,"\n\n")
    
    if(a=='exit()'):
        exit()    

    if(a=='rewrite message'):
        print("\n\nok\n\n")
    
    if(a=='help'):
        print("""\n\nhelp:- to show help\n
        yes:- after message will enter into logs\n 
        messahe after you type the message will show the message you typed\n
        rewrite :- will re write the message you want to write\n
        exit():- to exit the program\n""")        