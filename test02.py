#coding=utf-8

def rotate(nums, k):    
    length = len(nums)    
    print length
    if length != 0:        
#        nums[:] = nums[length - k:length] + nums[0:length-k] 
#         nums[:] = nums[length - k:length]

         nums[:] = nums[1:length] + nums[0:1]

mylist = [1,2,3,4,5,6,7]
rotate(mylist, 2)
print(mylist)