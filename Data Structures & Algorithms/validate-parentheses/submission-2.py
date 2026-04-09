class Solution:
    def isValid(self, s: str) -> bool:
        from collections import deque
        d = deque()

        openingB = {
            '}' : '{',
            ']' : '[',
            ')' : '('
        }

        for b in s:
            if b in ['{','[','('] or len(d) == 0:
                d.append(b)
            elif b in ['}',']',')'] and openingB[b] == d[-1]:
                print(b,openingB[b],d)
                d.pop()
            else:
                d.append(b)

        return len(d) == 0

        