def q1(target, nums, count):

    #let us iterate through the list
    for i in range(0 ,len(nums)):
        # making sure that i<j helps us avoid counting duplicate pairs
        for j in range(i+1, len(nums)):
            if (nums[i]+nums[j]==target): 
                count = count + 1

    #return the count ie number of pairs           
    return count
            

if __name__ == "__main__":
    print(q1(10,[2,7,4,1,3,6],0))