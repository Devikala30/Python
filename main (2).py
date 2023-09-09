'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''
def CheckLeap(Year):  

  if((Year % 400 == 0) or  
     (Year % 100 != 0) and  
     (Year % 4 == 0)):   
    print("Given Year is a leap Year"); 
  else:  
    print ("Given Year is not a leap Year")  
Year = int(input("Enter the number: ")) 
CheckLeap(Year)
