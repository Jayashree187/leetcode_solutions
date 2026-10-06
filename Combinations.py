class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        res = []
        
        def backtrack(start, path):
            # If the combination is done
            if len(path) == k:
                res.append(list(path))
                return
            
            # Iterate through the remaining integers
            for i in range(start, n + 1):
                # Optimization: Prune the search tree if there aren't enough elements left
                if len(path) + (n - i + 1) < k:
                    break
                    
                path.append(i)
                backtrack(i + 1, path)
                path.pop()  # Backtrack
                
        backtrack(1, [])
        return res
