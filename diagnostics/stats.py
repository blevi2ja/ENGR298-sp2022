from util import generate_random_int_list

# Diagnostic #2: complete the methods calculate_mean and calculate_std_dev

class StatsPackage:

    def __init__(self):
        # Do nothing! :)
        return

    # complete the method implementation to calculate the mean of an unknown list
    def calculate_mean(self, nums):

        global average
        average = 0
        total = 0
        numint = len(nums)
        for val in nums:
            total = total+val
            average = total/numint


        return average

    # complete the method implementation to calculate the standard deviation
    # https://mathworld.wolfram.com/StandardDeviation.html
    def calculate_std_dev(self, nums):

        mean = self.calculate_mean(nums)
        i = 0
        sum = 0
        standarddev = 0
        while i < len(nums):
            sum += (nums[i] - mean)*(nums[i] - mean)
            i += 1
        standarddev = (sum/len(nums))** (1/2)
        return standarddev


if __name__ == "__main__":
    print('Welcome to the stats program!!')

    print('Now generating a random length list of random integers....')
    rands = generate_random_int_list(100, 10000)

    stats_package = StatsPackage()

    print('List mean is ' + str(stats_package.calculate_mean(rands)))
    print('List standard deviation is ' + str(stats_package.calculate_std_dev(rands)))

    print('All done!')

