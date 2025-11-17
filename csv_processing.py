# csv_processing.py

import csv
import pandas as pd


def convert_csv_to_xlsx(file_path):
    file_path = file_path.replace(".csv", "")
    csv_data = pd.read_csv(f"{file_path}.csv")
    # save data to xlsx file
    xlsx_file = f"{file_path}.xlsx"
    csv_data.to_excel(xlsx_file, index=False)


def load_costs_csv(file_path):
    products_input = {}
    with open(file_path, mode='r', newline='') as csvfile:
        csvreader = csv.DictReader(csvfile)
        for row in csvreader:
            name = row['name']
            total_cost = float(row['total cost'])
            qty = int(row['qty'])
            cost = float(row['cost'])

            products_input[name] = {}
            products_input[name]['total_cost'] = total_cost
            products_input[name]['qty'] = qty
            products_input[name]['cost'] = cost
            
    return products_input


def backup_product_costs_to_csv(products, file_path):
    with open(file_path, "w", newline="") as csv_file:
        csvwriter = csv.DictWriter(csv_file, fieldnames=["name", "total cost", "qty", "cost"])

        csvwriter.writeheader()
        for name, details in products.items():
            csvwriter.writerow({'name': name,
                                'total cost': details['total_cost'],
                                'qty': details['qty'],
                                'cost': details['cost']})


def write_products_to_csv(products, file_path):
    with open(file_path, mode='w', newline='') as csvfile:
        csvwriter = csv.DictWriter(csvfile, fieldnames=['DESCRIPTION', 
                                                        'COST', 
                                                        'MARKUP', 
                                                        'PRICE', 
                                                        'PROFIT', 
                                                        'ACTUAL MARKUP'])
        csvwriter.writeheader()
        for name, details in products.items():
            csvwriter.writerow({'DESCRIPTION': name, 
                                'COST': details['cost'], 
                                'MARKUP': details['markup'], 
                                'PRICE': details['price'], 
                                'PROFIT': details['profit'], 
                                'ACTUAL MARKUP': details['act. markup']})
            

def load_prices_csv(file_path):
    products_input = {}
    with open(file_path, mode='r', newline='') as csvfile:
        csvreader = csv.DictReader(csvfile)
        for row in csvreader:
            name = row['DESCRIPTION']
            cost = float((row['COST'].replace("$", "")).strip())
            markup = float(row['MARKUP'].replace("%", ""))
            price = float(row['PRICE'].replace("$", ""))
            act_markup = float(row['ACTUAL MARKUP'].replace("%", ""))

            products_input[name] = {}
            products_input[name]['cost'] = cost
            products_input[name]['markup'] = markup
            products_input[name]['price'] = price
            products_input[name]['act_markup'] = act_markup
            
    return products_input

