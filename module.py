# def add(a,b):
#     return a+b


# def multi(a,b):
#     return a*b


# def sub(a,b):
#     return(a-b)

# def div(a,b):
#     return(a/b)

# print('hello' + __name__)


# x = int(input('The value of x is: '))

# if x%2==0:
#     print('even')


# else:
#     print('odd')

# a = int(input('The value of a is: '))
# b = int(input('The value of b is: '))
# c = bool(input('The flag is: '))

# if (a >=0) != (b >=0) and not c:
#     print('true')


# if a < 0 and b < 0 and c:
#     print('true')


# else:
#     print('false')



# def check_status(a, b, flag):

#     if (a >= 0) != (b >= 0) and not flag:
#         return True
    

#     if a < 0 and b < 0 and flag:
#         return True
    
#     else:
#         return False


# # p rint(check_status(5,-3, False))


# print(check_status(5, 3, True))


# a  = bool(input('Is john angry ? : ' ))

# b  = bool(input('Is smith angry ? : ' ))

# if a == True and b == True:
#     print('Trouble')
#     print('True')



# elif a == False and b == False:
           
          
#     print('Trouble')
#     print('True')


# else:
#     print(False)


# def agry_lvl(j_angry, s_angry):

#     if j_angry == s_angry:
#         return True
    
#     return False


# print(agry_lvl(True, True))

# print((agry_lvl)(False, False))

# print(agry_lvl(True, False))



# x = [1,2,3,4,5,6,7,8,9]

# for i in x:
    # print max(x)

# import array


# x = array('i'[1,2,3,4,5,6,7,8,9])

# print(x)



# from array import*

# x = array('i',[1,2,3,4,5])

# print(x)






# x = [1,3,4,5,6,7,8,9]


# def lrg(x):

#     lrg = x[0]
#     for i in x:
#         if i > lrg:
#             lrg = i
#     return lrg
        

# print(lrg(x))




# question 1

x = [3,5,7,22,56,91,455]


def lrg(arr):

    lrg = arr[0]
    for i in arr:
        if i > lrg:
            lrg = i
    return lrg



print(lrg(x))





# question 2

x = [2,4,6,12,45,69,45,65]

def sml(arr):

    sml = arr[0]
    for i in arr:
        if i < sml:
            sml = i

    return sml

print(sml(x))






# a = [1,2,3,4,5,6,7,8,9]

# def rev(a):

# def large(arr):
    
#     large = arr[0]
#     for i in arr:
#         if i > large:
#             large = i
#     return large

# print(large(a))



# question 3

a = [1,2,3,4,5,6,7,8,9]


def rev(arr):

    arr.reverse()
    return arr
    # return arr[::-1]

print(rev(a))


b = [1,2,3,4,5,6,7,8,9]


def rev(arr):

    rev_arr = []

    for i in range(len(arr) - 1, -1, -1):
        rev_arr.append(arr[i])

    return rev_arr

print(rev(b))


def rev(arr):
    for i in reversed(arr):
        print(i)
    

print(rev(b))


# question 4

print(sum(x))



def add(arr):
    sum = 0
    for i in arr:
        sum += i
    return sum
    

print(add(x))


# question 5

def dup(arr):
    
    x = set()
    result = []
    for i in arr:
        if i not in x:
            result.append(i)
            x.add(i)
    return result

print(dup(x))



# question 6





# question 7

def count(arr,num):
    count = 0
    for i in arr:
        if i == num:

            count = count+1
    return count

print(count(x,7))

# question 8

def index(arr,num):
     
    for i in range(len(arr)):

    # for i in range(len(arr)):
        if arr[i] == num:
            return i
    return -1

print(index(x,9))

# question 9

def second_largest(arr):
    largest = second = float()
    
    for i in arr:
        if i > largest:
            largest = i
        elif largest > i > second:
            second = i
    
    return second

array = [4, 2, 9, 7, 9, 3]
print(second_largest(array)) 


# abhi theek se nhi aaya ^^9

#  question 10

c = [1, [2, [3, 4], 5], [6, 7], 8]



def flatten(arr):
    lst = []

    for i in arr:
        if isinstance(i,list):
            lst.extend(flatten(i))
        else:    
            lst.append(i)

    return lst

