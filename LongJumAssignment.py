
import math # I imported the "math" module that I use later to round the decimals.

Competitorname = input ("Enter your name: ") # Here I made an input to get the user's name to use later on

Jump1 = float(input("Enter Jump 1 Length: ")) # These 4variables are getting the users input on their long jump distance. They will be stored in a list later to easily do all the rest of the steps.
Jump2 = float( input("Enter Jump 2 Length: "))
Jump3 = float( input("Enter Jump 3 Length: "))
Jump4 = float(input("Enter Jump 4 Length: "))


#I have used the float function so decimals are compatible.
Jumplengths = [float(Jump1), float(Jump2), float(Jump3), float(Jump4)] # Now I am compiling all the data of the jump lengths that I got via the user inputs, and making it into a list via using a square bracket. I make it into a variable so I can use it in the next steps.
# The main reason I converted this into a list is so I can easily remove the lowest number via using the .remove function as seen below.
Jumplengths.remove(min(Jumplengths))

# Next I use the math.fsum function (imported from earlier) and get the sum of the 3 largest numbers. At first I used the normal sum function but it didn't work with float numbers, which is why I imported that module.
sumOfJumps = (math.fsum(Jumplengths)) # I create another variable called "sumOfJumps" just to make things easier for the next steps.
# Next, I create a new variable called "AverageofJumps" which divides the sumOfJumps (as seen above) by 3 to get the average/mean.
AverageofJumps =  (sumOfJumps / 3)



# And lastly I make a variable called "twodecimals" where I use the round function and take the above variable and make sure the sum of it is rounded to TWO decimals. At first I just tried doing "round(AverageofJumps, 2)" but that wasn't working so I experimented and made a new variable to round with.
twodecimals = round(AverageofJumps, 2)

print (Competitorname + " scored " + str(twodecimals) + " in the long jump competition. ") # And lastly I put it all together. Also added the "str" function so that it would be able to print as a string.





