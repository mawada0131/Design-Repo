def calculate_average(numbers):
    """
    Calculate the average of a list of numbers.
    """
    
    sum_of_numbers = 0
    count_of_numbers = 0
    
    for index in range(len(numbers)):
        current_number = numbers[index]
        if not isinstance(current_number, (int, float)):
            raise TypeError(f"Element at index {index} is not a number")
        sum_of_numbers += current_number
        count_of_numbers += 1
    

    average = sum_of_numbers / count_of_numbers
    return round(average, 2)


# Usage
try:
    result = calculate_average([1, 2, 3, 4, 5])
    print(f"The average is: {result}")
except (TypeError, ValueError) as e:
    print(f"Error: {str(e)}")