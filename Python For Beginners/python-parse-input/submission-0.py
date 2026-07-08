from typing import List

def read_integers() -> List[int]:
    line = input()
    s_list = line.split(",")
    inte_list=[]
    for string in s_list:
        inte_list.append(int(string))
    return inte_list

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
