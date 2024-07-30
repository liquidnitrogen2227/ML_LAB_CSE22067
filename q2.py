def q2(nums, max_val, min_val):
    max_num = max_val
    min_num = min_val
    
    for i in range(len(nums)):
        if max_num < nums[i]:
            max_num = nums[i]

    min_num = nums[0]  
    for j in range(len(nums)):
        if min_num > nums[j]:
            min_num = nums[j]
    
    range1 = max_num - min_num
    return min_num, max_num, range1

if __name__ == "__main__":
    print(q2([1,2,3,4,5], 0, 0))
