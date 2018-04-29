
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


def lengthOfLongestSubstring(s):
    if s == None or len(s) == 0:
        return 0
    l = 0
    r = 0
    max_len = 0
    num_index_map = {} 
    while r < len(s):
        if s[r] in num_index_map:
            prev_index = num_index_map[s[r]]
            if prev_index >= l:
                l = prev_index + 1
        max_len = max(max_len, r - l + 1)
        num_index_map[s[r]] = r
        r += 1
    return max_len

def print_index(s, substr):
    print s.index(substr)
    
def findSubstring(s, words):
        
    if s == None or len(s) == 0 or words == None or len(words) == 0:
        return []
    wlen = len(words[0])
    length_words = len(words)
    input = s
    indices = []
    offset = 0
    while len(input):
        min_index = 2147483647
        word_indices = []
        concat = True
        for word in words:
            try:
                windex = input.index(word)
            except ValueError as ve:
                concat = False
                break
            if windex != -1:
                word_indices.append(windex)
                min_index = min(min_index, windex)
            else:
                concat = False
                break
        if concat:
            start_index = min_index + wlen
            found_match = True
            for j in range(1, length_words):
                if start_index not in word_indices:        
                    found_match = False
                    break
                start_index += wlen
            if found_match:
                indices.append(min_index + offset)
                offset += start_index
                if offset < len(s):
                    input = s[offset:]
                else:
                    break
            else:
                break
        else:
            break           
    return indices    

def findSubstring2(s, words):
    if s == None or len(s) == 0 or words == None or len(words) == 0:
        return []
    wlen = len(words[0])
    words_length = len(words)
    start = 0
    block = wlen * words_length
    end = start + block - 1
    indices = []
    while end < len(s):
        input = s[start:end+1]
        found = True
        min_index = 2147483647
        left = 0
        right = left + wlen - 1
        tmp_words = words[:]
        while right < len(input):
            substr = input[left:right+1]
            if substr in tmp_words:
                min_index = min(left + start, min_index)
                tmp_words.remove(substr)
            else:
                found = False
                break
            left = right + 1
            right = left + wlen - 1
        if found:
            indices.append(min_index)
        start += 1
        end = start + block - 1
    return indices


def findSubstring3(s, words):
    if s == None or len(s) == 0 or words == None or len(words) == 0:
        return []
    wlen = len(words[0])
    words_length = len(words)
    start = 0
    block = wlen * words_length
    end = start + block - 1
    indices = []
    # build the word occurrence map
    word_occ_map = {}
    for word in words:
        count = 1
        if word in word_occ_map:
            count = word_occ_map[word]
            count += 1
        word_occ_map[word] = count
    while end < len(s):
        input = s[start:end+1]
        found = True
        min_index = 2147483647
        left = 0
        right = left + wlen - 1
        word_dyn_map = word_occ_map.copy()
        while right < len(input):
            substr = input[left : right + 1]
            if substr in word_occ_map.keys():
                count = word_dyn_map[substr]
                if count > 0:
                    count -= 1
                    word_dyn_map[substr] = count
                    min_index = min(left + start, min_index)    
            left = right + 1
            right = left + wlen - 1 
        for word in word_dyn_map:
            if word_dyn_map[word] > 0:
                found = False
                break
        if found:
            indices.append(min_index)
        start += 1
        end = start + block - 1
    return indices      

def findSubstring4(s, words):
    if s == None or len(s) == 0 or words == None or len(words) == 0:
        return []
    num = len(words)
    indices = []
    length = len(words[0])
    block = num * length
    words_map = {}
    for word in words:
        if word in words_map:
            words_map[word] += 1
        else:
            words_map[word] = 1
    end_index = len(s) - block
    i = 0
    while i <= end_index:
        seen_map = {}
        j = i
        while j < i + block:
            substr = s[j:j+length]
            if substr not in words_map:
                break
            else:
                if substr in seen_map:
                    seen_map[substr] += 1
                else:
                    seen_map[substr] = 1
                if seen_map[substr] > words_map[substr]:
                    break
            j += length
        if j == i + block:
            indices.append(i)
        i += 1
    return indices



if __name__ == '__main__':
    print findSubstring4("ababaab", ["ab", "ba", "ba"])
#     print findSubstring3("abababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababab",
#                          ["ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba"])
#     print findSubstring3("lingmindraboofooowingdingbarrwingmonkeypoundcake", ["fooo","barr","wing","ding","wing"])
#     print findSubstring3("foobarthebarfooman", ["foo", "bar"])
#     print_index('foobar', 'bar')
#     print lengthOfLongestSubstring('tmmzuxt')
#     print expand('abccba', 1, 2)
#     print expand('aabaac', 3, 3)
#     print expand('aabaac', 3, 4)
#     print expand('aabaac', 4, 4)
#     find_longest_palindromic_substring('abccba')