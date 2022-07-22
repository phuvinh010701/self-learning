def isValid(self, s):
    """
    :type s: str
    :rtype: bool
    """
    res = []
    for i in range(len(s)):
        if s[i] == '(' or s[i] == '{' or s[i] == '[':
            res.append(s[i])
        else:
            if len(res) > 0:
                if s[i] == ")":
                    if res[-1] == "(":
                        res.pop()
                    else:
                        res.append(s[i])
                elif s[i] == "]":
                    if res[-1] == "[":
                        res.pop()
                    else:
                        res.append(s[i])
                elif s[i] == "}":
                    if res[-1] == "{":
                        res.pop()
                    else:
                        res.append(s[i])
            else:
                res.append(s[i])
    
    if len(res) == 0:
        return True
    else:
        return False   
