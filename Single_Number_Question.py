


#find single number

# nums=[1,1,2,1,2,5,5,3]

# def findS():
#     if len(nums)==1:
#         return nums[0]
#     else:
#         for i in range(0,len(nums)):
#             for j in range(i+1,len(nums)):
#                 if nums[i] == nums[j]:
#                     print(f"{i} indexli {nums[i]} is not single") 
#         else:
#             print(f"{i} indexli {nums[i]} is single")
                
            
# findS()





def singleNumber():
    myList=[1,2,1,2,7]
    result=0
    for num in myList:
        result=num ^ result  #bit manipulation xhor (^)
    return result





singleNumber()





# time O(N), space O(1)

