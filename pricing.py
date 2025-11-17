def price_rounding(costs, price):
    # Convert the price to a string to work with its decimal places
    str_price = str(price)
    
    # Find the position of the decimal point
    dot_position = str_price.find(".")

    if dot_position != -1 and dot_position + 2 < len(str_price):
        # Extract the hundredth digit from the string
        hundredth_digit = int(str_price[dot_position + 2])

        if 0 < hundredth_digit < 5:
            # If the hundredth digit is between 1 and 4, round up the price
            rounded_price = round(price, 2) + (5 - hundredth_digit) / 100
        elif 5 < hundredth_digit <= 9:
            # If the hundredth digit is between 6 and 9, round down the price
            rounded_price = round(price, 1)
        else:
            # If the hundredth digit is 5, no rounding is needed
            rounded_price = float(price)
    else:
        # If there are no decimal places or only one decimal place, return the original price
        rounded_price = float(price)

    # check if profit is less than $0.10 add $0.10 to the price only if cost is greater than $0.10
    if rounded_price - costs < 0.1 and costs > 0.1:
        rounded_price += 0.1

    return rounded_price

# # Input the cost and markup percentage
# cost = float(input("Cost: $"))
# markup = float(input("Markup (%): ")) / 100

# # Calculate the price before rounding
# price = round(cost + cost * markup, 2)

# # Round the price using the custom rounding function
# price = price_rounding(cost, price)

# # Calculate the profit
# profit = round(price - cost, 2)

# # Display the results
# print(f"\nCost: ${cost:.2f}")
# print(f"Markup: {markup * 100:.0f}%")
# print(f"Price: ${price:.2f}")
# print(f"Profit: ${profit:.2f}")