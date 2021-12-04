#! /usr/bin/python3

import random
from random import randint

a_dictionary = []

check_dict={}  #storing the count of names

try:
  password = 1234
  pwcheck = int(input("Password:"))
  password = pwcheck
  print("Success")
except:
  print("An exception occurred")
  exit()

class Santa:
    def __init__(self,name,recipient,passwordres):
        self.name = name
        self.recipient = recipient
        self.__passwordres = passwordres

    def myfunc(self):
        print("Hi " + self.name +", Your running Secret Santa for Store " + self.recipient)
        passwordres = 0
        print(passwordres)

    def listOfName(self):
        a_file = open("null.txt")
        count=0
        #a_file.read()
        
        x = 0
        for line in a_file:
            key,value= line.split()
            a_dictionary.append(value)
            a_dictionary.append(key)
        data=list(set(a_dictionary))
        #print(data)
        for i in data:
            check_dict[i]=a_dictionary.count(i)
            
        
        print("A:",a_dictionary)
        mylist = a_dictionary[:]
        random.shuffle(a_dictionary)
        print("B: ",mylist)
        finalList = []
        while len(mylist) != 0: 
            if mylist[x] != a_dictionary[x]: 
                finalList.append(mylist[x] + a_dictionary[x])
                print(mylist[x] , ' Matched to ' , a_dictionary[x])
                mylist.remove(mylist[x])
                a_dictionary.remove(a_dictionary[x])
        #print(len(mylist))
        #print("C:",finalList)
        #if lync != lync2 :
        #    x += 1
        #    for lync in a_dictionary:
        #        print(lync,'Matched to ',lync2)
        #else:
         #   if check_dict[lync]>0 and check_dict[lync2]>0:
         #       count +=1
                #check_dict[lync]=check_dict[lync]
                #check_dict[lync2]=check_dict[lync2]
                #print(len(a_dictionary))
                
               # if count > len(a_dictionary):
                #    return
p1 = Santa('Pete','Mitchell','con')
p1.myfunc()
print(p1.__repr__())
p1.listOfName()
