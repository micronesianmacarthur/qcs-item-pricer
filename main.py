# main.py

import pandas as pd
from pricing import price_rounding
from datetime import datetime
import os
import sys


def startup():
    if len(sys.argv) < 2:
        # sys.exit("Specify 'sys.argv' argument [get_price, update_table, all]")
        main()
    elif sys.argv[1] == "get_price":
        main()
    elif sys.argv[1] == "update_table":
        combine_price_data()
    elif sys.argv[1] == "all":
        main()
        combine_price_data()

def main():
    # load the producs csv file into a DataFrame
    products_input = pd.read_excel("data/products.xlsx")

    # prompt for markup percentage
    markup = float(input("Markup (%): ")) / 100

    # create empty list to store output rows
    products_output_list = []

    for index, row in products_input.iterrows():
        name = row["name"].upper()
        cost = row["cost"]
        price = price_rounding(cost, round(cost + cost * markup, 2))
        profit = round(price - cost, 2)

        products_output_list.append({
            "DESCRIPTION": name,
            "COST": f"${cost:.2f}",
            "MARKUP": f"{markup * 100:.1f}%",
            "PRICE": f"${price:.2f}",
            "PROFIT": f"${profit:.2f}",
            "ACTUAL MARKUP": f"{profit / cost * 100:.1f}%"
        })

        # create DataFrame from output list
        products_output = pd.DataFrame(products_output_list)

        # sort the DataFrame by product name
        products_output = products_output.sort_values(by="DESCRIPTION")

        # get current date
        current_date = datetime.today().strftime("%Y-%m-%d")

        # save output DataFrame to new xlsx file
        # products_output.to_excel(f"data/backup/product_prices_{current_date}.xlsx", index=False)
        products_output.to_excel(f"data/processed/product_prices_{current_date}.xlsx", index=False)

        # backup original xlsx data
        products_input.to_excel(f"data/backup/product_costs_{current_date}.xlsx", index=False)

    print(f"Price sheet created.")


def combine_price_data():
    # iterate through files in directory
    backup_directory = "data/backup"
    filenames = os.listdir(backup_directory)

    product_prices_list = []

    for filename in filenames:
        # look for product prices sheet
        if filename.startswith("product_price"):
            if filename.endswith(".xlsx"):
                price_data = pd.read_excel(f"data/backup/{filename}")
            else:
                price_data = pd.read_csv(f"data/backup/{filename}")

            for index, row in price_data.iterrows():
                description = row["DESCRIPTION"]
                cost = float(row["COST"].replace("$", ""))
                markup = float(row["MARKUP"].replace("%","")) / 100
                price = float(row["PRICE"].replace("$", ""))
                profit = float(row["PROFIT"].replace("$", ""))
                act_markup = float(row["ACTUAL MARKUP"].replace("%", ""))

                # append to empty product prices list
                product_prices_list.append({
                    "DESCRIPTION": description,
                    "COST": cost,
                    "MARKUP": markup,
                    "PRICE": price,
                    "PROFIT": profit,
                    "ACTUAL MARKUP": act_markup
                })

    product_prices = pd.DataFrame(product_prices_list)
    # sort by product description
    product_prices = product_prices.sort_values(by="DESCRIPTION")
    # specify xlsx file
    target_excel_file = "data/Product_Prices.xlsx"
    # specify sheet name
    sheet_name = 'Products'
    # Write the DataFrame to the specified sheet
    with pd.ExcelWriter(target_excel_file, engine='openpyxl', mode='w') as writer:
        product_prices.to_excel(writer, sheet_name=sheet_name, index=False)

    print(f"Exported {sheet_name} sheet in {target_excel_file}")

    

if __name__ =="__main__":
    startup()
    # main()
    # combine_price_data()