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

    return  -digit if is_negative else digit

def main():
    print(string_to_int("-123"))

if __name__ == '__main__':
    main()