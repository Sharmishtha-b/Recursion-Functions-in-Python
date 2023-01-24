# sum of n sums
def sum1(n):
    if n==1:
        return 1
    else:
        return (n+sum1(n-1))
    
#fibonacci
def fib(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return(fib(n-1)+fib(n-2))

#reverse string
def revstri(str1):
    len1=len(str1)
    if len1==1:
        return str1[0]
    else:
        return(str1[-1]+revstri[str[:-1]])

#factorial
def factorial(x):
    if x == 1:
        return 1
    else:
        return (x * factorial(x-1))

#prime number
def isPrime(n, i = 2):
    if (n <= 2):
        return True if(n == 2) else False
    if (n % i == 0):
        return False
    if (i * i > n):
        return True
    return isPrime(n, i + 1)

#palindrome
def is_palindrome(s):
    if len(s) < 1:
        return True
    else:
        if s[0] == s[-1]:
            return is_palindrome(s[1:-1])
        else:
            return False

#special triangle
def spltriangle(A): 
        if (len(A) < 1): 
            return
        temp = [0] * (len(A) - 1) 
        for i in range( 0, len(A) - 1): 
          
            x = A[i] + A[i + 1] 
            temp[i] = x 
        spltriangle(temp) 
        print(A) 
      
#binary search 
def binary_search(lst,low,high, val):  
    if high >= low:
        mid = (high + low) // 2
        if lst[mid] == val: 
            return mid 
        elif lst[mid] > val: 
            return binary_search(lst, low, mid - 1, val) 
        elif lst[mid]<val: 
            return binary_search(lst, mid + 1, high, val) 
        else:
            return -1

#counting no of digits
def countDigit(n): 
    if n == 0: 
        return 0
    return 1 + countDigit(n // 10)

#find the largest number in the list
def Max(lst):
    if len(lst) == 1:
        return lst[0]
    else:
        m = Max(lst[1:])
        return m if m > lst[0] else lst[0]
  
#main
print("1.SUM")
print("2.FIBONACCI")
print("3.REVERSE STRING")
print("4.FACTORIAL")
print("5.PRIME")
print("6.CHECK PALINDROME ")
print("7.SPECIAL TRIANGLE")
print("8.BINARY SEARCH")
print("9.COUNTING NO OF INTEGERS")
print("10.MAX NUMBER IN A LIST")
ch=int(input("Enter your choice : "))
if ch==1:
    n=int(input("enter no : "))
    print("The sum of the numbers is",sum1(n))
if ch==2:
    n=int(input("enter no : "))
    print("the number at",n,"position in the fibonacci series is",fib(n))
if ch==3:
    str1=input("Enter string: ")
    print("The reverse of the string is",revstri(str1))
if ch==4:
    x=int(input("enter no : "))
    print("The factorial is ",factorial(x))
if ch==5:
    n=int(input("Enter number to check whether prime or not : "))
    if (isPrime(n)):
        print("Yes, number is a prime number")
    else:
        print("Number is not a Prime number ")
if ch==6:
    a=str(input("Enter string:"))
    if (is_palindrome(a) ==True):
          print("String is a palindrome")
    else:
          print("String is not a palindrome ")
if ch==7:
          A=list(eval(input("Enter list : ")))
          print(spltriangle(A))
if ch==8:
    lst=list(eval(input("Enter list: ")))
    val=(int(input("Enter value to be searched: ")))
    x=binary_search(lst,0,len(lst)-1,val)
    if x==1:
         print("The number is not found")
    else:
         print("The number is found at", x+1)
if ch==9:
    n=int(input("Enter number: "))
    print("The number of digits in",n,"are",countDigit(n))
if ch==10:
    lst=list(eval(input("Enter numbers of the list: ")))
    print("The largest number is ",Max(lst))

   
        
