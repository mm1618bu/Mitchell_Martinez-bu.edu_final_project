#! /usr/bin/python3

import random # importing the random module to assist with re-arraging names
from random import randint # importing randint to help generate a random integer

a_dictionary = [] # defining a blank list

check_dict={}  #storing the count of names

try: # user will be asked to enter a password. If it is correct, the program will run. If not, the program will exit.
  password = 123456789
  print(" ")
  pwcheck = int(input("Password:"))
  if password != pwcheck:
      exit()
except:
  print("An exception occurred")
  exit()

class Santa: # Define the class Santa
    def __init__(self,name,recipient,passwordres): # Defining the inital name, recipient and password
        self.name = name
        self.recipient = recipient
        self.__passwordres = passwordres

    def myfunc(self):
        print("Hi " + self.name +", Your running Secret Santa for Store " + self.recipient) # This will print the name and store that the program is running for
        passwordres = 123456789 # defines the program password. If correct, the program will run. If not, the program will exit.
        if passwordres == 123456789:
            pass
        else:
            exit()

    def __repr__(self): # Prints confirmation that the program can run after verifying credentials
        return(self.name +" We have confirmed you are authorized to run this program.")

    def resultprint(self): # Prints the header of the list
        return("The Secret Santa Pairs for Store " + self.recipient + " Are as follows: ")

    def listOfName(self):
        a_file = open("null.txt") # opens the text file
        count=0 # makes the count variable set to 0
        
        x = 0 # makes the value of x equal 0
        for line in a_file: # for each line in the text file
            key,value= line.split() # Split the two words into two different variables per line
            a_dictionary.append(value) # Append the second word in the line to the a_dicitonary list
            a_dictionary.append(key) # Append the first word in the line to the a_dictionary list
        data=list(set(a_dictionary)) # make data a set of dictionary, then make back into list to prevent duplicates
        for i in data:
            check_dict[i]=a_dictionary.count(i) # for each line, make sure there are no duplicate values
            
        
        mylist = a_dictionary[:] # split the list up by name
        random.shuffle(a_dictionary) # shuffle the values around in the list
        finalList = [] # define the list where all the pairs will be matched
        while len(mylist) != 0: # while mylist is not empty
            if mylist[x] != a_dictionary[x]:  # if there are the same name in both list, dont match. Otherwhise:
                finalList.append(mylist[x] + a_dictionary[x]) # append both names at the selected index together in the finalList
                print(mylist[x].upper() , ' Buys a Gift For ' , a_dictionary[x].upper()) # Print the pairings on  seperate lines, with the names UPPERCASE
                mylist.remove(mylist[x]) # remove the name from the list after picking
                a_dictionary.remove(a_dictionary[x]) # remove the name from the list after picking
            else:
                mylist.append(mylist.pop(0)) # Remove the first person in the list to prevent duplication
p1 = Santa('Mitchell','North Quincy',1234) # Run the Santa Class with the User's name, store name, and a default pw
p1.myfunc() #Run myFuc
print(" ") #Blank Line
print(p1.__repr__()) # Runs the confirmation print statement in the fuction above
print(" ") #Blank Line
print(p1.resultprint()) # Prints the results
print(" ") #Blank Line
p1.listOfName() # Prints the actual program
print(" ") #Blank Line
print("Thanks For Playing! Enjoy your Gifts!")
