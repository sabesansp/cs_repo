# There are two sorted arrays nums1 and nums2 of size m and n respectively. Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

class Solution(object):

    def __init__(self):
        pass

    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        val = 0.1 if 1<2 else 1.1
        return val

if __name__ == '__main__':

    s = Solution()
    nums1 = [1,2,3,4]
    nums2 = [5,6,7,8]
    print s.findMedianSortedArrays(nums1, nums2)
