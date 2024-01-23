def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s): 
    if not s[0].isalpha() or not s[1].isalpha():
        return False
    if not (len(s) >= 2 and len(s) <= 6):
        return False
    if not s.isalnum():
        return False
    for i in range(2,len(s)):
        if s[i].isdigit():
            if s[i] == "0":
                return False
            else :
                for j in range(i+1,len(s)):
                    if s[j].isalpha():
                        return False
    return True                 
    



main()