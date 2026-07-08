def add_two_numbers() -> int:
    nums = input()
    s_list = nums.split(",")
    inte_list = []
    for string in s_list:
        inte_list.append(int(string))
    return sum(inte_list)




# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
