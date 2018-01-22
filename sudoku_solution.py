def solve_sudoku(sudoku):
    complete_solve_sudoku(sudoku)
    print(sudoku)


def complete_solve_sudoku(sudoku):
    point = find_next_point(sudoku)
    if point is not None:
        solutions_of_point = find_all_solution(point, sudoku)
        num_of_solutions = len(solutions_of_point)
        if num_of_solutions == 0:
            return False
        for i in range(0, num_of_solutions):
            sudoku[point[0]][point[1]] = solutions_of_point[i]
            if not complete_solve_sudoku(sudoku):
                if i == num_of_solutions - 1:
                    sudoku[point[0]][point[1]] = "."
                    return False
            else:
                return True
    return True


def find_next_point(sudoku):
    for i in range(0, 9):
        for j in range(0, 9):
            if sudoku[i][j] == ".":
                return [i, j]
    return None


def find_all_solution(point, sudoku):
    result = []
    for i in range(1, 10):
        temp = str(i)
        if temp in sudoku[point[0]]:
            continue
        is_same = False
        for j in range(0, 9):
            if temp == sudoku[j][point[1]]:
                is_same = True
                break
        if not is_same:
            if point[0] < 3:
                up_down_start = 0
                up_down_end = 3
            elif point[0] > 5:
                up_down_start = 6
                up_down_end = 9
            else:
                up_down_start = 3
                up_down_end = 6
            if point[1] < 3:
                left_right_start = 0
                left_right_end = 3
            elif point[1] > 5:
                left_right_start = 6
                left_right_end = 9
            else:
                left_right_start = 3
                left_right_end = 6
            for j in range(up_down_start, up_down_end):
                for k in range(left_right_start, left_right_end):
                    if temp == sudoku[j][k]:
                        is_same = True
                        break
        if not is_same:
            result.append(temp)
    return result
