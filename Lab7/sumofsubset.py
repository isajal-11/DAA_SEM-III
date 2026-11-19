#Sum of Subset problem
def subset_sum(nums, target, index, current, total, result):
    if total == target:
        result.append(current[:])
        return
    if index == len(nums) or total > target:
        return

    current.append(nums[index])
    subset_sum(nums, target, index + 1, current, total + nums[index], result)
    current.pop()

    subset_sum(nums, target, index + 1, current, total, result)

nums = [10, 7, 5, 18, 12, 20, 15]
target = 35
result = []

subset_sum(nums, target, 0, [], 0, result)

if result:
    for s in result:
        print(s)
else:
    print("No subset found")