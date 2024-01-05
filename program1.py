class Solution(object):
    def isValid(self, s):
        d={'{':'}','(':')','[':']'}
        stack=[]
        for i in s:
            if i in d.keys():
                stack.append(i)
            elif i in d.values():
                if stack==[]:
                    return False
                elif d[stack[-1]]==i:
                    stack.pop()
                else:
                    return False
        if stack==[]:
            return True
        else:
            return False
    



  

