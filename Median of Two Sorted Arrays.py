class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums1.extend(nums2)
        nums1.sort()
        if len(nums1)%2 == 0:
            #print(nums1[len(nums1)//2-1])
            #print(nums1[len(nums1)//2])
            #print(len(nums1)//2)
            return round(float((nums1[len(nums1)//2-1] + nums1[len(nums1)//2])/2), 1)
        else:
            return round(float(nums1[len(nums1)//2]), 1)


if __name__ == "__main__":
    m = Solution()
    nums1 = [1,2,3,4,5]
    nums2 = [6,7,8,9,10]
    print(m.findMedianSortedArrays(nums1, nums2))
