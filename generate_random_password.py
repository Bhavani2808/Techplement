
#  GENERATE RANDOM PASSWORD
num_of_characters=int(input("Enter your desired no.of characters:"))

def generate_random_password(num_of_characters,upper,lower,symbols,digits):
    
    upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lower = 'abcdefghijklmnopqrstuvwxyz'
    symbols = '@#$%!.~^*&'
    digits = '0123456789'
    
    
    all_elements = ''
    if upper:
        all_elements += upper
    if lower:
        all_elements += lower
    if symbols:
        all_elements += symbols
    if digits:
        all_elements += digits    
    
    s=set(all_elements)
    #print(len(s))
    
    
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
    
use_upper = input("use uppercase letters (yes/no)? > ") == 'yes'
use_lower = input("use lowercase letters (yes/no)? > ") == 'yes'
use_symbols = input("use symbols (yes/no)? > ") == 'yes'
use_digits = input("use digits (yes/no)? > ") == 'yes'

print()       
result=generate_random_password(num_of_characters,use_upper,use_lower,use_symbols,use_digits)
print(result)
print()
