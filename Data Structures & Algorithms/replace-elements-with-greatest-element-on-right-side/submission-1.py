class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        

        for i in range(len(arr)):
            greatest = 0
            for j in range(i + 1, len(arr)):
                greatest = max(greatest, arr[j])
            if i != len(arr) - 1:
                arr[i] = greatest
            else:
                arr[i] = -1
    
        return arr
