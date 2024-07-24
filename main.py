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



