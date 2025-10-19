# DICTIONARY & MAP
# Bài 1: Cho 1 danh sách gồm tên của học sinh (viết hoa lộn xộn)
# Yêu cầu: Dùng map() để chuyển đổi danh sách trên viết hoa tất cả chữ
# Ví dụ: tRunG -> TRUNG
PTI18 = ['mInh', 'kHIEm', 'tRi', 'BAcH', 'nGUyen']
    # cách 1: 
def convert_name(name):
    # upper(): chuyển tất cả chữ thường thành chữ hoa
    return name.upper()
    # Hiển thi kết quả
pti18_1 = map(convert_name, PTI18)
print(list(pti18_1))

    # cách 2: dùng lambda function
pti18_2 = map(lambda name: name.upper(), PTI18)
print(list(pti18_2))

# Bài 2: Quản lý thông tin sinh viên
# #Yêu cầu: Tạo một dictionary lưu trữ thông tin sinh viên với các khóa: name, age, và grade. 
# Thực hiện các thao tác sau:
# 1. Thêm sinh viên với thông tin name = "John", age = 22, và grade = "A".
student = {
    "name": "John",
    "age": 22,
    "grade": "A"
}
# 2. Cập nhật grade của sinh viên thành "A+".
student["grade"] = "A+"
# 3. Xóa thông tin age của sinh viên.
del student["age"]
# 4. Kiểm tra xem name có trong dictionary không.
print("name" in student)

# Bài 3: Đếm Số Lần Xuất Hiện Của Từ Trong Chuỗi
# Yêu cầu: Viết chương trình nhận vào một chuỗi và trả về một dictionary đếm số lần xuất hiện của mỗi từ trong chuỗi.
sentence = 'this is a test this is only a test'

def count_words(sentence):
    # strip(): xóa khoảng trắng ở đầu và cuối
    # split(): tách chuỗi thành danh sách
    words = sentence.strip().split()
    # Tạo dictionary rỗng để lưu kết quả
    word_count = {}
    # Duyệt danh sách từ
    for word in words:
        if word in word_count:      # word đã có trong dictionary
            word_count[word] += 1
        else:                       # word chưa có trong dictionary   
            word_count[word] = 1
    return word_count   
print(count_words(sentence))


# Bài 4: Gộp Hai Dictionary
# Yêu cầu: Cho hai dictionary A và B. Viết chương trình gộp chúng lại. Nếu một key xuất hiện ở cả hai dictionary, cộng giá trị của chúng lại.
A = {'a': 100, 'b': 200, 'c': 300}
B = {'b': 250, 'c': 150, 'd': 400}

def merge1(dict1, dict2):
    # Tạo bản sao của dict1 để không bị thay đổi dữ liệu
    merge_dict = dict1.copy()
    # Duyệt dict2
    for key, value in dict2.items():
        if key in merge_dict:
            merge_dict[key] += value
        else:
            merge_dict[key] = value
    return merge_dict
print(merge1(A, B))

# Bài 5: Tìm Key Có Giá Trị Lớn Nhất
# Yêu cầu: Cho một dictionary có các cặp {key: value}. Viết chương trình để tìm key có giá trị lớn nhất.
def find_max_key(dict):
    # Khai báo value lớn nhất là value đầu tiên trong dict
    max_value = list(dict.values())[0]
    # Khai báo key lớn nhất mặc định là key đầu tiên
    max_key = list(dict.keys())[0]
    # Duyệt dict
    for key, value in dict.items():
        # Nếu value lớn hơn max_value thì cập nhật max_value và max_key
        if value > max_value:
            max_value = value
            max_key = key
    return max_key
print(find_max_key(A))
print(find_max_key(B))

    # Cách 2
def find_max_key_2(dict1):
    # sử dụng max() với key để tìm key có giá trị lớn nhất
    return max(dict1, key = dict1.get)
print(find_max_key_2(A))
print(find_max_key_2(B))

# Bài 6: Sắp Xếp Dictionary Theo Giá Trị
# Yêu cầu: Viết chương trình để sắp xếp một dictionary theo giá trị từ cao đến thấp.
grade = {
    'Đức Minh': 1,
    'Quang Huy': 7,
    'Hoàng Bách': 9,
    'Minh Nhật': 7.5,
    'Xuân Tú': 8
}
def sort_dict(dictionary):
    # sử dụng sorted() với key để sắp xếp dictionary
    return dict(sorted(dictionary.items(), key=lambda item: item[1], reverse=True))
print(sort_dict(grade))

# Bài 7: Nhóm Các Phần Tử Theo Giá Trị
# Yêu cầu: Viết chương trình để nhóm các phần tử của một dictionary dựa trên giá trị của chúng. Ví dụ, các phần tử có cùng giá trị sẽ được đưa vào một danh sách.
data = {
    'apple': 1,
    'banana': 2,
    'cherry': 2,
    'bomb': 3,
    'elderberry': 3
}

def group_by_value(dict):
    # Khai báo dict để lưu các phần tử có cùng số lượng
    group_dict = {}
    # Duyệt dict
    for key, value in dict.items():
        # Nếu value chưa có trong group_dict thì thêm vào
        if value not in group_dict:
            group_dict[value] = []
        # Nếu value đã có trong group_dict thì thêm key vào danh sách
        group_dict[value].append(key)
    return group_dict
print(group_by_value(data))
        

# Bài 8: Tạo Dictionary Từ Danh Sách
# Yêu cầu: Viết chương trình tạo một dictionary từ hai danh sách: một danh sách chứa key và một danh sách chứa value tương ứng.
keys = ['apple', 'banana', 'cherry']
values = [1, 2, 3]
def list_to_dict(keys, values):
    # zip(): tạo ra các cặp key-value từ 2 danh sách
    # dict(): chuyển các cặp key-value thành dictionary
    return dict(zip(keys, values))
print(list_to_dict(keys, values))
