# Binary_Search

list1 = [1,3,4,5,6,7,9,10,12,45]
print(list1)
u_in = int(input("Enter the Number you want to search : "))
low=0
high=len(list1)-1
mid=0
found=False
while low<=high and not found:
    mid=int((high+low)/2)
    if u_in==list1[mid]:
        found=True
    elif u_in>list1[mid]:
        low = mid+1
    else:
        high = mid-1
if found==True:
    print("\n",list1[mid],"is Found","at Index No.",mid,"\n")
else:
    print(u_in,"is Not there in list..!")