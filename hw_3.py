# STRINGS
course = "Python Course for Beginners"
print(course)

#Define string for multiple sentences: example- an email, use triple quotes
mail = '''    
Hi John,
Here is our first mail to you.

Thank you,
The support team

'''
print(mail)

#Using Square bracket []  for getting character. Index of characters in python is 01234..
# We can get negative index here. -1 is the index of the last character, assuming that 0 is the character of the first character.
course = 'Python for Beginners'
print (course[-3])
print  (course[0:3])   #Excludes character which is at the 3rd place
print (course[0:])     #Includes all the characters
print (course[1:])     #Excludes 1st character
print (course[:5])     #With end index, includes 0th character
print (course[:])      #Leave it blank, then starting index will be 0 and the lenght of the index is the ending index

#Example
name = 'Jennifer'
print (name[1:-1])

# FORMATTED STRINGS
# Example: To print John [Smith] is a coder
first = 'John'
last = 'Smith'
message = first + ' [' + last +'] is a coder'
print (message)
# With more complicated texts, it becomes time consuming, so we use formatted strings. f is used for formatted string.
# Curly brackets are place holders
msg = f'{first}  [{last}] is a coder'

# STRING METHODS
#len() is used to know the length of the character. It's a general purpose function.
print(len(course))
#course._____ The options we get are nothing but the methods
print (course.upper())          #For uppercase
print (course.lower())          #For lowercase
print (course.find('P'))        #To find P, it will return with an index number of P. Find is case sensitive
print (course.replace('Beginners', 'Absolute Beginners'))  #Replace is case sensitive.
'.....' in .......              #To find if python is in the course variable. The result will have boolean value.