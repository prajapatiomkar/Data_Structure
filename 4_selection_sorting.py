# Selection_Sort.

list1=[5,2,4,58,62,74,25,3,69,41,25]
print("Before Sorting : ",list1,"\n")
n=len(list1)

for i in range(n):
    min =i
    for j in range(i+1,n):
        if list1[min]>list1[j]:
            min=j
    temp = list1[i]
    list1[i]=list1[min]
    list1[min]=temp
print("After Sorting : ",list1,"\n")
