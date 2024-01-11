class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        count = 26
        new_sentence = set(sentence)
        if len(new_sentence)==count:
            return True
        else:
            return False
       
