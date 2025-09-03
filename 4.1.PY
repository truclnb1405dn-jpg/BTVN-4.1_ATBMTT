def caesar_encrypt(text, key):
    result = ""
    for char in text:
        # Kiểm tra ký tự có phải chữ hoa không
        if char.isupper():
            # Dịch chuyển ký tự trong bảng chữ cái hoa
            result += chr((ord(char) - ord('A') + key) % 26 + ord('A'))
        # Kiểm tra ký tự có phải chữ thường không
        else:
            # Dịch chuyển ký tự trong bảng chữ cái thường
            result += chr((ord(char) - ord('a') + key) % 26 + ord('a'))
    return result
# Ví dụ sử dụng

text = "Truc"
key = 12
print(caesar_encrypt(text, key))