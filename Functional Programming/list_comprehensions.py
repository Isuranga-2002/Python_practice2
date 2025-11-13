# Original approach using a loop
numbers = [1, 2, 3, 4, 5]
squares = []
for num in numbers:
  squares.append(num ** 2)

# Using a list comprehension to square each number
squared_numbers = [num ** 2 for num in numbers]

# Displaying the outcomes
print('Original Numbers:', numbers)
print('Squared Numbers(Without using comprehensions):', squares)
print('Squared Numbers(With using comprehensions):', squared_numbers)

#Commented for a commit