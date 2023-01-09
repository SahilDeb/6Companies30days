# Idea:

# Using two map:
# 1. One for how many sequences have that ending word
# 2. Another for how many numbers are unchecked

# Loop through every number
# If there is sequence with the number - 1, we add the number to the seq
# If not, Create a new seq using the number
# If there aren't two numbers behind to let us create new seq, return False

from collections import Counter

# O(n)


def isPossible(nums) -> bool:
    # key: ending number, val: how many seqs
    seq = Counter()
    # key: number, val: how many of key are left unchecked
    left = Counter(nums)

    for num in nums:
        # the number is already in seqs, we don't need to check again
        if not left[num]:
            continue

        left[num] -= 1

        # If there is sequence before the number, we add the number to the seq
        # Greedily keep the len of seq to 3 initially, later check if we can add upto existing sequences
        if seq[num-1] > 0:
            seq[num-1] -= 1
            seq[num] += 1
        # If not, create a new seq using the number
        else:
            #  If there aren't two numbers behind to let us create new seq, return False
            if (not left[num+1] or not left[num+2]):
                return False

            left[num+1] -= 1
            left[num+2] -= 1
            seq[num+2] += 1
    return True


n1 = [1, 2, 3, 3, 4, 5]
n2 = [1, 2, 3, 3, 4, 4, 5, 5]
n3 = [1, 2, 3, 4, 5, 5]
print(isPossible(n3))
