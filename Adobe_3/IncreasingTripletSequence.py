def increasingTriplet(nums) -> bool:
    prev = float("inf")
    curr = float("inf")

    for num in nums:
        if num <= prev:
            prev = num
        elif num <= curr:
            curr = num
        else:
            return True

    return False
