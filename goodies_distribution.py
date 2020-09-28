# Read the file
input_file  = open("goodiesinput/input.txt")
print("Reading File")

# Initialize varaibles
prices_dict = dict()
no_of_employees = 0
diff_prices = []

# Convert prices information to dictionary.
for line in input_file:
    col_pos = line.find(":")
    if col_pos == -1: continue
    if line[:col_pos].strip() == "Goodies and Prices": continue
    if line[:col_pos].strip() == "Number of employees":
        no_of_employees = int(line[col_pos+2:].strip())
        continue
    prices_dict[line[:col_pos].strip()] = int(line[col_pos+2:].strip())

# Sort the dictionary according to price and store it in a list
prices_list = [(item, price) for item, price in sorted(prices_dict.items(), key=lambda item: item[1])]


# Calculate the price differences to choose the lowest price difference between highest and lowest

for item in range(0,len(prices_list)-no_of_employees):
    diff_prices.append((prices_list[item+(no_of_employees)-1][1] - prices_list[item][1], item, item+((no_of_employees)-1)))
diff_prices = sorted(diff_prices)


# Save the output in the file
with open('goodiesoutput/output.txt','w+') as output_file:
    output_file.write("The goodies selected for distribution are:\n\n")
    for item in range(diff_prices[0][1], diff_prices[0][2]+1):
        output_file.write("{}: {}\n".format(prices_list[item][0], prices_list[item][1]))
    output_file.write("\nAnd the difference between the chosen goodie with highest price and the lowest price is {}".format(diff_prices[0][0]))
print("Please check output.txt file for the results")
