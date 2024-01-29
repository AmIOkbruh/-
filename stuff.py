mylist = [10,9,8,7,6,5,4,3,2,1]

# def bubble_sort(mylist): # Unnecessarily long idk why
#     swapped = True
#     while swapped:
#         for i in range(len(mylist)-1):
#             if mylist[i] > mylist[i+1]:
#                 temp = mylist[i+1]
#                 mylist[i+1] = mylist[i] 
#                 mylist[i] = temp
#                 swapped = True
#             else:
#                 swapped = False
#                 mylist[i],mylist[i+1]
#     return mylist

def bubble_sort(mylist):
    for i in range(len(mylist)):
        for j in range(len(mylist)-1):
            if mylist[j] > mylist[j+1]:
                mylist[j],mylist[j+1] = mylist[j+1],mylist[j]
    return mylist

print(bubble_sort(mylist))
