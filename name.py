#!/usr/bin/python
import random
import os
#some names..
list1 = ['akash','amit','jay','rahul','anand','ravindra','ankit','kunal','saheb','arjun','aaditya','sanjay','op','sunil','navneet']
#take a list for storing the names which are selected/generated by the code.
listTemp = [] 
os.system('clear')
print "game started..."
 
def generator():
 #print "hit enter to continue:"
 #raw_input()
 print "player's name generated"
 rand_item1 = random.sample(list1,1)  
 rand_item2 = random.sample(list1,1)
 listTemp.append(rand_item1)
 listTemp.append(rand_item2)
 try:
    list1.remove(rand_item1)
    list1.remove(rand_item2)
 except:
    pass
 print rand_item1,
 print " vs",
 print rand_item2

#call the function until it has !zero names.
for names in list1:
 generator()
 
for j in listTemp:
 print j 
