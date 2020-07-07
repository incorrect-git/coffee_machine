res, i = 0, 0
while True:
    num = input()
    if num == '.':
        print(res / i)
        break
    i += 1
    res += int(num)
