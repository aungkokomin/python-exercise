# list
nums = [1,2,3]
nums.append(4)
print(nums)
# unpacking the list
first,second,third,last = nums
print(first, second, third, last)
# tuple
point = (10,10) #tuple (immutable)
point = (10,10,10) # tuples can be reassigned
print(point)

# unpacking the tuple
x,y,z = point
print(x, y, z)

# dictionary
user = {"id":1,"name":"John", "age":30}
print(user)
print(user["name"])

#tag
tags = {"python", "coding", "programming"}
print(tags)

numbers = [1, 2, 3, 4, 5]
print(numbers[1:4])
print(numbers[0:])
print(numbers[::-1]) # reverse the list
print(numbers[1::3]) # slicing the list

squares = [n * 2 for n in nums]
print(squares)

slugged = {u["id"]: u["name"].lower() for u in [{"id": 1, "name": "Alice"}]}
print(slugged)