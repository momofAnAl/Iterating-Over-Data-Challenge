def calculate_total_sales(sales_totals):
    total = 0.0
    for details in sales_totals.values():
        total += details['quantity'] * details['price']
    return total

def calculate_average_sales(sales_totals):
    if not sales_totals:
        return 0.0
    
    total_sales = calculate_total_sales(sales_totals)
    num_items = len(sales_totals)
    
    return total_sales / num_items

def filter_to_better_than_average_sales(sales_totals):
    if not sales_totals:
        return {} 

    average_sales = calculate_average_sales(sales_totals)
    
    better_sales = {}
    for item, details in sales_totals.items():
        item_total_sales = details['quantity'] * details['price']
        
        if item_total_sales > average_sales:
            
           better_sales[item] = details
    return better_sales
    
def ninety_nine_bottles(count, beverage):
    lines = []
    
    for i in range(count, 0, -1):
        if i == 1:
            lines.append(f"{i} bottle of {beverage} on the wall, {i} bottle of {beverage}")
            lines.append(f"If one of those bottles should happen to fall, {i - 1} bottles of {beverage} on the wall")
        elif i == 2: 
            lines.append(f"{i} bottles of {beverage} on the wall, {i} bottles of {beverage}")
            lines.append(f"If one of those bottles should happen to fall, {i - 1} bottle of {beverage} on the wall")
        else:
            lines.append(f"{i} bottles of {beverage} on the wall, {i} bottles of {beverage}")
            lines.append(f"If one of those bottles should happen to fall, {i - 1} bottles of {beverage} on the wall")

    return lines
