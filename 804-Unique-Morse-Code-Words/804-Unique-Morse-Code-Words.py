class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        list1  = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        list2 = "abcdefghijklmnopqrstuvwxyz"
        mapping = dict(zip(list2,list1))
        for i in range(len(words)):
            morse_code = ""
            for j in words[i]:
                morse_code +=mapping[j]
            words[i]=morse_code
        return len(set(words))