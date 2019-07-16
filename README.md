# CTCI

### Backtrack Summary: 
Combination Sum, Subsets, Permutation,  Palindrome)


39. Combination Sum

[https://leetcode.com/problems/combination-sum/](https://leetcode.com/problems/combination-sum/)

```python
def combinationSum(self, candidates, target):
        def backtrack(tmp, start, end, target):
            if target == 0:
                ans.append(tmp[:])
            elif target > 0:
                for i in range(start, end):
                    tmp.append(candidates[i])
                    backtrack(tmp, i, end, target - candidates[i])
                    tmp.pop()
        ans = [] 
        candidates.sort(reverse= True)
        backtrack([], 0, len(candidates), target)
        return ans
```

---

40. Combination Sum II

[https://leetcode.com/problems/combination-sum-ii/](https://leetcode.com/problems/combination-sum-ii/)

```python
def combinationSum2(self, candidates, target):
        def backtrack(start, end, tmp, target):
            if target == 0:
                ans.append(tmp[:])
            elif target > 0:
                for i in range(start, end):
                    if i > start and candidates[i] == candidates[i-1]:
                        continue
                    tmp.append(candidates[i])
                    backtrack(i+1, end, tmp, target - candidates[i])
                    tmp.pop()
        ans = []
        candidates.sort(reverse= True)
        backtrack(0, len(candidates), [], target)
        return ans
```
