import random
lst=[]
for j in range(10):           #generating random number
    lst.append(random.randrange(0,50,1))
print(lst)

lst2 = [] #creating a new array with non-repeating elements
for j in range(len(lst)):
    if (j ==0):lst2.append(lst[0])
    elif lst[j] != lst[j-1]:lst2.append(lst[j])
print(lst2)

def findpk(lst):
    if lst2!= []:#checking if array is not empty
        peak_list = []#creating new empty array for peak elements
        n = len(lst2)#length of an array containing non-repeating elements
        for i in range(n):#iterating through elements of an array lst2
            if (i==0  and (lst2[0] > lst2[1])):# comparing 1st and 2nd elements
                peak_list.append(lst2[0])
            elif (i == n-1 and (lst2[i] > lst2[i-1])): #comparing last element to the element before it
                peak_list.append(lst2[i])
            elif i > 0 and i < len(lst2)-1: # comparing each intermediate element to its neighbors
                if(lst2[i] > lst2[i-1] and lst2[i] > lst2[i+1]):
                    peak_list.append(lst2[i])
    else:# if lst2 is empty
        return 0               
    print(peak_list)    
findpk(lst)