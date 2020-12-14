preamble_len = 25


def num_valid(idx, numbers):
    for j in range(idx - 25, idx):
        for k in range(idx - 25, idx):
            if numbers[j] + numbers[k] == numbers[idx] and not numbers[j] == numbers[k]:
                return True
    return False


def find_contiguous_set(inv_num, numbers):
    for idx in range(len(numbers)):
        j = idx + 1
        contiguous_sum = numbers[idx]
        while contiguous_sum < inv_num:
            contiguous_sum += numbers[j]
            j += 1
        if contiguous_sum == inv_num:
            return idx, j


with open('input.txt', 'r') as file:
    nums = [int(n) for n in file.read().split('\n')]
    for i in range(preamble_len, len(nums)):
        if not num_valid(i, nums):
            lower_bound, upper_bound = find_contiguous_set(nums[i], nums)
            print(min(nums[lower_bound:upper_bound]) + max(nums[lower_bound:upper_bound]))
