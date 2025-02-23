from typing import List

class Solution:
    def quicksort(self, array: list, low: int, high: int) -> None:
        if low < high:
            pivot = self.partition(array, low, high)
            self.quicksort(array, low, pivot)
            self.quicksort(array, pivot + 1, high)

    def partition(self, array: List[int], low: int, high: int) -> int:
        pivot = array[(low + high) // 2]
        i = low - 1
        j = high + 1

        while True:
            i += 1
            while array[i] < pivot:
                i += 1
            j -= 1
            while array[j] > pivot:
                j -= 1
            if i >= j:
                return j

            array[i], array[j] = array[j], array[i]

    def sortArray(self, nums: List[int]) -> List[int]:
        self.quicksort(nums, 0, len(nums) - 1)
        return nums
    
solution = Solution()
print(solution.sortArray([5,1,1,2,0,0]))
