class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        lst = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            low, high = i+1, len(nums)-1

            while low < high:
                summ = nums[i] + nums[low] + nums[high]
                if summ == 0:
                    lst1 = ([nums[i], nums[low], nums[high]])
                    lst.append(lst1)
                    low += 1
                    high -= 1
                    while low < high and nums[low] == nums[low-1]:
                        low += 1
                    while low < high and nums[high] == nums[high+1]:
                        high -= 1
                elif summ > 0:
                    high -= 1
                else:
                    low += 1

        return lst
