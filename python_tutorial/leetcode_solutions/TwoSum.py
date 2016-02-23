#Given an array of integers, return indices of the two numbers such that they add up to a specific target.
#You may assume that each input would have exactly one solution.
#
#Example:
#Given nums = [2, 7, 11, 15], target = 9,
#
#Because nums[0] + nums[1] = 2 + 7 = 9,
#return [0, 1].



# This solution was accepted on leetcode

class TwoSum(object):


   def twoSum(self, nums, target):
      """
      
      :type nums: list[int]
      :type target: int
      :rtype: list[int]
      """

      o = []
      if nums is None or len(nums)==0:
         raise Exception("nums is none/empty")
      else:
         # Initialize an empty dictionary 
         d = {}

         # for each value in the 'nums' array, 
         # populate the dictionary based on this value
         for i in range(len(nums)):
            if nums[i] in d:
               o.append(d[nums[i]])
               o.append(i)
               break
            else:
               d[target-nums[i]] = i
      return o   
               
         



if __name__ == '__main__':
   t = TwoSum()
   o = t.twoSum([2,9,11],9)
   print o
           
