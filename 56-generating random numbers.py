#Q.56 How will you set the starting value in generating random numbers?
# ans:->The random number generator needs a number to start with (a seed value), 
#       to be able to generate a random number. By default the random number generator
#       uses the current system time. Use the seed() method to customize the start number of the random number generator.

A=random.randrange(1,5) 
print(A)