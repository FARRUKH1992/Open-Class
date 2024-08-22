Pi_value = 3.14
userAge = 25
user_location = "New York"
MAXLIMIT = 1000


# Define initial amount and yearly interest rate
initial_amount = 10000  # Example: $10,000
interest_rate = 0.07    # 7% interest rate

# Calculate the total amount after one year
total_amount = initial_amount * (1 + interest_rate)

# Print the result
print("Total amount after one year: ${:.2f}".format(total_amount))


# Define prices of the items
price_bread = 2.50      # Example price for bread
price_peanut_butter = 3.75  # Example price for peanut butter
price_jelly = 1.99      # Example price for jelly

# Calculate the total cost
total_cost = price_bread + price_peanut_butter + price_jelly

# Print the result
print("Total cost of bread, peanut butter, and jelly: ${:.2f}".format(total_cost))



# Define the variables
Pi_value = 3.14
userAge = 25
user_location = "New York"
MAXLIMIT = 1000

# Print statements using the variables
print(f"Pi is approximately {Pi_value}.")
print(f"The user is {userAge} years old and lives in {user_location}.")
print(f"The maximum limit is set to {MAXLIMIT}.")

# Calculate the area of a circle using Pi_value
radius = 5
area_of_circle = Pi_value * radius ** 2
print(f"The area of a circle with radius {radius} is {area_of_circle:.2f}.")

# Check if a value exceeds the MAXLIMIT
value = 1500
if value > MAXLIMIT:
    print(f"The value {value} exceeds the maximum limit of {MAXLIMIT}.")
else:
    print(f"The value {value} is within the maximum limit.")