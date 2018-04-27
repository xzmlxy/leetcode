# 给定一个字符串s和一组字符串d,在d中寻找可由s删减字符得到的字符串。如果存在多个，返回最长的那个；如果存在多个等最长的，返回排序后更靠前的


def find_longest_word(s, d):
    result = None
    len_target = len(s)
    if len_target > 0 and len(d) > 0:
        len_result = 0
        for string in d:
            len_string = len(string)
            if len_string < len_result:
                continue
            else:
                i = -1
                j = -1
                while i < len_string - 1 and j < len_target - 1:
                    i += 1
                    j += 1
                    while string[i] != s[j] and j < len_target - 1:
                        j += 1
                if string[i] == s[j] and i == len_string - 1:
                    if len_string > len_result or string < result:
                        len_result = len_string
                        result = string
    return result
