#given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

numeros = [1,1,1,3,5,8,4,1,1,5,4,8,4]

def removeDuplicates(nums) -> int:
  if len(nums) == 0:
    return 0

  unique_count = 1  # O primeiro elemento é sempre único
  current = nums[0]

  for i in range(1, len(nums)):
    if nums[i] != current:
        current = nums[i]
        nums[unique_count] = current
        unique_count += 1

  return unique_count

resultado = removeDuplicates(numeros)
print(resultado)