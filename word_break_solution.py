# 检查字符串s是否能由wordDict中的单词拼接而成
def can_break(s, word_dict):
    if s is not None and len(word_dict) != 0:
        need_compare_strings = [s]
        for string in need_compare_strings:
            for word in word_dict:
                if string.startswith(word):
                    word_length = len(word)
                    if len(string) == word_length:
                        return True
                    else:
                        temp = string[word_length:]
                        if temp not in need_compare_strings:
                            need_compare_strings.append(temp)
    return False
