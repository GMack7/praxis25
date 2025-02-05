def sum(number_list):
    x = 0
    sum = 0
    while x<len(number_list):
        sum = sum + number_list[x]
        x = x+1
    return sum

nums = [0,1,2,3,4,5,6000]
print(sum(nums))