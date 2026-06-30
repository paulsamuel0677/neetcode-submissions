def concatenate(s1: str, s2: str) -> str:
    com = s1+s2
    if len(com)>10:
        return "Too long!"
    else:
        return com






# do not modify below this line
print(concatenate("He", "llo"))
print(concatenate("Hello ", "world!"))
print(concatenate("Length", "of10"))
