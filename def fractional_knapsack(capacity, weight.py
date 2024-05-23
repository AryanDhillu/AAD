def value_per_weight (item):
    return item[1]/item [0]

def fractional_Knapsack (items, capacity):
    items.sort(key=value_per_weight, reverse=True)
    max_value = 0
    for weight, value in items:
        if capacity == 0:
            break
        if weight <= capacity:
            max_value += value
            capacity -= weight
        else:
            max_value += (value/weight)*capacity
            break
    return max_value

num_items = int(input("Enter the number of items: "))
items = []

for i in range(num_items):
    weight = int(input(f"Enter the weight for item {i+1}: "))
    profit = int(input(f"Enter the value for the item {i+1}: "))
    items.append((weight, profit))
    
capacity = int(input("Enter the capacity of the Knapsack: "))
print("Maximum profit: ", fractional_Knapsack(items, capacity))
                                        