def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    if not s:
        return 0
    big_l = 0
    prev_s = ''
    for c in s:
        index = prev_s.find(c)
        if index != -1:
            # Character was found in string,
            # please strip off the string
            prev_s = prev_s[index+1:len(prev_s)]
        prev_s += c
        big_l = max(big_l, len(prev_s))
    return big_l


if __name__ == '__main__':
    n = lengthOfLongestSubstring('dvdf')
    print n
    
