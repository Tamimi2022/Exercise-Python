# Do not modify these lines
__winc_id__ = '62311a1767294e058dc13c953e8690a4'
__human_name__ = 'casting'

# Add your code after this line
# Part 1
leek_price = int(2)
print("Leek is " + str(leek_price) + " euro per kilo.")

# Part 2
leek = 'leek 4'
leek_extraction = leek[leek.find(" "):] # Extract from string
#print(leek_extraction) 
#print(type(leek_extraction)) # To see the type 
sum_total = int(leek_extraction) * leek_price # Cast to integer
print(sum_total)

# Part 3
broccoli_price = 2.34
broccoli_order = float('1.6')
#print(type(broccoli_order))
total_price = round(broccoli_price * broccoli_order, 2)
#print(total_price)
print(str(broccoli_order) + "kg broccoli costs " + str(total_price) + "e")