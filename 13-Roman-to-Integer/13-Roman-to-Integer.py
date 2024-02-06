class Solution:
    def romanToInt(self, s: str) -> int:
        exp_dict = {'I'  : 1,
                    'V'  : 5,
                    'X'  : 10,
                    'L'  : 50,
                    'C'  : 100,
                    'D'  : 500,
                    'M'  : 1000}
        total_sum = 0            
        for i in range(len(s)-1):
            if(exp_dict[s[i]] < exp_dict[s[i+1]]):
                total_sum -= exp_dict[s[i]]
            else:
                total_sum += exp_dict[s[i]]
        return total_sum+exp_dict[s[-1]]
