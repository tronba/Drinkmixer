# Drinkmixer
A machine to make cocktails and highballs by pouring ingredients by turn into a glass. 
The glass stands on a weight cell that measures how much (in grams) of each ingredient has been added.
The liquid is forced out of the flasks using air pressure.
The heart of the system is a Raspberry Pi and it supports 18 ingredient liquids (GPIO pin constraints)

I have built a working prototype (more details in the wiki) that has made about 300 drinks so far (from 30 recipes).
Each ingredient is within +-3g (but sadly, with some outlier errors).

The main script is included and takes command by adding the ingredient number, and amount in gram.
Python3 masterpour ingredientnumber1.amountgram1 ingredientsnumber2.amountgram2
Exsample, Python3 masterpour 04.50 18.100 12.50

More information will be added, and the main script will need more polish.