print(flatten(c))


# question 11

# question 12

a = [1,2,3,4,5,6,7,8,9]
b = [2,4,6,8]


def common(arr1,arr2):

    arr = set(arr1) & set(arr2)
    return list(arr)

print(common(a,b))


#  using loop


def common(arr1,arr2):
    arr = []

    for i in arr1:
        if i in arr2 and i not in arr:
            arr.append(i)

    return arr

print(common(a,b))



#  question 13

def remove(arr,elm):
    edit = []

    for i in arr:
        if i != elm:
            edit.append(i)

    return edit


print(remove(x,5))



# question 14

def unique(arr):

    x = set()

    for i in arr:
        if i in x:
            return False
        x.add(i)
    return True
    
print(unique(a))

# question 15

def merg(arr1, arr2):
    new = []
    a, b = 0, 0

    for i in range(len(arr1) + len(arr2)):
        if a < len(arr1) and (b >= len(arr2) or arr1[a] < arr2[b]):
            new.append(arr1[a])
            a += 1
        else:
            new.append(arr2[b])
            b += 1

    return new



x = [1,3,5,7]
y = [2,4,6,8]


print(merg(x,y))





# question 16

x = [1,2,3,4,5,6,7,9]


def missing(arr):
    for i in arr:
        if i+1 not in arr :
            return i+1
    return None


print(missing(x))


# question 17

x = int(input('enter a number: '))
count = 0
for i in range(1,x+1):
    if x%i==0:
        count += 1

if count == 2:
    print('prime')

else:
    print('not prime')


# print table of n

x = int(input('enter the value of n: '))
for i in range(1,11):
    y = x*i
    print(y)


# print all elements in one line
lst = ['one','two','three','four','five']

def one_line(arr):
    for i in arr:
        print(i,end=" ")
    return ' '



print(one_line(lst))
print()

# factorial
def fac(x):
    fac = 1
    for i in range(1,x+1):
        fac *= i
    print(fac)
    return ' '
    
print(fac(6))


# reversal string

x = [1,2,3,4,5,6,7,8,9]

y = []
for i in reversed(x):
    y.append(i)
print(y)


# fibonacci sequence

x = int(input('enter the no. of terms: '))

a,b = 0,1
for i in range(x):
    print(a, end = ' ')
    a, b = b , a+b



# count vovels

def vov(str):
    count = 0
    for i in str:
        if i in 'aeiou':
            count += 1

    print(count)
    return ' '
print(vov('my name is dhruv kumar'))

print(vov('aeiou'))



# sum of array

x = [1,2,3,4,5,6,7,8,9]

def sum(arr):
    sum = 0
    for i in arr:
        sum += i
    return sum

print(sum(x))

# maximum from an array

x = [1,2,3,4,5,6,7,8,9]

def max_num(arr):
    maximum = arr[0]
    for i in arr:
        if i > maximum:
            maximum = i

    return maximum

print(max_num(x))


# count even numbers in an array

x = [23,42,35,53,64,57,75,54,42,26,68]

def even(arr):
    count = 0
    for i in arr:
        if i%2 == 0:
            count += 1

    return count

print(even(x))

# table of n

n = int(input('enter the number: '))
for i in range(1,11):
    print(f"{n} x {i} = {n*i}")


# calculate sum of n natural numbers

def sum_n():
    n = int(input('enter the number: '))
    count = 0
    for i in range(n+1):
        count += i
    return count


print(sum_n())

# count vovel

def count_vovel():
    x = str(input('Enter your string: '))
    count = 0
    for i in x:
        if i in 'aeiou':
            count += 1

    return count

print(count_vovel())

# palindrome

def pln():
    x = str(input('Enter your sring: '))

    for i in x:
        # print(i, end='') 
        continue

    for v in reversed(x):
        # print(v, end='')
        continue

    if i == v:
         print('palindrome')
    else:
         print('non palindrome')

    return ' '


print(pln())

# flat the given array

a = [1,2,3,[4,5],8,[9]] 
# expected output = [1,2,3,4,5,8,9]


def flatten(arr):
    flat = []
    for i in arr:
        if isinstance(i,list):
            for y in i:
                flat.append(y)
        else:
            flat.append(i)        
    return(flat)

