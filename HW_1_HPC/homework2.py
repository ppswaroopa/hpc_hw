import numpy as np


# Question 1

def q1():
    sev_by_fiv = []
    for i in range(2000, 3201):
        if i % 7 == 0 and i % 5 != 0:
            sev_by_fiv.append(str(i))
    return sev_by_fiv


q1_ans = q1()
print("All numbers divisible by 7 but are not multiple of 5 from 2000-3000\n")
print(','.join(q1_ans), '\n')


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


fact = int(input("Enter a number to get the factorial of it: \n"))
print('Factorial of number', fact, 'is', q2(fact))


# Question 3

def q3(num):
    gen_dict = {}
    for i in range(1, num + 1):
        gen_dict[i] = i * i
    return gen_dict


print(q3(int(input("Enter a number to generate a dictionary \n"))))

# Question 4

in_list = input("Enter comma separated values to get a tuple with a list: \n").split(',')
out_tuple = tuple(in_list)
print(in_list)
print(out_tuple)


# Question 5

class QuestionFive:

    def getString(self):
        return str(input("Enter string to test the class implementation: \n"))

    def printString(self, var):
        print(var.upper())


ques5 = QuestionFive()
printing = ques5.getString()
ques5.printString(printing)

# Question 6

ques6 = input("Enter comma separated values to return a value using a formula: \n").split(',')
C = 50
H = 30
ans6 = []
for l in range(len(ques6)):
    q = np.sqrt((2 * C * int(ques6[l])) / H)
    ans6.append(str(int(q)))

print(','.join(ans6))

# Question 7


ques7 = input("\nEnter two comma separated value to return a matrix: \n").split(',')
ans7 = []
for n in range(int(ques7[0])):
    t = []
    for o in range(int(ques7[1])):
        t.append(n * o)
    ans7.append(t)
print(ans7)

# Question 8

print("Enter comma separated words to sort them alphabetically:\n")
ques8 = [s for s in input().split(',')]
ques8.sort()
print(','.join(ques8))

# Question 9

print('\nEnter lines to capitalize: \n')
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

ques10 = input("Enter whitespace separated words to sort and remove duplicates:\n")
output = ques10.split()

new_set = {x.replace('', '').replace('', '') for x in output}
print(sorted(new_set))


# Question 25

class Question25:
    name = "Person"

    def __init__(self, name=None):
        # self.name is the instance parameter
        self.name = name


daniel = Question25("Daniel")
print("%s name is %s" % (Question25.name, daniel.name))

jackie = Question25()
jackie.name = "Jackie"
print("%s name is %s" % (Question25.name, jackie.name))

# Question 36


ques36 = dict()
for t in range(1, 21):
    ques36[t] = t ** 2
for u in ques36.keys():
    print(u)

# Question 37

ques37 = list()
for v in range(1, 21):
    ques37.append(v)
print(ques37)

# Question 43

ques43 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
ans43 = list()
for w in range(len(ques43)):
    if ques43[w] % 2 == 0:
        ans43.append(ques43[w])
ans43_tup = tuple(ans43)
print(ans43_tup)


# Question 51

class American(object):
    pass


class NewYorker(American):
    pass


ini_americ = American()
ini_newy = NewYorker()


# Question 53

class Rectangle(object):
    def __init__(self, l, w):
        self.length = l
        self.width = w

    def area(self):
        return self.length * self.width


ques53 = Rectangle(2, 10)
print(ques53.area())


# Question 54

class Shape(object):
    def __init__(self):
        pass

    def area(self):
        return 0


class Square(Shape):
    def __init__(self, l):
        Shape.__init__(self)
        self.length = l

    def area(self):
        return self.length * self.length


ques54 = Square(3)
print(ques54.area())


# Question 56

def throws():
    return 5 / 0


try:
    throws()
except ZeroDivisionError:
    print("division by zero!")


# Question 94


def ques94(qu):
    ans94 = []
    preserve = set()
    for item in qu:
        if item not in preserve:
            preserve.add(item)
            ans94.append(item)

    return ans94


li = [12, 24, 35, 24, 88, 120, 155, 88, 120, 155]
print(ques94(li))
