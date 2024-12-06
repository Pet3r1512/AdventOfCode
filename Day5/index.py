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
invalid_orders = []

print(total_sum)

for order in orders:
    if is_valid_order(order, dictionary):
        middle_index = len(order) // 2
        middle_element = order[middle_index]
        total_sum += middle_element  
    else:
        invalid_orders.append(order)

def fix_invalid_order(invalid_order):
    for i in range(0, len(invalid_order)):
        new_dict = {}
        sliced_order = invalid_order[i:]
        
        for key, values in dictionary.items():
            if key in sliced_order:
                valid_values = [value for value in values if value in sliced_order]
                if valid_values: 
                    new_dict[key] = valid_values
        
        values_set = set()
        for values in new_dict.values():
            values_set.update(values)
        missing_element = int((set(sliced_order) - values_set).pop())
        missing_element_index = invalid_order.index(missing_element)
        invalid_order[i], invalid_order[missing_element_index] = invalid_order[missing_element_index], invalid_order[i]



    return invalid_order

invalid_sum = 0
for line in invalid_orders:
    valid = fix_invalid_order(line)
    middle_index = len(valid) // 2
    middle_element = valid[middle_index]
    invalid_sum += middle_element  

print(invalid_sum)