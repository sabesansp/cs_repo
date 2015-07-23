#!/bin/python

s = 

num_list = list()

length = len(s)

print length

for m in range(0,100) :
   if m >= 0 and m<10 :
      num_list.append('0'+str(m))
   else : 
      num_list.append(str(m))

#print num_list



for i in range(0,length-1) :
   sval = s[i] + s[i+1]
   #print sval
   if sval in num_list :
      num_list.remove(sval)


if len(num_list) == 0:
    print True
else :
    print False




