def remove_fourth_character(word: str) -> str:
    beforeS = word[0:3]
    afterS = word[4:]
    Cstring = beforeS+afterS 
    return Cstring


# do not modify below this line
print(remove_fourth_character("NeetCode"))
print(remove_fourth_character("Hello"))
