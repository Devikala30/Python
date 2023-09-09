'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

def factorial(n):
    return 1 if (n==1 or n==0) else n * factorial(n-1);
 
n = int(input("Enter input number : "))
 
print("The factorial of",n,"is",factorial(n))