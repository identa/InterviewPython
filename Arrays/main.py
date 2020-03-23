# Viết chương trình lấy đầu vào là một mảng các chữ số mã hóa số nguyên thập phân D không âm và cập nhật mảng để biểu diễn số nguyên D + 1.
# Ví dụ: nếu đầu vào là (1,2,9) thì bạn nên cập nhật mảng thành (1,3,0).
# Thuật toán của bạn sẽ hoạt động ngay cả khi nó được thực hiện bằng ngôn ngữ có số học chính xác hữu hạn.


def add(A):
    A[-1] += 1
    for i in reversed(range(1, len(A))):
        if A[i] != 10:
            break
        A[i] = 0
        A[i - 1] += 1
    if A[0] == 10:
        A[0] = 1
        A.append(0)
    return A


# Một chuỗi là một chuỗi các ký tự. Một chuỗi có thể mã hóa một số nguyên, ví dụ: "123" mã hóa 123.
# Trong vấn đề này, bạn phải thực hiện các phương thức lấy một chuỗi đại diện cho một số nguyên và trả về số nguyên tương ứng và ngược lại.
# Mã của bạn nên xử lý số nguyên âm. Bạn không thể sử dụng các hàm thư viện như int trong Python.

def int_to_string(a):
    is_negative = False
    if a < 0:
        a = -a
        is_negative = True
    s = []
    while True:
        a1 = a % 10
        s.append(chr(ord('0') + a1))
        a //= 10
        if a == 0:
            break
    return ''.join(reversed(s)) if is_negative else '-'.join(reversed(s))


def string_to_int(str):
    digit = 0
    is_negative = False
    if str[0] == '-':
        is_negative = True
        str = str[1::]

    for chr in str:
        digit *= 10
        digit += (ord(chr) - ord('0'))

    return -digit if is_negative else digit


# Một số ứng dụng yêu cầu số học chính xác tùy ý.
# Một cách để đạt được điều này là sử dụng các mảng để biểu diễn các số nguyên, 
# ví dụ: với một chữ số trên mỗi mục nhập với chữ số có ý nghĩa nhất xuất hiện đầu tiên và một chữ số hàng đầu âm biểu thị một số nguyên âm.
# Ví dụ: (1,9,3,7,0,7,7,2,1) đại diện cho 193707721 và (-7,6,1,8,3,8,2,5,7,2,8,7) đại diện cho -761838257287.


def array_to_digit(array):
    digit = array[0] * 10 ** (len(array) - 1)
    is_negative = False
    if array[0] < 0:
        is_negative = True
    for i in range(1, len(array)):
        if is_negative:
            digit += (-1) * 10 ** (len(array) - i - 1) * array[i]
        else:
            digit += 10 ** (len(array) - i - 1) * array[i]
    return digit



# Vấn đề này liên quan đến vấn đề mua và bán cổ phiếu một cách tối ưu một lần, như được mô tả trên Trang 2.
# Ví dụ, hãy xem xét trình tự sau của giá cổ phiếu (310.315.275.295.260.270.290.230.255.250).
# Lợi nhuận tối đa có thể được thực hiện với một lần mua và một lần bán là 30 --- mua ở mức 260 và bán ở mức 290.
# Lưu ý rằng 250 không phải là giá thấp nhất, cũng không phải là 290 giá cao nhất.
# Viết chương trình lấy một mảng biểu thị giá cổ phiếu hàng ngày và lấy lại lợi nhuận tối đa có thể kiếm được bằng cách mua và sau đó bán một cổ phiếu của cổ phiếu đó. Không cần phải mua nếu không có lợi nhuận.


import math


def buy_and_sell_stock_once(prices):
    min_price_so_far, max_profit = math.inf, 0.0
    for price in prices:
        max_profit_sell_today = price - min_price_so_far
        max_profit = max(max_profit, max_profit_sell_today)
        min_price_so_far = min(min_price_so_far, price)
    return max_profit


def main():
    print(buy_and_sell_stock_once([1, 2, 3, 4]))


if __name__ == '__main__':
    main()
