import math
import os
import string
import time

# ---------- Built-in Functions Exercises ----------

# 1. Multiply all numbers in a list
nums = [2, 3, 4, 5]
result = math.prod(nums)
print("Product of all numbers:", result)

# 2. Count uppercase and lowercase letters in a string
s = input("Enter a string: ")
upper = sum(1 for c in s if c.isupper())
lower = sum(1 for c in s if c.islower())
print("Uppercase letters:", upper)
print("Lowercase letters:", lower)

# 3. Check if a string is palindrome
s = input("Enter a string: ")
is_palindrome = s == ''.join(reversed(s))
print("Is palindrome:", is_palindrome)

# 4. Invoke square root after specific milliseconds
num = int(input("Enter number: "))
ms = int(input("Enter milliseconds: "))
time.sleep(ms / 1000)
print(f"Square root of {num} after {ms} milliseconds is {math.sqrt(num)}")

# 5. Return True if all elements of the tuple are true
t = (True, True, 1, "text")
print("All elements are true:", all(t))

# ---------- Directories and Files Exercises ----------

# 6. List only directories, files and all together
path = "."
print("Directories:", [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))])
print("Files:", [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))])
print("All:", os.listdir(path))

# 7. Check for access to a specified path
path = input("Enter path: ")
print("Exists:", os.access(path, os.F_OK))
print("Readable:", os.access(path, os.R_OK))
print("Writable:", os.access(path, os.W_OK))
print("Executable:", os.access(path, os.X_OK))

# 8. Test whether path exists and split into filename and directory
path = input("Enter path: ")
if os.path.exists(path):
    print("Directory part:", os.path.dirname(path))
    print("File name part:", os.path.basename(path))
else:
    print("Path does not exist")

# 9. Count number of lines in a text file
filename = input("Enter filename: ")
with open(filename, 'r') as f:
    lines = f.readlines()
    print("Number of lines:", len(lines))

# 10. Write a list to a file
data = ["apple", "banana", "cherry"]
with open("output.txt", "w") as f:
    for item in data:
        f.write(item + "\n")
print("List written to output.txt")

# 11. Generate 26 text files named A.txt to Z.txt
for letter in string.ascii_uppercase:
    with open(f"{letter}.txt", "w") as f:
        f.write(f"This is file {letter}.txt")
print("26 files created (A.txt ... Z.txt)")

# 12. Copy contents of one file to another
src = input("Enter source file: ")
dst = input("Enter destination file: ")
with open(src, "r") as f1, open(dst, "w") as f2:
    f2.write(f1.read())
print("File copied successfully")

# 13. Delete file by specified path
path = input("Enter path to delete: ")
if os.path.exists(path):
    if os.access(path, os.W_OK):
        os.remove(path)
        print("File deleted")
    else:
        print("No permission to delete file")
else:
    print("File does not exist")
