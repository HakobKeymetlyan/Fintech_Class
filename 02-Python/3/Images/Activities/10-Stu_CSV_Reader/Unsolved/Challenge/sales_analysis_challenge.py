# -*- coding: utf-8 -*-
"""Student Do: Sales Analysis.

This script will use the Pathlib library to set the file path,
use the csv library to read in the file, and iterate over each
row of the file to calculate customer sales averages.
"""

# @TODO: Import the pathlib and csv library
from pathlib import Path
import csv

# @TODO: Set the file path
csv_path = Path("/Users/hakobkeymetlyan/Rutgers/Fintech_Class/02-Python/3/Images/Activities/10-Stu_CSV_Reader/Resources/sales.csv")

# @TODO: Initialize dictionary
sales_dict = {}

# @TODO: Open the csv file as an object
with open(csv_path, "r") as csv_file:
    
    # @TODO:
    # Pass in the csv file to the csv.reader() function
    # (with ',' as the delmiter/separator) and return the csvreader object
    csv_reader = csv.reader(csv_file, delimiter = ",")

    # @TODO: Read the header row first (skip this step if there is no header)
    csv_header = next(csv_reader)
    # @TODO: Print the header
    print(csv_header)

    # @TODO: Read each row of data after the header
    for row in csv_reader:
        # @TODO: Print the row
        print(row)
        # @TODO:
        # Set the 'name', 'count', and 'revenue' variables for better
        # readability, convert strings to ints for numerical calculations
        name = row[0]
        count = int(row[1])
        revenue = int(row[2])


        # @TODO: Calculate the average and round to the nearest 2 decimal places
        average = round(revenue/count, 2)


        # @TODO:
        # If name is not already in the analysis dict, initialize the dictionary
        # Else continue to add to the existing key and nested key-value pairs
        if name not in sales_dict.keys():
            sales_dict[name] = {"count": count, "revenue": revenue}
        else:
            sales_dict[name]["count"] += count
            sales_dict[name]["revenue"] += revenue

print(sales_dict)



# @TODO: Set the header for aggregate.csv


# @TODO: Set the path for the aggregate.csv

# @TODO:
# Open the output path as a file and pass into the 'csv.writer()' function
# Set the delimiter/separater as a ','



    # @TODO: Write the header as the first row

    # @TODO:
    # Loop over every key in analysis and write the associated key (name) and
    # nested key-value pairs (metrics)
