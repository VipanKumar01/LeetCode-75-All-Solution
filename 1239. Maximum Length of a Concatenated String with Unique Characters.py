# Comments are(My Code) - Some Fault occur in my Code Please Check

class Solution:
    def maxLength(self, arr: List[str]) -> int:
#         setStr = ""
#         MaxLen = 0
        
#         if len(arr) == 1:
#             return len(set(arr[0]))
        
#         for i in range(len(arr)-1):
#             setStr = len(set(arr[i]+arr[i+1]))
#             if MaxLen < setStr:
#                 MaxLen = setStr
            
#         return MaxLen


And this is the Right Code ->

        n = len(arr)
        res = [""]
        op = 0
        
        for word in arr:
            for r in res:
                newRes = r+word
                if len(newRes)!=len(set(newRes)): continue
                res.append(newRes)
                op = max(op, len(newRes))
        return op
