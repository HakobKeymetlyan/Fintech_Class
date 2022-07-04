# -*- coding: utf-8 -*-
"""
Student Activity: Market Capitalization.

This script showcases the use of Python Dicts to determine the
bank names associated with the corresponding market cap ranges.
"""

# Banks and Market Caps
#-----------------------
# JP Morgan Chase: 327
# Bank of America: 302
# Citigroup: 173
# Wells Fargo: 273
# Goldman Sachs: 87
# Morgan Stanley: 72
# U.S. Bancorp: 83
# TD Bank: 108
# PNC Financial Services: 67
# Capital One: 47
# FNB Corporation: 4
# First Hawaiian Bank: 3
# Ally Financial: 12
# Wachovia: 145
# Republic Bancorp: .97

# @TODO: Initialize a dictionary of banks and market caps (in billions)


banks = {
    "JP Morgan Chase": 327,
    "Bank of America": 302,
    "Citigroup": 173,
    "Wells Fargo": 273,
    "Goldman Sachs": 87,
    "Morgan Stanley": 72,
    "U.S. Bancorp": 83,
    "TD Bank": 108,
    "PNC Financial Services": 67,
    "Capital One": 47,
    "FNB Corporation": 4,
    "First Hawaiian Bank": 3,
    "Ally Financial": 12,
    "Wachovia": 145,
    "Republic Bancorp": .97
    }


# @TODO: Change the market cap for 'Citigroup'
banks['Citigroup'] = 170

# @TODO: Add a new bank and market cap pair
banks["American Express"] = 33

# @TODO: Remove a bank from the dictionary
del banks["Wachovia"]

# @TODO: Print the modified dictionary

#initializing variables
total_market_cap = 0
bank_count = 0
avg_market_cap = 0

maximum_value = 0
maximum_key = ""
minimum_value = 0
minimum_key = ""


#Lists
mega_caps = []
large_caps = []
mid_caps = []
small_caps = []

for bank_name, market_cap in banks.items():
    print(f"Name: {bank_name} | Market Cap: {market_cap}")
print("----------------------------")



for bank_name, market_cap in banks.items():
    
  

    total_market_cap += int(market_cap)
    bank_count += 1

    # creating minimum values
    if minimum_value == 0:
        minimum_value = market_cap
        minimum_key = bank_name
    elif market_cap < minimum_value:
        minimum_value = market_cap
        minimum_key = bank_name


    # creating maximum values
    if market_cap > maximum_value:
        maximum_value = market_cap
        maximum_key = bank_name
    
    # finding average
    avg_market_cap = round(total_market_cap/bank_count, 2)

    # grouping banks

    if market_cap >= 300:
        mega_caps.append(bank_name)
    elif market_cap >= 10 and market_cap < 300:
        large_caps.append(bank_name)
    elif market_cap >= 2 and market_cap < 10:
        mid_caps.append(bank_name)
    elif market_cap < 2:
        small_caps.append(bank_name)




print(f"Total Market Capitalization: {total_market_cap}")
print(f"Total Numer of Banks: {bank_count}")
print(f"Average Market Capitalization: {avg_market_cap}")
print(f"Largest Bank: {maximum_key}")
print(f"Smallest Bank: {minimum_key}")
print("------------------------------------------------")
print(f"Mega Cap Banks: {mega_caps}")
print(f"Large Cap Banks: {large_caps}")
print(f"Mid Cap Banks: {mid_caps}")
print(f"Small Cap Banks: {small_caps}")