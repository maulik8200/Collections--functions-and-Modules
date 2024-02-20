#Q.53 How can you pick a random item from a list or tuple?

import random 
tuple=[(10,2.21),(30,),(40,50,"hello"),(70,"Django"),("yash"),(100)]
tuple=random.choice(tuple)
print(tuple)