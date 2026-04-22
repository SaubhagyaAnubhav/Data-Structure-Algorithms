class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        last = 0
        operations = 0
        for i in range(len(target)):
            if target[i] > last:
                operations+=target[i]-last
                last = target[i]
            else:
                target[i] < last
                last = target[i]
        return operations
        