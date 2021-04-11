#Insertion_Sort

list1 = [22,3,41,7,8,54,26,98,74]
print("\nBefore Insertion_Sort",list1,"\n")
i=1
for i in range(1,len(list1)):
    new=list1[i]
    j=i-1
    while j>=0 and new<list1[j]:
        if new<list1[j]:
            list1[j+1]=list1[j]
            j=j-1
        else:
            break
        list1[j+1]=new
print("After Insertion_Sort",list1,"\n")