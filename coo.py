import random
from random import randint

a_dictionary = []

check_dict={}  #storing the count of names

try:
  password = 1234
  pwcheck = int(input("Password:"))
  print("Success")
except:
  print("An exception occurred")

class Santa:
    def __init__(self,name,recipient):
        self.name = name
        self.recipient = recipient

    def myfunc(self):
        print("Hi " + self.name +", Your running Secret Santa for Store " + self.recipient)

    def listOfName(self):
        a_file = open("null.txt")
        count=0
        #a_file.read()
        
        x = randint(0,len(a_dictionary))
        x += 1
        for line in a_file:
            key,value= line.split()
            a_dictionary.append(value)
            a_dictionary.append(key)

        data=list(set(a_dictionary))
        for i in data:
            check_dict[i]=a_dictionary.count(i)
            
        
        #print(a_dictionary)
        while(count < len(a_dictionary)):
            #print(a_dictionary)
            random.shuffle(a_dictionary)
            #print(a_dictionary)
            mylist = list(dict.fromkeys(a_dictionary))
            #print(mylist)
            lync = mylist[len(mylist)-x]
            lync2 = mylist[x-1]
            if lync == lync2 :
                pass
            else:
                if check_dict[lync]>0 and check_dict[lync2]>0:
                    count+=1
                    check_dict[lync]=check_dict[lync]-1
                    check_dict[lync2]=check_dict[lync2]-1
                    print(len(a_dictionary))
                    print(lync,'Matched to ',lync2)
                    if count > len(a_dictionary):
                        return
p1 = Santa('Pete','Mitchell')
p1.myfunc()
print(p1.__repr__())
p1.listOfName()

