# # Created by: Hamza Salman
# Course: ICS3U
# Created on: September 2016
# factorial program with 4 loops

print ('enter a number')
number = raw_input()
answer = 1

number = int(number) + 1
for i in range(1, number):
    answer = answer * i
print ('the factorial is ') + str(answer)
