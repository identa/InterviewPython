# Viết chương trình đếm số bit được đặt thành 1 trong số nguyên dương là một cách tốt để tăng tốc với các kiểu nguyên thủy.
# Chương trình sau đây kiểm tra các bit một lần bắt đầu với bit có trọng số thấp nhất.
# Nó minh họa sự dịch chuyển và mặt nạ; nó cũng chỉ ra cách tránh mã hóa cứng kích thước của từ nguyên.


def countbits(x):
    num_bits = 0
    while x:
        num_bits += x & 1
        x >>= 1
    return num_bits


def main():
    parity(10)




# Tính toán chẵn lẻ của một từ(Computing the parity of a word)

# Tính chẵn lẻ của một từ nhị phân là 1 nếu số 1s trong từ là số lẻ; mặt khác, nó là 0.
# Ví dụ, chẵn lẻ của 1011 là 1 và chẵn lẻ của 10001000 là 0.
# Kiểm tra chẵn lẻ được sử dụng để phát hiện các lỗi bit đơn giản trong lưu trữ dữ liệu và giao tiếp.
# Khá đơn giản để viết mã tính toán tính chẵn lẻ của một từ 64 bit.


def parity(x):
    result = 0
    while x:
        a = x & 1
        result ^= x & 1  # result = result xor (x and 1)
        x >>= 1  # x = x >> 1
    return result

if __name__ == '__main__':
    main()