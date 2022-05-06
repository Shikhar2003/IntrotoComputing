# Question 1
_string= "Python is a case sensitive language"
# Part a [Finding the length of input string]
print(len(_string))

# Part b [Reversing the order]
part_b=_string[-1::-1]
print(part_b)

# Part c [Using slice function]
Part_c=_string[10:26]
print(Part_c)

# Part d [Replacing a part of string]
part_d=_string.replace("a case sensitive", "object oriented")
print(part_d)

# Part e [Finding a]
part_e=_string.find("a")
print(part_e)

# Part f [Removing white spaces]
part_f=_string.replace(" ", "")
print(part_f)



# Question 2 
letter = '''Hey,ABC Here!
My SID is 2110XXXX
I am from XYZ department and my CGPA is Q'''
name=input("Enter your name: ",)
_SID=input("Enter your SID: ",)
department=input("Enter your department: ",)
cgpa=input("Enter your CGPA: ",)
letter=letter.replace("ABC", name)
letter=letter.replace("2110XXXX", _SID)
letter=letter.replace("XYZ", department)
letter=letter.replace("Q", cgpa)
print(letter)



# Question-3
a=56
b=10

# part-a
_part_a=a&b
print("Part a: ", _part_a)

# part-b 
_part_b=a|b
print("Part b: ",  _part_b)

# part-c
_part_c=a^b
print("Part c: ", _part_c)

# part-d
_part_d_1=a<<2
print("First part of Part d:", _part_d_1)
_part_d_2=b<<2
print("Second part of Part d:", _part_d_2)

# part-e
_part_e_1=a>>2
print("First part of Part e: ", _part_e_1)
_part_e_2=b>>4
print("Second part of Part e ", _part_e_2)



# Question-4
statement=input("Enter a statement: ",)
namecount=statement.count("name")
if namecount>= 1 :
 print("Yes")
else:
 print("No")

# Question-5
# The principle is that the sum of any two sides a triangle should be greater than the remaining side then only it will form a triangle
side1=round(float(input('Enter first side : ')))
side2=round(float(input('Enter second side : ')))
side3=round(float(input('Enter third side : ')))
a=side1+side2>side3
b=side2+side3>side1
c=side3+side1>side2
match a,b,c:
    case True,True,True:            # Checking for valid triangle case
        print('Yes')
    case (False,True|False,True|False)|(True,False,True|False)|(True,True,False):           # Checking for invalid triangle case
        print('No')

 #Question-6
  # Get the value of a and b
a, b = map(int, input("Enter the value of a and b:").split())
# a,b=int(input("Enter the value of a and b:"))
# Calculating xor of a and b
num = a ^ b
Count_flipped_bit = 0
# Counting Number of set bit present
while (num != 0):
    num = num & (num - 1)
    Count_flipped_bit += 1
print("Number of bits needed to be flipped to convert a to b is:", Count_flipped_bit)
 

 

