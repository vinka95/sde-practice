class Solution:
    def findCatalan(self, n : int) -> int:
        # code here
        # Base Case
        if n <= 1:
            return 1
 
        # Catalan(n) is the sum of catalan(i)*catalan(n-i-1)
        res = 0
        for i in range(n):
            res += self.findCatalan(i) * self.findCatalan(n-i-1)
 
        return res

#{ 
 # Driver Code Starts
if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n = int(input())
        
        obj = Solution()
        res = obj.findCatalan(n)
        
        print(res)
        

# } Driver Code Ends
