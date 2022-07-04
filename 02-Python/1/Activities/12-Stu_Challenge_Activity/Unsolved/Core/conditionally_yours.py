"""
Conditionally Yours

Pseudocode:


"""

# Increase = Current Price - Original Price
# Percent Increase = Increase / Original x 100

# Create integer variable for original_price
original_price = 200

# Create integer variable for current_price
current_price = 300

# Create float for threshold_to_buy
threshold_to_buy = 10

# Create float for threshold_to_sell
threshold_to_sell = 3

# Create float for portfolio balance
balance = 5000



# Create string for recommendation, default will be buy

# Calculate difference between current_price and original_price
difference = current_price - original_price

# Calculate percent increase
percent_change = (difference/original_price)*100


# Print original_price
print(f"Netflix's original stock price was ${original_price}")

# Print current_price
print(f"Netflix's current stock price is ${current_price}" )

# Print percent increase
print(f"The percent increase is {percent_change}%")

# Determine if stock should be bought or sold
if percent_change > threshold_to_buy and balance >= 5*current_price:
    print("Buy!!")
elif percent_change < threshold_to_sell:
    print("Sell!!")
else: print("Hold")

