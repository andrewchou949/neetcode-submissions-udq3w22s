class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        for i in range(len(matrix)):
            # the first matrix item range is the result should be at
            if matrix[i][0] <= target <= matrix[i][-1]:
                l, r = 0, len(matrix[i]) - 1
                while l <= r:
                    mid = l + (r - l) // 2
                    curr = matrix[i][mid]
                    if curr == target:
                        return True
                    if target < curr:
                        r = mid - 1
                    else:
                        l = mid + 1
        return False