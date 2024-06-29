# Purpose
### The Python program generates a random password based on user-specified criteria, including length, uppercase/lowercase letters, symbols, and digits.

# Features
###  Allows the user to specify the desired password length.
### Allows uppercase, lowercase, symbols, and digits.
### Ensures the minimum password length.
### Generates unique passwords to avoid repetition.

# Code for Generating Password

##  Define Function:
### Define the function with name 'generate_random_password' to generates random password.
### Function parameters are 'num_of_characters, upper, lower, symbols, and digits.'

#### def generate_random_password(num_of_characters,upper,lower,symbols,digits):

## Create strings to assign & assign various characters:
### The function defines character sets for uppercase, lowercase letters, symbols, and digits as strings.
## Creating the Mixed Character Set:
### The user initializes a blank string called all_elements, and then adds matching character sets to it under their choices.
## Convert 'all_character' into a set:
### s=set(all_elements) 
## Logic for password generating:

### Initializes empty string password.
### Iterates num_of_characters to build password.
### Handles errors for insufficient length or exceeding unique characters.
### Randomly selects, adds, removes character to avoid duplicates.

## Take input from user:
### User Password Preferences Code:
### Collects user input.
### Asks for password length.
### Decides on uppercase, lowercase, symbols, digits.
## Function call:
### The user's inputs are passed to the function generate_random_password, and the resultant password is saved in the variable result. Next, the password is printed.

# Example Usage
## Consider the following example to learn how the program works:

### Desired number of characters: 6
### Use uppercase letters: yes
### Use loercase letters: yes
### Use symbols: yes
### Use digits: yes

###   The program will generate a 6-character random password consisting of uppercase, lowercase, symbols, and digits.


# CODE

```
#GENERATE RANDOM PASSWORD
num_of_characters=int(input("Enter your desired no.of characters:"))

#Define function 

def generate_random_password(num_of_characters,upper,lower,symbols,digits):
    
    #create string variables to store various characters

    upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lower = 'abcdefghijklmnopqrstuvwxyz'
    symbols = '@#$%!.~^*&'
    digits = '0123456789'
    
    #create empty string variable to store mixed characters

    all_elements = ''
    if upper:
        all_elements += upper
    if lower:
        all_elements += lower
    if symbols:
        all_elements += symbols
    if digits:
        all_elements += digits    
    
    #convert to string to remove duplicates and get random characters

    s=set(all_elements)
    #print(len(s))
    
    #create empty string variable to store characters after iterating

    password=''
    for _ in range(num_of_characters):
        if num_of_characters<4:
            print("ValueError: Your password length should be at least 4 characters.")
            break
        elif num_of_characters>=len(s):
            print("ValueError: num_of_characters exceeds the length of the set s.")
            break
        character=next(iter(s))
        password +=character
        s.remove(character)
    return password
#create input method for get input from user

use_upper = input("use uppercase letters (yes/no)? > ") == 'yes'

use_lower = input("use lowercase letters (yes/no)? > ") == 'yes'

use_symbols = input("use symbols (yes/no)? > ") == 'yes'

use_digits = input("use digits (yes/no)? > ") == 'yes'

print()     #for empty line 

result=generate_random_password(num_of_characters,use_upper,use_lower,use_symbols,use_digits)

#print random password

print(result)

```

## Summary
### This application generates a random password depending on user-specified criteria. It handles issues such as inadequate password length and exceeding the number of allowable unique characters. The generated password appears as the output.
