# 判断两个字符串格式是否相形，如“AABB”和“CCDD”便是同形的
def is_isomorphic(s, t):
    word_map = {}
    for i in range(0, len(s)):
        a = s[i]
        b = t[i]
        if a not in word_map:
            if b in word_map.values():
                return False
            else:
                word_map[a] = b
        else:
            if word_map[a] != b:
                return False
    return True
