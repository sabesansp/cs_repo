# There are two sorted arrays nums1 and nums2 of size m and n respectively. Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

class Solution(object):

    def __init__(self):
        pass

    def median(self, n):
        l = len(n)
        if l%2==0:
            return float( ( n[l/2-1] + n[l/2] ) / 2.0)
        else:
            return n[l/2]

    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m = len(nums1)
        n = len(nums2)
        if m==0 and n==0:
            return None
        if m>n:
            return self.findMedianSortedArrays(nums2, nums1)
        if m==1 and n==1:
            return float( (nums1[0] + nums2[0])/ 2.0 )
        if m==2 and n==2:
            return float( max(nums1[0], nums2[0]) + min(nums1[1], nums2[1]) ) / 2.0
        if m==1 and n>2:
            m2 = self.median(nums2)
            return self.findMedianSortedArrays(nums1, nums2[:n/2+1])
        if m>2 and n>2:
            m1 = self.median(nums1)
            m2 = self.median(nums2)
            if m1 == m2:
                return m1
            elif m1>m2:
                nums1, nums2 = nums2, nums1
            return self.findMedianSortedArrays(nums1[m/2 -1: ], nums2[:n/2+1])
        return None

if __name__ == '__main__':

    s = Solution()
    nums1 = [1,2,3,4]
    nums2 = [5,6,7,8]
    print s.findMedianSortedArrays(nums1, nums2)
