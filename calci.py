def add(P, Q):       
   return P + Q   
def subtract(P, Q):      
   return P - Q   
def multiply(P, Q):      
   return P * Q   
def divide(P, Q):       
   return P / Q      
print ("Please select the operation.")    
print ("a. Add")    
print ("b. Subtract")    
print ("c. Multiply")    
print ("d. Divide")    
c1 = True
while c1:
   choice = input("Please enter choice (a/ b/ c/ d): ") 
   c1 = choice in ["a","b","c","d"] 
   if len(choice) == 0:
      c1 = not c1
   c1 = not c1

   if c1:
      print('invalid input')
b1 = True
while b1:
   try:
      num1 = float(input ("Please enter the first number: ").replace(' ', ''))
      b1 = False
   except:
      print('not a number')
b2 = True
while b2:
   try:
      num2 = float(input ("Please enter the second number: ").replace(' ', ''))    
      b2 = False
   except:
      print('not a number')
if choice == 'a':    
   print (num1, " + ", num2, " = ", add(num1, num2))    
    
elif choice == 'b':    
   print (num1, " - ", num2, " = ", subtract(num1, num2))    
    
elif choice == 'c':    

   print (num1, " * ", num2, " = ", multiply(num1, num2))    
elif choice == 'd':    
   
   print (num1, " / ", num2, " = ", divide(num1, num2))    
