# Given a long number, return all the possible sum of two digits of it.

# For example, 12345: all possible sum of two digits from that number are:

# [ 1 + 2, 1 + 3, 1 + 4, 1 + 5, 2 + 3, 2 + 4, 2 + 5, 3 + 4, 3 + 5, 4 + 5 ]
# Therefore the result must be:

# [ 3, 4, 5, 6, 5, 6, 7, 7, 8, 9 ]

def digits(num):
    digit_array = []; result = []; string_numbers = str(num);

    for i in range(0, len(string_numbers) - 1):
      for j in range(i + 1, len(string_numbers)):
        digit_array.append(string_numbers[i] + string_numbers[j])
        
    for numbers in digit_array:
      result.append(int(numbers[0]) + int(numbers[1]))
    
    return result