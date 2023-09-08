# You are going to use Dictionary Comprehension to create a dictionary called result that takes each word in the
# given sentence and calculates the number of letters in each word.

# new_dict = {new_key:new_value for item in list}
# new_dict = {new_key:new_value for (key, value) in dict.items()}

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# Don't change code above 👆

# Write your code below:

result = {word: len(word) for word in sentence.split()}

print(result)
