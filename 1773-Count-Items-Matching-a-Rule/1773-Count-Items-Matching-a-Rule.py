class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        items_dict = {"type":0,
                    "color":1,
                    "name":2}

        count =0
        for item in items:
            key_result = items_dict[ruleKey]
            if item[key_result] == ruleValue:
                count+=1
        return count