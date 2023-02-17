# Time complexity:
# O(2 ^ N) for trying all possible guesses
# O(N ^ 2) for validating each guess
# Total: O((N ^ 2) * (2 ^ N))
def maximumGood(statements) -> int:
    n = len(statements)
    ans = [0]

    # check if assumed config is matching the statement
    def isValid(config):
        for i in range(n):
            if config[i]:
                for j in range(n):
                    if statements[i][j] != 2 and statements[i][j] != config[j]:
                        return False
        return True

    config = [0] * n
    # try all combinations of config

    def backtrack(i, curr_good):
        # base case
        if i == n:
            if isValid(config):
                ans[0] = max(ans[0], curr_good)
            return

        backtrack(i+1, curr_good)
        config[i] = 1
        backtrack(i+1, curr_good+1)
        config[i] = 0

    backtrack(0, 0)
    return ans[0]


s = [[2, 1, 2], [1, 2, 2], [2, 0, 2]]
print(maximumGood(s))
