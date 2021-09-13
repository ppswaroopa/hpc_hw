import numpy as np
import sys


# Question 1

def q1():
    sev_by_fiv = []
    for i in range(2000, 3201):
        if i % 7 == 0 and i % 5 != 0:
            sev_by_fiv.append(i)
    return sev_by_fiv


q1_ans = q1()
for j in range(len(q1_ans)):
    print(q1_ans[j], ',', end=" ")


# Question 2

def q2(n):
    if n < 0:
        return False
    elif n == 0:
        return False
    else:
        f = 1
        for k in range(1, n + 1):
            f = f * k
        return f


fact = int(input("Enter a number: \n"))
print('Factorial of number', fact, 'is', q2(fact))


# Question 3

def q3(num):
    gen_dict = {}
    for i in range(1, num + 1):
        gen_dict[i] = i * i
    return gen_dict


print(q3(int(input("Enter a number \n"))))

# Question 4

in_list = input("Enter comma separated values: \n").split(',')
out_tuple = tuple(in_list)
print(in_list)
print(out_tuple)


# Question 5

class QuestionFive:

    def getString(self):
        return str(input("Enter string: \n"))

    def printString(self, var):
        print(var.upper())


ques5 = QuestionFive()
printing = ques5.getString()
ques5.printString(printing)

# Question 6

ques6 = input("Enter comma separated value: \n").split(',')
C = 50
H = 30
ans6 = []
for l in range(len(ques6)):
    q = np.sqrt((2 * C * int(ques6[l])) / H)
    ans6.append(int(q))
for m in range(len(ans6)):
    print(ans6[m], ',', end=" ")

# Question 7


ques7 = input("\nEnter two comma separated value: \n").split(',')
ans7 = []
for n in range(int(ques7[0])):
    t = []
    for o in range(int(ques7[1])):
        t.append(n * o)
    ans7.append(t)
print(ans7)

# Question 8


ques8 = input("\nEnter comma separated words: \n")
split_words = ques8.split()
split_words.sort()
for split_words in split_words:
    print(split_words, ',', end=" ")

# Question 9

print('\nEnter lines: \n')
lines = []
while True:
    line = input()
    if line:
        lines.append(line)
    else:
        break
ques9 = '\n'.join(lines)
print(ques9.upper())

# Question 10

ques10 = input("Enter input:\n")
output = ques10.split()

new_set = {x.replace('', '').replace('', '') for x in output}
print(sorted(new_set))



