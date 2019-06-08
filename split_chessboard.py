import numpy as np
import time


# 有一个棋盘（8*8），棋盘每格存在一个数字（用二维数组chessboard表示），经cut次切割后分为cut+1个矩形，求这n+1个矩阵的最小均方差
# 切割时有如下要求：再次切割时，只能切分上一次切割后得到的某一个子块

class Answer:
    area = "area"
    length = 8

    def __init__(self, chessboard, cut):
        self.rectangles = []
        for i in range(0, Answer.length):
            temp1 = []
            for j in range(0, Answer.length):
                temp2 = []
                for k in range(0, Answer.length + 1):
                    temp3 = []
                    for l in range(0, Answer.length + 1):
                        temp3.append({})
                    temp2.append(temp3)
                temp1.append(temp2)
            self.rectangles.append(temp1)
        self.cut = cut
        if isinstance(chessboard, str):
            self.chessboard = Answer.pretreatment(chessboard)
        else:
            self.chessboard = chessboard
        self.average = float(np.sum(self.chessboard)) / (self.cut + 1)
        self.total = np.sum(self.chessboard) ** 2
        # for row in self.chessboard:
        #     print(row)

    @staticmethod
    def pretreatment(chessboard_string):
        chessboard_string_list = chessboard_string.split(" ")
        assert len(chessboard_string_list) == 64
        i = 0
        temp = []
        result = []
        for s in chessboard_string_list:
            temp.append(int(s))
            i += 1
            if i == Answer.length:
                result.append(temp)
                temp = []
                i = 0
        return result

    def count_min_variance(self):
        for high in range(1, Answer.length + 1):
            for width in range(1, Answer.length + 1):
                for row in range(0, Answer.length + 1 - high):
                    for column in range(0, Answer.length + 1 - width):
                        self._build_min_variance_dic(column, row, width, high)
        return round((self.rectangles[0][0][Answer.length][Answer.length][self.cut] / (self.cut + 1)) ** 0.5, 3)

    def _build_min_variance_dic(self, x, y, w, h):
        max_cut = self._get_max_cut(x, y, w, h)
        for i in range(0, max_cut + 1):
            self.rectangles[x][y][w][h][i] = self._count_small_rec_variance(x, y, w, h, i)

    def _get_max_cut(self, x, y, w, h):
        this_cut = self.cut
        if x > 0:
            this_cut -= 1
        if y > 0:
            this_cut -= 1
        if x + w < Answer.length:
            this_cut -= 1
        if y + h < Answer.length:
            this_cut -= 1
        return min(w + h - 2, max(this_cut, 0))

    def _count_small_rec_variance(self, x, y, w, h, cut):
        if cut == 0:
            self.rectangles[x][y][w][h][Answer.area] = self._get_area(x, y, w, h)
            return (self.rectangles[x][y][w][h][Answer.area] - self.average) ** 2
        else:
            return self._get_min_variance_square(x, y, w, h, cut)

    def _get_area(self, x, y, w, h):
        if h > 1:
            return self.rectangles[x][y][w][h - 1][Answer.area] + self.rectangles[x][y + h - 1][w][1][Answer.area]
        if w > 1:
            return self.rectangles[x][y][w - 1][h][Answer.area] + self.rectangles[x + w - 1][y][1][h][Answer.area]
        return self.chessboard[y][x]

    def _get_min_variance_square(self, x, y, w, h, cut):
        cut -= 1
        min_variance_square = self.total
        for i in range(1, h):
            if cut in self.rectangles[x][y][w][i]:
                temp1 = self.rectangles[x][y][w][i][cut] + self.rectangles[x][y + i][w][h - i][0]
            else:
                temp1 = None
            if cut in self.rectangles[x][y + i][w][h - i]:
                temp2 = self.rectangles[x][y][w][i][0] + self.rectangles[x][y + i][w][h - i][cut]
            else:
                temp2 = None
            min_variance_square = Answer._find_min_without_none(min_variance_square, temp1, temp2)
        for i in range(1, w):
            if cut in self.rectangles[x][y][i][h]:
                temp1 = self.rectangles[x][y][i][h][cut] + self.rectangles[x + i][y][w - i][h][0]
            else:
                temp1 = None
            if cut in self.rectangles[x + i][y][w - i][h]:
                temp2 = self.rectangles[x][y][i][h][0] + self.rectangles[x + i][y][w - i][h][cut]
            else:
                temp2 = None
            min_variance_square = Answer._find_min_without_none(min_variance_square, temp1, temp2)
        return min_variance_square

    @staticmethod
    def _find_min_without_none(min_var, temp1, temp2):
        result = min_var
        if temp1 is not None:
            result = min(min_var, temp1)
        if temp2 is not None:
            result = min(min_var, temp2)
        return result


chessboard_string_test = "1 1 1 1 1 1 1 3 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1" \
                         " 1 1 1 1 1 1 1 1 1 1 1 1 0 1 1 1 1 1 1 0 3"
cut_number = 2
answer = 1.633
Answer1 = Answer(chessboard_string_test, cut_number)

time_start = time.time()
print(Answer1.count_min_variance())
print(time.time() - time_start)
