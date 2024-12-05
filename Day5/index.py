orders = []
with open("Day5/order.txt", "r") as file:
    for line in file:
        # Split the line by commas and convert each value to an integer
        array = list(map(int, line.strip().split(',')))
        # Append the array to the orders list
        orders.append(array)

dictionary = {}
with open("Day5/rule.txt", "r") as file:
    for line in file:
        key, value = map(int, line.strip().split('|'))
        if key not in dictionary:
            dictionary[key] = []
        dictionary[key].append(value)

def is_valid_order(order, rule_dict):
    for key, values in rule_dict.items():
        for value in values:
            if key in order and value in order:
                if order.index(key) > order.index(value): 
                    return False
    return True

total_sum = 0

for order in orders:
    if is_valid_order(order, dictionary):
        print(f"Valid order: {order}")
        middle_index = len(order) // 2
        middle_element = order[middle_index]
        print(f"Middle element: {middle_element}")
        total_sum += middle_element  

print(f"Total sum: {total_sum}")
