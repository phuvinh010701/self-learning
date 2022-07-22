def isPalindrome(self, s: str) -> bool:
    def is_true(string):
        leng = len(string)
        for i in range(leng // 2):
            if string[i] != string[leng - 1- i]:
                return False
        return True
    temp = ""
    for i in s:
        if i.isalpha() or i.isdigit():
            temp += i
    temp = temp.lower()
    print(temp)
    return is_true(temp)