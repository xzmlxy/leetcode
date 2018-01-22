#happy number是这样的数：个、十、百……位的数字的平方和组成新的数字，不断重复可最终到达1
def is_happy_number(n):
    if str(n).isdigit() and n > 0:
        old_data = {}
        while True:
            if n == 1:
                return True
            if n in old_data:
                return False
            old_data[n] = {n: 0}
            total = 0
            while True:
                total += pow(n % 10, 2)
                n = int(n / 10)
                if n == 0:
                    n = total
                    break
    return False
