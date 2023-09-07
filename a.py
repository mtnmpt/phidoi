def are_strings_equal(string1, string2):
    return string1 == string2

# Nhập hai chuỗi từ người dùng
input1 = input("Nhập chuỗi thứ nhất: ")
input2 = input("Nhập chuỗi thứ hai: ")

# Kiểm tra sự trùng lặp và in kết quả
if are_strings_equal(input1, input2):
    print("Hai chuỗi trùng nhau.")
else:
    print("Hai chuỗi không trùng nhau.")
