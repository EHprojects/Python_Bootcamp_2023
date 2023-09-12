# FileNotFound
try:
    file = open("a_file.txt")
    a_dictionary = {"key": "value"}
    value = a_dictionary["non-existent"]
except FileNotFoundError:
    file = open("a_file.txt", "w")
    file.write("Something")
except KeyError as error_msg:
    print(f"The key {error_msg} does not exist.")
else:
    content = file.read()
    print(content)
finally:
    pass
    # file.close()
    # print("File was closed.")
    # raise TypeError("This is made up")

height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("Height should not exceed 3 meters.")

bmi = weight / height * height
print(bmi)
