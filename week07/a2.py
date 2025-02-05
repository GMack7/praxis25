def filter_evens(numbers):
   evens = []
   for number in numbers:
      if number % 2 == 0: 
         evens.append(number)
   return evens

nums = [0,-2,3,14]
print(filter_evens(nums))