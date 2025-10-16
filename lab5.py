import re

# 1. 'a' followed by zero or more 'b's
print(bool(re.fullmatch(r'ab*', 'abbb')))  

# 2. 'a' followed by two to three 'b'
print(bool(re.fullmatch(r'ab{2,3}', 'abbb')))  

# 3. sequences of lowercase letters joined with underscore
print(re.findall(r'[a-z]+_[a-z]+', 'this_is_test and another_one'))  

# 4. one uppercase followed by lowercase letters
print(re.findall(r'[A-Z][a-z]+', 'Hello There Are Words'))  

# 5. 'a' followed by anything, ending in 'b'
print(bool(re.fullmatch(r'a.*b', 'acccb')))  

# 6. replace space, comma, or dot with colon
print(re.sub(r'[ ,.]', ':', 'Hello, world. How are you'))  

# 7. convert snake_case to camelCase
def snake_to_camel(s):
    parts = s.split('_')
    return parts[0] + ''.join(word.capitalize() for word in parts[1:])
print(snake_to_camel('this_is_snake_case'))  

# 8. split string at uppercase letters
print(re.split(r'(?=[A-Z])', 'SplitAtUpperCase'))  

# 9. insert spaces between words starting with capital letters
print(re.sub(r'(?=[A-Z])', ' ', 'InsertSpacesBetweenWords'))  

# 10. convert camelCase to snake_case
print(re.sub(r'([A-Z])', r'_\1', 'camelCaseToSnake').lower())  
