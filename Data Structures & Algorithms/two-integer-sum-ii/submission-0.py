class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        numbers.reverse()
        ix=1
        l = len(numbers)
        while True:
            k = numbers.pop()
            print(k)
            if target-k in numbers:
                return [ix, l-numbers.index(target-k)]
            ix+=1