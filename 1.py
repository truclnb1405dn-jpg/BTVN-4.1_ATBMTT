import sys

# Đánh số bảng chữ cái từ 1 đến 26
def text_to_numbers(text):
    numbers = []
    # Chuyển đổi toàn bộ văn bản thành chữ thường để xử lý đồng nhất
    text = text.lower()
    for char in text:
        if 'a' <= char <= 'z':
            # Giá trị ASCII của 'a' là 97, nên ta trừ đi 96 để có a=1, b=2, ...
            number = ord(char) - 96
            numbers.append(number)
        else:
            # Nếu không phải chữ cái, gán giá trị 0 hoặc bỏ qua
            numbers.append(0)
    return numbers

# Mã hóa
def rsa_encrypt(n, e, plaintext_numbers):

    ciphertext = []
    for m in plaintext_numbers:
        c = pow(m, e, n)
        ciphertext.append(c)
    return ciphertext

# Hàm chính để chạy chương trình
def main():
    # Nhập khóa công khai K(n, e) từ người dùng
    try:
        n = int(input("Nhập giá trị n của khóa K(n, e): "))
        e = int(input("Nhập giá trị e của khóa K(n, e): "))
    except ValueError:
        print("Lỗi: Giá trị nhập vào phải là số nguyên.")
        sys.exit(1)

    # Nhập văn bản cần mã hóa
    # input_text = "Truc"
    input_text = input("Nhập văn bản bạn muốn mã hóa: ")

    # Chuyển đổi văn bản thành số
    numbers_to_encrypt = text_to_numbers(input_text)

    # Mã hóa các số
    encrypted_numbers = rsa_encrypt(n, e, numbers_to_encrypt)
    print(f"Chuỗi số đã mã hóa: {encrypted_numbers}")

# Chạy chương trình
if __name__ == "__main__":
    main()