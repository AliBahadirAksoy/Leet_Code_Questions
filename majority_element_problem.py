# I am trying to find the element which is the most repeated in the array


# nums= [2,2,1,3,1,2,5,33,3,3,3,3,6,6,6,6,6,6,6,6,6,6]

# def find_m():
#     max_count=0
#     b=-1
#     for i in range(0,len(nums)):
#         count=nums.count(nums[i])
#         if max_count < count:
#             max_count=count
#             b=i
#         elif max_count==count:
#             max_count=count
#         else:
#             max_count=max_count
            
            
#     print(b,nums[b],max_count) 
# find_m()  

#this shows how the code works
        





nums= [2,2,1,3,1,2,5,33,3,3,3,3,6,6,6,6,6,6,6,6,6,6]

def find_m():
    max_count=0
    b=-1
    for i in range(0,len(nums)):
        count=nums.count(nums[i])
        if max_count < count:
            max_count=count
            b=i
        elif max_count==count:
            max_count=count
        else:
            max_count=max_count
            
            
    print(f" majority element is : {nums[b]}") 
find_m()


# myList=[1,1,1,1,2,3,2,2,2,2,2,2,4,4,4,4,4,4,4,4,4,4,4,4]

# def boyerMoore():
#     result=0
#     count=0
    
#     for num in myList:
#         if count==0:
#             result=num
#         if num==result:
#             count+=1
#         else:
#             count-=1
#     return result 
# boyerMoore()

# boyermoore's solution




