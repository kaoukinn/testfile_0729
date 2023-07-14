# 第一題:寫出一個99乘法表
for i in range(1, 10):
    for j in range(1, 10):
        product = i * j
        print(f"{i} x {j} = {product}")
    print()

# 第二題:有1、2、3、4個數字，能組成多少個互不相同且無重複數字的三位元數？都是多少？(EX: 123 => OK , 112 => 1有重複)
count = 0
for i in range(1, 5):
    for j in range(1, 5):
        for k in range(1, 5):
            if i != j and i != k and j != k:
                number = i * 100 + j * 10 + k
                print(number)
                count += 1
print("總數量:", count)

# 第三題:輸入三個整數x,y,z，請把這三個數由小到大輸出。
x = int(input("請輸入第一個整數 x："))
y = int(input("請輸入第二個整數 y："))
z = int(input("請輸入第三個整數 z："))

numbers = [x, y, z]
numbers.sort()
print("由小到大排序：", numbers)

# 第四題:請設計一程式檢查輸入的身份證代號是否正確
def check_id(in_txt):
    check_num = 0

    if in_txt[0] == 'A':
        check_num += 1 + 0 * 9
    elif in_txt[0] == 'B':
        check_num += 1 + 1 * 9
    elif in_txt[0] == 'C':
        check_num += 1 + 2 * 9
    elif in_txt[0] == 'D':
        check_num += 1 + 3 * 9
    elif in_txt[0] == 'E':
        check_num += 1 + 4 * 9
    elif in_txt[0] == 'F':
        check_num += 1 + 5 * 9
    elif in_txt[0] == 'G':
        check_num += 1 + 6 * 9
    elif in_txt[0] == 'H':
        check_num += 1 + 7 * 9
    elif in_txt[0] == 'I':
        check_num += 3 + 4 * 9
    elif in_txt[0] == 'J':
        check_num += 1 + 8 * 9
    elif in_txt[0] == 'K':
        check_num += 1 + 9 * 9
    elif in_txt[0] == 'L':
        check_num += 2 + 0 * 9
    elif in_txt[0] == 'M':
        check_num += 2 + 1 * 9
    elif in_txt[0] == 'N':
        check_num += 2 + 2 * 9
    elif in_txt[0] == 'O':
        check_num += 3 + 5 * 9
    elif in_txt[0] == 'P':
        check_num += 2 + 3 * 9
    elif in_txt[0] == 'Q':
        check_num += 2 + 4 * 9
    elif in_txt[0] == 'R':
        check_num += 2 + 5 * 9
    elif in_txt[0] == 'S':
        check_num += 2 + 6 * 9
    elif in_txt[0] == 'T':
        check_num += 2 + 7 * 9
    elif in_txt[0] == 'U':
        check_num += 2 + 8 * 9
    elif in_txt[0] == 'V':
        check_num += 2 + 9 * 9
    elif in_txt[0] == 'W':
        check_num += 3 + 2 * 9
    elif in_txt[0] == 'X':
        check_num += 3 + 0 * 9
    elif in_txt[0] == 'Y':
        check_num += 3 + 1 * 9
    else:
        check_num += 3 + 3 * 9

    check_num += int(in_txt[1]) * 8
    check_num += int(in_txt[2]) * 7
    check_num += int(in_txt[3]) * 6
    check_num += int(in_txt[4]) * 5
    check_num += int(in_txt[5]) * 4
    check_num += int(in_txt[6]) * 3
    check_num += int(in_txt[7]) * 2
    check_num += int(in_txt[8])
    check_num += int(in_txt[9])

    if check_num % 10 == 0:
        return True
    else:
        return False

id_number = input("請輸入身份證代號：")
if check_id(id_number):
    print("身份證代號正確")
else:
    print("身份證代號錯誤")