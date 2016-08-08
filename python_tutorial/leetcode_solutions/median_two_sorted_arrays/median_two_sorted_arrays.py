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
        l = m + n
        if l==0:
            raise Exception("Invalid input: Empty arrays")
        k = -1
        if l%2 == 0:
            n1 = self.findKthSmallest(nums1, nums2, l/2)
            n2 = self.findKthSmallest(nums1, nums2, l/2+1)
            return (n1 + n2)/2.0
        else:
            return self.findKthSmallest(nums1, nums2, l/2+1)    


    def findKthSmallest(self, nums1, nums2, k):
        m = len(nums1)
        n = len(nums2)
        l = m + n
        if k<1 or k>l:
            raise Exception("Invalid value for k. k has to be "  
                            "between 1 and sum of lengths of arrays")
        if m==0:
            return nums2[k-1]
        elif n==0:
            return nums1[k-1]
        elif m>n:
            # Exchange nums1 and nums2 since m>n
            return self.findKthSmallest(nums2, nums1, k)
        elif k==1:
            return min(nums1[0], nums2[0])
        else:
            i = k/2 -1
            j = -1
            if k%2 == 0:
                j = k/2 -1
            else:
                j = k/2
            if i>m-1 or i<0:
                i = m/2
                j = k-i-2
            if nums1[i] <= nums2[j]:
                return self.findKthSmallest(nums1[i+1:m], nums2[0:j+1], k-i-1)
            else:
                return self.findKthSmallest(nums1[0:i+1], nums2[j+1:n], k-j-1)
                      

if __name__ == '__main__':

    s = Solution()
    nums1 = [1, 1, 10, 11]
    nums2 = [1, 2, 4, 5]
    print s.findMedianSortedArrays(nums1, nums2)
