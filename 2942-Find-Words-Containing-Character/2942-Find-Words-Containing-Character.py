class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        index_list = []
        for index  in range(len(words)):
            if x in words[index]:
                index_list.append(index)

           
        return index_list 
