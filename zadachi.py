numbers = [1, 3, 2, 5, 7, 6, 8, 4, 9]
goal = 10


def finder_goal(numbers: list, goal: int) -> None:
    current_index = 0
    next_index = 1
    while current_index+next_index <= len(numbers)-1:
        summ_of_element = numbers[current_index] + numbers[current_index+next_index]
        if summ_of_element == goal:
            return print([numbers[current_index], numbers[current_index+next_index]])
        next_index += 1
    else:
        current_index += 1


finder_goal(numbers, goal)


# def finder_goal(numbers: list, goal: int):
#     for i in range(len(numbers)-1):
#         if result_for_n_element(i) == goal:
#             return print([''])


# def finder_goal(numbers: list, goal: int):
#     summ_of_element = 0
#     for i in range(len(numbers)-1):
#         summ_of_element = numbers[i] + numbers[i+1]
#         print(summ_of_element)
#
#     return print(summ_of_element)



# def finder(numbers: list, goal: int):
#     result = (first, second)
#     for num in numbers:
#         if num + numbers[num+1] == goal:
#             return first
#
#     return print(result)
#
#
