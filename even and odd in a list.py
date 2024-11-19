list1=[]
list2=[]
list_size=int(input("Enter the size of the list1:"))
print("enter the elements of the list")
for i in range(list_size):
  list1.append(int(input()))
list2_size=int(input("Enter the size of list2"))
print("Enter the number of elements of the list2")
for i in range(list2_size):
    list2.append(int(input()))
combined_list=list1+list2
even_list=[]
odd_list=[]
for i in combined_list:
    if i%2==0:
        even_list.append(i)
    else:
        odd_list.append(i)
even_list.sort()
odd_list.sort()
print(f"sorted even numbers: {even_list}")
print(f"sorted odd numbers: {odd_list}")