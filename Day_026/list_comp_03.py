with open("file1.txt", "r") as file1:
    list1 = file1.readlines()

with open("file2.txt", "r") as file2:
    list2 = file2.readlines()

# list1 = [int(num) for num in list1]
# list2 = [int(num) for num in list2]
#
# result = [num for num in list1 if num in list2]

result = [int(num) for num in list1 if num in list2]

# Write your code above 👆

print(result)