print(flatten(a)) 

 
# Write a program to print the square of numbers from 1 to 10

x = [1,2,3,4,5,6,7,8,9]

for i in x:
    print(i*i, end=(' '))



# Count how many times a specific character appears in a string

x = ('my name is dhruv')

def count_vov(str):
    count = 0
    for i in str:
        if i in 'aeiou':
            count += 1
    return count

print(count_vov(x))

# find maax , min from list

x = [1,2,3,4,5,6,7,8,9]

def max_min(x):
    maximum = x[0]
    minimum = x[0]

    for i in x:
        if i > maximum:
            maximum = i
        if i < minimum:
            minimum = i

    return maximum, minimum


print(max_min(x))

# Remove all even numbers from a list

x = [1,2,3,4,5,6,7,8,9,10]

def rmv_even(arr):
    for i in arr:
        if i%2 != 0:
            print(i)

print(rmv_even(x))


# Create a new list that contains the square of each element from the original list

x = [1,2,3,4,5,6,7,8,9,99]

def square_num(arr):
    sqr = []
    for i in arr:
        sqr.append(i*i)
    return sqr

print(square_num(x))


# check prime

x = int(input('enter the number: '))
count = 0

for i in range(1,x+1):
    if x%i == 0:
        count += 1

if count == 2:
        print('prime')
else:
        print('no prime')

# factorial

x = int(input('enter the number: '))

fact = 1
for i in range(1,x+1):
    fact *= i
print(fact)

# count frequency

x = [1,2,3,4,2,5,6,7,89,6,4,3,2,4,5,6,4,5,4,5,4,3,4,5,6,7,8,65,4,3,4,5]

def count(arr,y):
    count = 0
    for i in arr:
        if i == y:
            count += 1
    return count
print(count(x,4))

# convert to capital

x = ('My name is dhruv')

def to_uppercase(str):
    result = ('')
    for i in str:
        if 'a' <= i <= 'z':
            result += chr(ord(i) - 32)
        else:
            result += i
    return result

print(to_uppercase(x))

# q1 square


for i in range(1, 6):
    for j in range(1,6):
        print('*', end=" ")
    print()


# q2 left aligned triangle

for i in range(1,6):
    for i in range(1, i+1):
        print('*', end=" ")
    print()

# q3 right aligned triangle

x = 5

for i in range(1,x+1):
    for j in range(1,x+1):
        if j <= x-i:
            print(' ', end=' ')
        else:
            print('*', end=' ')
    print()

# q4 Inverted Right-Angled Triangle (Left-Aligned)

for i in range(x, 0, -1):
    for j in range(1, i+1):
        print('*', end=" ")
    print()

# q5 Inverted Right-Angled Triangle (Right-Aligned)

x = 5
for i in range(5, 0, -1):
    for j in range(1, x+1):
        if j <= x-i:
            print(' ', end=' ')
        else:
            print('*', end=' ')
    print()

# q6 Pyramid Pattern

x = 5

for i in range(1, x + 1):
    spaces = '  ' * (x - i)
    stars = ' *' * (2 * i - 1)
    print(spaces + stars)

# q7 Inverted Pyramid

x = 5

for i in range(5, 0, -1):
    spaces = '  ' * (x - i)
    stars = ' *' * (2 * i - 1)
    print(spaces + stars)


# q8 Hollow Square

x = 5
for i in range(x):
    for j in range(x):
        if i == 0 or i == x-1 or j == 0 or j == x-1:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()

# q9 Hollow Right-Angled Triangle (Left-Aligned)

x = 5
for i in range(1, x+1):
    for j in range(1, i+1):
        if j == 1 or j == i or i == x:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()

# q10 Half Pyramid Using Numbers

x = 5
for i in range(1, x+1):
    for j in range(1, 1+i):
        print(j, end=' ')
    print()

# q11 Full Diamond

x = 5
for i in range(1,x+1):
    spaces = '  ' * (x - i)
    stars = ' *' * (2 * i - 1)
    print(spaces + stars)

for i in range(4, 0, -1):
    spaces = '  ' * (x - i)
    stars = ' *' * (2 * i - 1)
    print(spaces + stars)

# q12 second largest

