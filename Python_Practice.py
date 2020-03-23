#Practicing Python with 365DataScience.com


#Radus of a Circle with User Input
radius = float(input('Pleast enter the circle radius:'))
pi = 3.14159
area = pi*radius**2
print('You entered', radius, 'the area of the circle is', area)

#Converting Fahrenheit to Celsius
far = float(input('Please enter the temperature in Fahrenheit: '))
cel = (far - 32) * 5/9
print(far,'Fahrenheit in Celsius is', cel)


#Obtain the sum of two integers and the product

num1 = int(input('Please enter the first number: '))
num2 = int(input('Please enter the second number: '))
print('The sum of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(num1 + num2))
product = num1 * num2
print('The product of', num1, 'and', num2, 'is', product)


#Bob, Ann, Jane and Ashwin want to order pizza - they know they will each eat 4 slices
#of pizza. The local pizza shop sells pizzas of only 6 slices.
#What is the minimum number of pizzas needed?

total_slices = 4 * 4
number_of_pizzas = (total_slices + 5)//6
slices_left = number_of_pizzas*6 - total_slices
print('Number of pizzas required is', number_of_pizzas,'there will be', slices_left,
      'remaining slices.')


#What should I wear?

temp = int(input('Please enter the temperature in Fahrenheit. \
                 An integer between 0-100:>>> '))

if temp > 75:
    print('Wear shorts and sunscreen')
elif temp <= 75 and temp > 65:
    print('It\'s warm, but not shorts weather!')
elif temp <= 65 and temp > 45:
    print('You\'ll probably need a vest today')
else:
    print('Too Cold! Don\'t go outside!')
    

#Can you guess the word I'm thinking of?
    
word = 'summer'

guess = input("I'm thinking of a word, can you guess what it is? \n Hint: It's a season!>>> ")

guess = guess.lower()

if guess == 'summer':
    print("Yes, it's Summer: Well Done!!")
elif guess == 'winter':
    print("No, it's not Winter. Sorry!")
elif guess == 'autumn':
    print("No, it's not Autumn. Sorry!")
elif guess == 'spring':
    print("No, it's not Spring. Sorry!")
else:
    print(guess.capitalize(), 'is not a season!')


#Write code that asks the user to input a number between 1 and 5 inclusive. The code
#will take the integer value and print out the string value. So for example if the user
#inputs 3 the code will print "Three". Reject any input that is not a number in that range!
    
user_input = int(input('Please enter an integer between 1 and 5:>>> '))

if user_input == 1:
    print("One")
elif user_input == 2:
    print("Two")
elif user_input == 3:
    print("Three")
elif user_input == 4:
    print("Four")
elif user_input == 5:
    print("Five")
else:
    print("Out of Range")
    
    
#Write code that turns a string into an integer!
    
user_input = input('Please type out a number between one and five:>>> ')
user_input = user_input.lower()

if user_input == 'one':
    print(1)
elif user_input == 'two':
    print(2)
elif user_input == 'three':
    print(3)
elif user_input == 'four':
    print(4)
elif user_input == 'five':
    print(5)
else:
    print("Out of Range")


#Guess a number
    
secret_number = 3

guess = input('Guess the number between 1-10:>>> ')

if guess.isdigit():
    guess = int(guess)
    if guess == secret_number:
        print("You've guessed correctly, you win!")
    elif guess > secret_number and guess <= 10:
        print("You guessed too high. Sorry you lose!")
    elif guess < secret_number and guess >= 1:
        print("You guessed too low. Sorry you lose!")
    else:
        print("Out of Range")
else:
    print("That's not even an integer! What are you playing at?!")
    
    

