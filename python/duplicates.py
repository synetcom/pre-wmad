numbers = [3, 5, 6, 4, 6, 8, 9, 10]
new_numbers =[]
for number in numbers:
    if number not in new_numbers:
        new_numbers.append(number)
print(new_numbers)
new_numbers.sort()
print(new_numbers)
