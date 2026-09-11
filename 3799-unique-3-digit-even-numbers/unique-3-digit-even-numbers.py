class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        freq=[0]*10
        for digit in digits:
            freq[digit]+=1
        ans=0
        for first in range(1,10):
            for second in range(10):
                for third in range(0,10,2):
                    if first==second==third:
                        if freq[third]>=3:
                            ans+=1
                    elif first == second:
                        if freq[first] >=2 and freq[third]>=1:
                            ans+=1
                    elif first==third:
                        if freq[first]>=2 and freq[second]>=1:
                            ans+=1
                    elif second==third:
                        if freq[second] >=2 and freq[first]>=1:
                            ans+=1
                    else:
                        if freq[first] and freq[second] and freq [third]:
                            ans+=1
        return ans