
def expand(s, l, r):
    left = l
    right = r
    m = len(s)
    while True:
        if left == 0 or right == m-1:
            return s[left:right+1]
        left -= 1
        right += 1
    return None


def is_palindrome(s):
    l=0
    r=len(s) -1
    while l<r:
        if s[l] != s[r]:
            return False
        l += 1
        r -= 1
    return True


def find_longest_palindromic_substring(s):
    print is_palindrome(expand(s, 1, 2))



if __name__ == '__main__':
    print expand('abccba', 1, 2)
    print expand('aabaac', 3, 3)
    print expand('aabaac', 3, 4)
    print expand('aabaac', 4, 4)
    find_longest_palindromic_substring('abccba')