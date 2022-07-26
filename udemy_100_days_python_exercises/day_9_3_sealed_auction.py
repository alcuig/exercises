from day_9_3_gavel import logo 
#HINT: You can call clear() to clear the output in the console.

print(logo)
print("Welcome to the secret auction program.")
name_bid_dict = {}
stop_pls= False #to break loop that adds "name":bid into dictionary

while stop_pls == False: #alternatively, 'while not stop_pls:'
    name = input("What is your name? ")
    bid = int(input("What is your bid? $")) 
    #Transforms user entry into int
    print(bid)
    name_bid_dict[name]= bid #adds "name":bid into dictionary
    bidders = input("Are there other bidders? Type 'yes' or 'no'.") #loop continues if user enters "yes"

    if bidders == "no":
        stop_pls= True #breaks loop
    
# vvv loop through dictionary to find highest bid
for name in name_bid_dict: 
    winning_bid = 0 #creates empty value to compare other bids
    if name_bid_dict[name] > winning_bid: #if the bidder has made a bid higher than the highest value, 
        winner = name  #it will create a variable called winner, which stores the name of the winning bidder
                       #which it will use in the print message below to retrieve the winning bid in the name:bid dictionary.

     
print(f"The winner is {winner} with a bid of ${name_bid_dict[winner]}")



