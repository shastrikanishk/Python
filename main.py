# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/


list1=[2,3,4]
list2=[4,5,6]
for i in list1:
    for j in list2:
        k=i+j
        print(k)



list3=list1+list2
print(list3)
print(list1,list2)
list1.insert(2,"Q")
print(list1)



person = {'name': 'Alice', 'age': 25, 'city': 'New York'}

# Loop through keys
for key1 in person:
    print(key1)

# Loop through values
for value1 in person.values():
    print(value1)

# Loop through key-value pairs
for key2, value2 in person.items():
    print(key2, value2)

key1,key2=key2,key1
print(key1,key2)



sort_list1=[23,12,34,44,21,12]
m1=sort_list1
print('m1----',m1)
#def selection_sort(sort_list1):
#    n = len(sort_list1)
#    for k in range(n-1):
#        first_ele=k
#        for l in range(k+1,n):
#            if k< l
#                first_ele=l
#            else:



print(range(1))

num=range(3,12,3) #range(start,stop,step) atleast stop is required
print(num) # prints the entire object num in its entirety.
for i in num:   #iterates over each element in num and prints each element separately.
    print(i)


my_tuple = (1, 2, 3, "apple", True)
# my_tuple[0] = 10  # This would raise an error

list12=[1,'test','oi',(2,3)]
for o in list12:
    print(o)
print(list12)

print(my_tuple)
#print("true")





list_demo=[1,2,"test",1.2]
#set_demo=set(1)
dictiona_demo={}
string_demo=""
tuple_demo=()

print("list demo - ")
print(type(tuple_demo))
#print(type(set_demo))
print(list_demo)

dict2={'name':'varun','age':33,'city':'Berlin'}
print(dict2)

