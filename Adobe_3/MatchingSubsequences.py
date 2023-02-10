from collections import defaultdict

# O(n + m)


def numMatchingSubseq(s: str, words) -> int:
    # create a dictionary with starting char as key
    wordMap = defaultdict(list)
    for w in words:
        key = w[0]
        wordMap[key].append(w)

    # now iterate through the string
    # if a char matches then pull the list of words for that char
    # if len of any word == 1, then increase count + 1
    # else, push the rest of the words from that list in the dict with key as word[1]
    res = 0
    for ch in s:
        if ch in wordMap:
            words_starting_with_ch = wordMap[ch]
            wordMap[ch] = []

            for w in words_starting_with_ch:
                if len(w) == 1:
                    # sequence completed
                    res += 1
                else:
                    wordMap[w[1]].append(w[1:])
    return res


s = "dsahjpjauf"
w = ["ahjpjau", "ja", "ahbwzgqnuk", "tnmlanowax"]
print(numMatchingSubseq(s, w))
