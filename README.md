# Drinkmixer
A machine to make cocktails and highballs by pouring ingredients by turn into a glass. 
The glass stands on a weight cell that messures how much (in grams) of each ingredient has been added.
The liquid is forced out of the flasks using air pressure.
The heart of the system is a Raspberry Pi, and supports 18 ingredient liquids (GPIO pin contraintments)

I have built a working prototype (more details in the wiki), that have made about 300 drinks so far.
Each ingredients are within +-3g (but sadly with some outlier errors).

The main script is included and takes command by addig the ingredient number, and amount in gram.
Python3 masterpour ingredientnumber1.amountgram1 ingredientsnumber2.amountgram2
Exsample, Python3 masterpour 04.50 18.100 12.50

More infomation will be added, and the main script will need some more polish.
