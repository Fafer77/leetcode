def lps(pattern):
    m = len(pattern)
    lps_array = [0] * m
    j, i = 0, 1

    while i < m:
        if pattern[i] == pattern[j]:
            j += 1
            lps_array[i] = j
            i += 1
        else:
            if j != 0:
                j = lps_array[j - 1]
            else:
                lps_array[i] = 0
                i += 1
    return lps_array


def kmp_search(text, pattern):
    lps_array = lps(pattern)
    matches = []
    i, j = 0, 0
    n = len(text)
    m = len(pattern)

    while i < n:
        if text[i] == pattern[j]:
            i += 1
            j += 1
            if j == m:
                matches.append(i - j)
                j = lps_array[j - 1]
        else:
            if j > 0:
                j = lps_array[j - 1]
            else:
                i += 1

    return matches


def solution():
    ai_name = input().strip()
    phone_name = input().strip()

    count = kmp_search(ai_name, phone_name)
    phone_len = len(phone_name)
    replacements = 0
    last = -1
    for s in count:
        if s > last:
            replacements += 1
            last = s + phone_len - 1

    print(replacements)


solution()
