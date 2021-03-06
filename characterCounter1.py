# accept a string/message, count the occurance of each letter
# and print result to screen


print('enter a phrase to count the occurance of each charatcer...\n')
message = input()

count = {}

""" for each char in the 'message' variable, cycle through from first to last...
set each char default value to 0, then add 1 every tim that char is discovered"""
for char in message:
    count.setdefault(char, 0)
    count[char] = count[char] + 1

""" sort the dict based on the char with the highest occurance,
in descending/reverse order, assign the sorted list to num dictionary"""
num = dict(sorted(count.items(), key=lambda x: x[1], reverse = True))

""" print each item(k & V) occurance in the num list"""
for k, v in num.items():
    print(k,v)
