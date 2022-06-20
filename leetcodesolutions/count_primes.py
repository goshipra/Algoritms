


class Solution(object):
    def countPrimes(self, n):
        if n < 2:
            return 0
        prime = [True] * n
        prime[0] = prime[1] = False
        for i in range(2,n):
            if prime[i]:
                for j in range(i+i,n,i):
                    prime[j]= False
        return prime.count(True)



obj = Solution()
print(obj.countPrimes(368349))
