def get_average():
    with open("../files/temperatures.txt", 'r') as file:
        data = file.readlines()
    values = data[1:]
    print(values)
    values = [float(i) for i in values]
    local_average = sum(values) / len(values)
    return local_average


average = get_average()
print(average)