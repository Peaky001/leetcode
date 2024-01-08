class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        len_list =[]
        for string in sentences:
            len_list.append(len(string.split()))
        
        return (max(len_list))
   