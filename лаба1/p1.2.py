def find_combinations(candidates, target):
    candidates.sort()
    results = []

    def backtrack(start, path, total):
        if total == target:
            results.append(path)
            return
        if total > target:
            return

        for i in range(start, len(candidates)):
            if i > start and candidates[i] == candidates[i - 1]:
                continue
            backtrack(i + 1, path + [candidates[i]], total + candidates[i])

    backtrack(0, [], 0)
    return results

print(find_combinations([2, 5, 2, 1, 2], 5))

print(find_combinations([10, 1, 2, 7, 6, 1, 5], 8))