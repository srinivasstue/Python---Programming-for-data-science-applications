# Mathematicsl operations

# understanding the precendence of operations

a = (13+4)*4-5

b = 20+(3*5)//5

c = 50/10+(100*2)

print('The values from the operations are:',a,b,c)

###############################################################################

# String operations

# count operation on a string

str1 = str(input('Enter a string: '))

str2 = str(input('Enter an alphabet to find out how many times it has appeared in the string: '))

cnt = str1.count(str2)

print("No of times the alphabet has appeared in the chosen word: ",cnt)

# count operation on integers

a = str(input('Enter your mobile number: '))

b = str(input('Enter a number to find out how many times it has appeared: '))

c = a.count(b)

print("No of times the chosen number appears in your mobile number: ",c)

# Find and accessing operations in a string


st1 = str(input('Enter a word: '))

st2 = str(input('Enter the alphabet that you want to access: '))

wrd = st1.find(st2)

print('The alphabet you wanted to access is: ',st1[wrd])
print('The alphabet can be found at the index: ',wrd)

##################################################################################

# Fibonacci series using While loop

z = int(input('Enter the number within which the fibonacci series has to be generated: '))

x = 0

y = 1

count = 0

while count < z:

    print(x,end = '\n')
    
    v = x + y

    x = y

    y = v

    count += 1
################################################################################

# Factorial using for loop

num = int(input('Enter the number for which the factorial must be computed: '))

i = 0

n = 1

for i in range(0,num,1):

    n = n*num

    num = num - 1

    i += 1

print(n)
#################################################################################



          
