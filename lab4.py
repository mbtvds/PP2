# ===============================
# PYTHON ITERATORS AND GENERATORS
# ===============================

# 1. Generator that generates squares of numbers up to N
def gen_squares(n):
    for i in range(1, n + 1):
        yield i ** 2

print("Squares up to N:")
for x in gen_squares(5):
    print(x, end=" ")
print("\n")

# 2. Print even numbers between 0 and n in comma separated form
n = int(input("Enter n for even numbers: "))
even_gen = (str(i) for i in range(0, n + 1) if i % 2 == 0)
print(",".join(even_gen))
print()

# 3. Generator for numbers divisible by 3 and 4 between 0 and n
def div_by_3_and_4(n):
    for i in range(n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

print("Numbers divisible by 3 and 4:")
for num in div_by_3_and_4(50):
    print(num, end=" ")
print("\n")

# 4. Generator squares from (a) to (b)
def squares(a, b):
    for i in range(a, b + 1):
        yield i ** 2

print("Squares from 2 to 6:")
for val in squares(2, 6):
    print(val, end=" ")
print("\n")

# 5. Generator that returns all numbers from n down to 0
def countdown(n):
    while n >= 0:
        yield n
        n -= 1

print("Countdown from 5:")
for i in countdown(5):
    print(i, end=" ")
print("\n")

# ===============================
# PYTHON DATE
# ===============================

import datetime

# 1. Subtract five days from current date
today = datetime.date.today()
five_days_ago = today - datetime.timedelta(days=5)
print("Current date:", today)
print("Five days ago:", five_days_ago)
print()

# 2. Yesterday, today, tomorrow
yesterday = today - datetime.timedelta(days=1)
tomorrow = today + datetime.timedelta(days=1)
print("Yesterday:", yesterday)
print("Today:", today)
print("Tomorrow:", tomorrow)
print()

# 3. Drop microseconds
now = datetime.datetime.now()
without_microseconds = now.replace(microsecond=0)
print("Now:", now)
print("Without microseconds:", without_microseconds)
print()

# 4. Calculate difference between two dates in seconds
date1 = datetime.datetime(2025, 1, 1, 0, 0, 0)
date2 = datetime.datetime(2025, 1, 1, 1, 30, 0)
difference = (date2 - date1).total_seconds()
print("Difference in seconds:", difference)
print()

# ===============================
# PYTHON MATH LIBRARY
# ===============================

import math

# 1. Convert degree to radian
degree = 15
radian = math.radians(degree)
print("Input degree:", degree)
print("Output radian:", round(radian, 6))
print()

# 2. Area of trapezoid
height = 5
base1 = 5
base2 = 6
area_trapezoid = 0.5 * (base1 + base2) * height
print("Area of trapezoid:", area_trapezoid)
print()

# 3. Area of regular polygon
n_sides = 4
length = 25
area_polygon = (n_sides * (length ** 2)) / (4 * math.tan(math.pi / n_sides))
print("Area of polygon:", area_polygon)
print()

# 4. Area of parallelogram
base = 5
height = 6
area_para = base * height
print("Area of parallelogram:", area_para)
print()

# ===============================
# PYTHON JSON PARSING
# ===============================

import json

# Пример данных из sample-data.json
data = {
    "imdata": [
        {"l1PhysIf": {"attributes": {"dn": "topology/pod-1/node-201/sys/phys-[eth1/33]", "descr": "", "speed": "inherit", "mtu": "9150"}}},
        {"l1PhysIf": {"attributes": {"dn": "topology/pod-1/node-201/sys/phys-[eth1/34]", "descr": "", "speed": "inherit", "mtu": "9150"}}},
        {"l1PhysIf": {"attributes": {"dn": "topology/pod-1/node-201/sys/phys-[eth1/35]", "descr": "", "speed": "inherit", "mtu": "9150"}}}
    ]
}

print("Interface Status")
print("=" * 80)
print(f"{'DN':<50} {'Description':<20} {'Speed':<8} {'MTU':<6}")
print("-" * 80)

for item in data["imdata"]:
    attr = item["l1PhysIf"]["attributes"]
    print(f"{attr['dn']:<50} {attr['descr']:<20} {attr['speed']:<8} {attr['mtu']:<6}")
