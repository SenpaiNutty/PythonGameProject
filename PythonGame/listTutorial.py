#Returns the sum of a list of numbers
def sum(list):
    sum = 0
    for number in list:
        sum = sum + number
    return sum

# Takes in a list of numbers and returns the biggest number
def biggest_number(list):
    biggest_so_far = 0
    for num in list:
        if (num > biggest_so_far):
            biggest_so_far = num
        return biggest_so_far