def search_last_index(haystack: str, needle: str):
    n = len(haystack)
    m = len(needle)
    last_index = None
    number_of_comparisons = 0

    if m == 0:
        return n - 1, 0

    for i in range(n - m + 1):
        j = 0
        while j < m:
            number_of_comparisons += 1
            if haystack[i + j] != needle[j]:
                break
            j += 1
        if j == m:
            last_index = i + m - 1

    return last_index, number_of_comparisons

haystack = 'HelloWorld'
needle = 'ello'
last_index, number_of_comparisons = search_last_index(haystack, needle)

print(f"Needle '{needle}' end at index: {last_index}")
print(f"Number of comparisons: {number_of_comparisons}")

haystack = "abcdabcd"
needle = "b"
last_index, number_of_comparisons = search_last_index(haystack, needle)

print(f"Needle '{needle}' end at index: {last_index}")
print(f"Number of comparisons: {number_of_comparisons}")