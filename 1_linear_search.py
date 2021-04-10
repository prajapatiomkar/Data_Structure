#Linear_Search

list1 = [1,2,5,6,7,8,13,87,6]
print((list1))
u_in = int(input("Enter The Number To Be Search : "))
cnt = 0
for i in range(len(list1)):
    if list1[i]==u_in:
        print(list1[i],"Number On Index",i)
        cnt = 1
if cnt==0:
    print("Item Not There In List...!")      
else:
    print("Item Founded...!")       
            