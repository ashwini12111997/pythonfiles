try:
   a= int(input("Please enter the dividend: ")) 
   b= int(input("Please enter the divisor: "))
   c=a/b 
   print(c)
except ValueError:
   print ("The divisor and dividend have to be numbers!") 
except ZeroDivisionError:
   print ("The divisor is zero!")
finally:
   print ("calculation done!")
