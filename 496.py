class Solution:
    def nextGreaterElement(self, nums1: 'List[int]', nums2: 'List[int]') -> 'List[int]':
        GreatNumDict = {}
        for i in range(len(nums2)):
            GreatNumDict[nums2[i]] = -1
            for j in range(i,len(nums2)):
                if nums2[j] > nums2[i]:
                    GreatNumDict[nums2[i]] = nums2[j]
                    break
        Result = []
        for ele in nums1:
            Result.append(GreatNumDict[ele])
        return Result