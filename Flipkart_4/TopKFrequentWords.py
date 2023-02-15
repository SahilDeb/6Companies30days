from collections import Counter, defaultdict
from heapq import heapify, heappop


def topKFrequent(words, k: int):
    wordFreq = Counter(words)

    groups = defaultdict(list)
    for key, v in wordFreq.items():
        groups[v].append(key)

    heap = []
    for key, v in groups.items():
        heap.append((-key, sorted(v)))
    heapify(heap)

    res = []
    while k > 0:
        _, words = heappop(heap)
        if len(words) > k:
            res += words[:k]
        else:
            res += words
        k -= min(k, len(words))

    return res


a = ["aaa", "aa", "a"]
k = 2
print(topKFrequent(a, k))
