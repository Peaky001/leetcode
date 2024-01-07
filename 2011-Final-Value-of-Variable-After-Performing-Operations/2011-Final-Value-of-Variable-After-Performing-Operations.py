class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        x =0
        dic = {"X++":1,"++X":1,"--X":-1,"X--":-1}
        for i in operations:
           x+= dic[i]
        return x