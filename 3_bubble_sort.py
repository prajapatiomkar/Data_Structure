# Bubble Sort

lt= [11,52,47,62,34,12,1,5,9,65,87,654]
print("Before Sorting : ",lt,"\n")
n=len(lt)
for i in range (n-1):
    for j in range(n-i-1):
        if lt[j]>lt[j+1]:
            t= lt[j]
            lt[j]=lt[j+1]
            lt[j+1]=t  
print("After Sorting : ",lt,"\n")

