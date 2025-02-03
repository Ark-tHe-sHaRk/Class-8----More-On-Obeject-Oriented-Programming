# Creating a class
class Pair_Of_Elements:
    def twosum(self, nums, target):
        # Creating a dictionary
        lookup = {}
        # Iterating through the list
        for i, num in enumerate(nums):
            # Checking if the number is in the dictionary
            if target - num in lookup:
                # Returning the index of the number
                return(lookup[target - num], i)
            # Adding the number to the dictionary
            lookup[num] = i10

# Take input from the user
value = int(input('Enter the sum for which you want to make this search: '))
result = Pair_Of_Elements().twosum([10, 20, 30, 40, 50, 60, 70, 80, 90], value)

if result:
    print('index1=%d, index2=%d' % result)
else:
    print('No pair found')