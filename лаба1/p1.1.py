def count_jewels(jewels, stones):
    return sum(1 for ch in stones if ch in jewels)

j = "ab"
s = "aabbcccd"
print(count_jewels(j, s))