x = [5,35,76,24,45,74,76,16,47,86,45]

def sec_largest(arr):
    largest = 0
    second = 0
    for i in arr:
        if i >= largest:
            second = largest
            largest = i
        elif largest > i > second:
            second = i
    return second


print(sec_largest(x))

# q13

x = [1,1,1,2,2,2,3,3,3,4,4,5,5,6]

def frequency(arr):
    count = {}
    for i in arr:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    return count

print(frequency(x))

# q14

x = [6,3,76,3,6,97,54,345]

def sec_largest(arr):
    largest = 0
    second = 0
    for i in arr:
        if i > largest:
            second = largest
            largest = i
        elif largest > i > second:
            second = i
    return second

# q15

x = [1,2,3,4,3,2,1]

def is_pallendrome(arr):

    count = 0
    for i in range(len(arr)//2):
        count += 1

        if arr[i] == arr[len(arr)-count]:
            return 'your array is pallendrome'
        return 'your array is not pallendrome'


print(is_pallendrome(x))


# at index 5th add value 50

x = [0,1,0,2,3,4,5,6,7,8,9]

def add_value(x,index,value):
    x += [0]

    for i in range(len(x) -1,index, -1):
        x[i] = x[i-1]

    x[index] = value

add_value(x,5,50)
print(x)

# Find the minimum element in an array.

x = [5,3,4,7,1,3,8,2,9]

def mini(x):
    min = x[0]
    for i in range(len(x)):
        if x[i] < min:
            min = i

    return min

print(mini(x))

# Find the index of a given element in an array (linear search).

x = [5,3,4,7,1,3,8,2,9]

def find_index(arr, elem):
    for i in range(len(arr)):
        if arr[i] == elem:
            return i

print(find_index(x,1))

# Rotate an array by k steps to the right

x = [5,3,4,7,1,3,8,2,9]

def rotate_right(arr, k):
    n = len(arr)
    k = k % n
    return arr[-k:] + arr[:-k]

print(rotate_right(x,5))

# Rotate an array by k steps to the left

def rotate_left(arr, k):
    n = len(arr)
    k = k % n
    return arr[+k:] + arr[:+k]

print(rotate_left(x,2))

# Find the missing number in an array containing numbers from 1 to n.

x = [1,2,3,5,6]

def missing(n):
    sum_n = n * (n+1)/2
    missing_num = sum_n - sum(x)
    return missing_num

print(missing(6))

# Find the element that appears only once in an array where every other element appears twice.

x = [1,1,2,2,3,3,4,5,5]

def once(arr):
    result = 0
    for i in arr:
        result = result ^ i
    return result

print(once(x))

# Count how many times a particular number appears in an array.

x = [1,2,3,4,5,5,5,5,6,7,8,9]

def count_elem(arr,elem):
    count = 0
    for i in arr:
        if i == elem:
            count += 1
    return count

print(count_elem(x,5))

# Remove duplicates from a sorted array (in-place).

x = [1,2,2,3,4,4,5,6,7,7]

def remove_dupli(arr):
    y = 0
    for i in range(len(arr)):
        if arr[i] != arr[y]:
            y += 1
            arr[y] = arr[i]
    return arr[:y+1]

print(remove_dupli(x))

# Find the maximum product of two integers in an array.

x = [-10,-3,5,5,-2]

def max_prdt(arr):
    arr.sort()

    pdt_1 = arr[-1] * arr[-2]
    pdt_2 = arr[0] * arr[1]

    if pdt_1 >= pdt_2:
        print(pdt_1)
    else:
        print(pdt_2)

print(max_prdt(x))

# # Find the index of the first occurrence of a given element.
x = [1,2,3,4,2,1,4,5,6,5,3,1,6]

def index(arr,elem):
    for i in range(len(arr)):
        if arr[i] == elem:
            return i
        
print(index(x,6))

# Find the index of the last occurrence of a given element.

x = [1,2,3,4,2,1,4,5,6,5,3,1,6]

def index(arr,elem):
    for i in range(len(arr)-1,-1,-1):
        if arr[i] == elem:
            return i
        
print(index(x,6))

# # Count how many elements are greater than a given number x.

x = [1,2,3,4,2,1,4,5,6,5,3,1,6]

def great(arr,num):
    elem = 0

    for i in arr:
        if i > num:
            elem += 1
    return elem

print(great(x,2))

# Count how many elements are smaller than a given number x.

x = [1,2,3,4,2,1,4,5,6,5,3,1,6]

def small(arr,num):
    elem = 0

    for i in arr:
        if i < num:
            elem += 1
    return elem

print(small(x,2))


# Replace all negative numbers in an array with 0

x = [-1,1,-2,2,-3,3,-4,4,-5,5]

def replace(arr):
    for i in range(len(arr)):
        if arr[i] < 0:
            arr[i] = 0

    return arr

print(replace(x))

# Find the sum of elements at even indices and odd indices separately.

x = [1,2,3,4,2,1,4,5,6,5,3,1,6]

def sum_index(arr):
    even = 0
    odd = 0
    for i in range(len(arr)):
        if i%2 != 0:
            even += arr[i]
        else:
            odd += arr[i]
    return even,odd

print(sum_index(x))

# Find the maximum and minimum element in a single traversal.

x = [1,2,3,4,5,6,7,8,9]

def min_max(arr):

    min_elem = max_elem = arr[0]

    for i in arr[1:]:
        if i < min_elem:
            min_elem = i
        elif i > max_elem:
            max_elem = i

    return min_elem, max_elem

print(min_max(x))


# Find the difference between the sum of even numbers and odd numbers in the array.


x = [10, 3, 5, 8, 2, 7, 4]


def difference(arr):
    even_sum = 0
    odd_sum = 0

    for i in arr:
        if i % 2 == 0:
            even_sum += i
        else:
            odd_sum += i

    difference = even_sum - odd_sum
    return difference

print(difference(x))

# Print all elements at even positions (index 0,2,4...)

x = [1,2,3,4,5,6,7,8,9]

def print_even(arr):

    for i in arr:
        if i%2 != 0:
            print(i)


print(print_even(x))


# Print all elements at odd positions (index 1,3,5...)

x = [1,2,3,4,5,6,7,8,9]

def print_even(arr):

    for i in arr:
        if i%2 == 0:
            print(i)


print(print_even(x))

# Count how many pairs in the array have a given sum k.

x = [1,2,3,4,5,6,7,8,9]

def count_pairs(arr, k):
    freq = {}
    count = 0

    for i in arr:
        complement = k - i
        if complement in freq:
            count += freq[complement]

        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1

    return count

print(count_pairs(x,9))


# Count how many pairs in the array have a difference k.

x = [1,2,3,4,5,6,7,8,9]

def count_pairs_with_difference(arr, k):
    y = set(arr)
    count = 0

    for i in arr:
        if i + k in y:
            count += 1

    return count

print(count_pairs_with_difference(x,1))

# Find the element that occurs more than n/2 times (majority element).

def majority_element(arr):
    count = {}
    n = len(arr)

    for i in arr:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
        
        if count[i] > n // 2:
            return i

    return None

x = [3, 2, 3]
print(majority_element(x))

# Find the element that occurs more than n/3 times (extended majority element).

def majority_element(arr):
    count = {}
    n = len(arr)

    for i in arr:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
        
        if count[i] > n // 3:
            return i

    return None

x = [3, 2, 3,3,3]
print(majority_element(x))



# Check if the array contains duplicate elements.

def contains_duplicates(arr):
    x = set()
    for i in arr:
        if i in x:
            return True
        x.add(i)
    return False

x = [1,2,3,4,4,5,6,7]

print(contains_duplicates(x))

# Find the equilibrium index (where left sum = right sum).

def find_equilibrium_index(arr):
    total_sum = 0
    for i in range(len(arr)):
        total_sum += arr[i]
    
    left_sum = 0
    for i in range(len(arr)):
        total_sum -= arr[i]
        
        if left_sum == total_sum:
            return i
        
        left_sum += arr[i]
    
    return -1

arr = [1, 3, 5, 2, 2]
print(find_equilibrium_index(arr))

# Find the second occurrence of a given element (or say it doesn’t exist).

def find_second_occurrence(arr, elem):
    count = 0
    for i in range(0, len(arr)):
        if arr[i] == elem:
            count += 1
            if count == 2:
                return i
    return "Second occurrence does not exist."

x = [1,2,3,4,5,6,5,7,8,9]

print(find_second_occurrence(x,7))

# # Count how many elements are divisible by a given number k.

x = [1,2,3,4,5,6,7,8,9]

def div_k(arr,k):
    count = 0
    for i in arr:
        if i % k == 0:
            count += 1

    return count
    
print(div_k(x,2))

# # Replace all even numbers with their half, and odd numbers with double their value.

x = [1,2,3,4,5,6,7,8,9]

def replace_elem(arr):
    new_arr = []
    for i in arr:
        if i % 2 == 0:
            new_arr.append(i//2)
        else:
            new_arr.append(i*2)
    return new_arr

print(replace_elem(x))


# # Find the product of all elements in the array.

x = [1,2,3,4,5,6,7,8,9]

def product(arr):
    product = 1
    for i in arr:
        product *= i
    return product

print(product(x))

# # Find the average of positive numbers and average of negative numbers separately.

x = [1,-1,2,-2,3,-3,4,-4,5,-5,6,-6,7,-7,8,-8,9,-9]

def average(arr):
    count_positive = 0
    count_negative = 0
    positive = 0
    negative = 0
    for i in arr:
        if i > 0:
            count_positive += 1
            positive += i
        else:
            count_negative += 1
            negative += i
    return positive/count_positive, negative / count_negative

print(average(x))

# # Replace every element with the sum of elements to its left.

def replace(arr):
    running_sum = 0

    for i in range(len(arr)):
        current_value = arr[i]
        arr[i] = running_sum
        running_sum += current_value
    
    return arr

x = [1, 2, 3, 4, 5]
print(replace(x))

# # Replace every element with the product of elements to its right.

x = [1, 2, 3, 4, 5]

def replace(arr):
    running_sum = 1

    for i in range(len(arr) -1, -1, -1):
        current_value = arr[i]
        arr[i] = running_sum
        running_sum *= current_value
    
    return arr

print(replace(x))

# # Print array elements in reverse order without modifying the original array.

arr = [1, 2, 3, 4, 5]
print(arr[::-1])

# # Swap the first and last element of the array.

x = [10, 20, 30, 40, 50]

def swap(arr):
    for i in range(len(arr)):
        if i == 0:
            first = arr[i]
        if i == len(arr) - 1:
            arr[i], arr[0] = first, arr[i]
    return arr

print(swap(x))

# # Swap adjacent elements in pairs (e.g. [1,2,3,4] → [2,1,4,3]).

def swap(arr):
    for i in range(0, len(arr) - 1, 2):
        arr[i], arr[i + 1] = arr[i + 1], arr[i]
    return arr

x = [1, 2, 3, 4]
print(swap(x))

# # Find the maximum difference between consecutive elements.

x = [1,5,2,6,1,9]

def max_diff(arr):

    max_diff = 0
    for i in range(0, len(arr) - 1):
        a = arr[i]
        b = arr[i+1]

        if a>b:
            diff = a - b
        else:
            diff = b - a

        if diff > max_diff:
            max_diff = diff
    return max_diff

print(max_diff(x))


# Find the minimum difference between consecutive elements.

x = [1,5,2,6,1,9]

def min_diff(arr):

    min_diff = float('inf')
    for i in range(0, len(arr) - 1):
        a = arr[i]
        b = arr[i+1]

        if a>b:
            diff = a - b
        else:
            diff = b - a

        if diff < min_diff:
            min_diff = diff
    return min_diff

print(min_diff(x))


# Count how many elements are strictly greater than their neighbors.

x = [1, 5, 2, 6, 1, 9]

def count_greater(arr):
    count = 0

    for i in range(1, len(arr) - 1):
        left = arr[i - 1]
        current = arr[i]
        right = arr[i + 1]
        
        if current > left and current > right:
            count += 1

    return count

print(count_greater(x))

# Find the peak element (element greater than or equal to its neighbors).

x = [1, 5, 2, 6, 1, 9]

def find_peak(arr):
    
    for i in range(1, len(arr) - 1):
        if arr[i] >= arr[i - 1] and arr[i] >= arr[i + 1]:
            return arr[i]
    return None

print(find_peak(x))


