from collections import defaultdict

# 242. Valid Anagram
# Given two strings s and t, write a function to determine if t is an anagram of s.

# Time complexity: O(n)
def isAnagram(s1, s2):
    if len(s1) != len(s2):
        return False

    d = defaultdict(int)
    for i in range(len(s1)):
        d[s1[i]] += 1
        d[s2[i]] -= 1

    return all(v==0 for v in d.values())

if __name__ == '__main__':
    s1, s2 = "anagram", "nagaram"
    print(f"s1: {s1}, s2: {s2}, {isAnagram(s1, s2)}")
    s1, s2 = "rat", "car"
    print(f"s1: {s1}, s2: {s2}, {isAnagram(s1, s2)}")
