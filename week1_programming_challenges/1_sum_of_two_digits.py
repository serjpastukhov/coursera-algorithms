def ab_sum(numbers_list):
    sum_number = sum(numbers_list)

    return sum_number


if __name__ == '__main__':
    input_string = input().split()
    numbers = [int(el) for el in input_string]

    s = ab_sum(numbers)

    print(s)
