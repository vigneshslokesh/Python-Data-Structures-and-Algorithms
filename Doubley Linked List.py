# pointers work different for different data types
# Example - 1 --> Integer
print("Data type : Integer")
num1 = 11
num2 = num1

print("Before the value is updated:")
print("num1 = ",num1)
print("num2 = ",num2)

print("\nnum1 points to: ",id(num1)) # id of the object in the memory
print("num2 points to: ",id(num2))

num2 = 22

print("\nAfter the value is updated:")
print("num1 = ",num1)
print("num2 = ",num2)

print("\nnum1 points to: ",id(num1)) # id of the object in the memory
print("num2 points to: ",id(num2))

# Example - 2 --> Dictionary
print("\nData type : Dictionary")
dict1 = {
    'value' : 11
}

dict2 = dict1

print("\nBefore the value is updated:")
print("dict1 = ",dict1)
print("dict2 = ",dict2)

print("\ndict1 points to: ",id(dict1))
print("dict2 points to: ",id(dict2))

dict2['value'] = 22 # update both the dictionaries 

print("\nAfter the value is updated:")
print("dict1 = ",dict1)
print("dict2 = ",dict2)

print("\ndict1 points to: ",id(dict1))
print("dict2 points to: ",id(dict2))

