# CRUD - Create, Read, Update, Delete

# Create
dict1 = {}
dict2 = {
    # Các cặp key - value
    "name": "Trần Bảo Hoàng",
    "age": 13,
    "gender": "male"
}

# Read - Duyệt, hiện phần tử
    # Duyệt toàn bộ key-value
for key, value in dict2.items():
    print(f"{key}: {value}")
    # Truy cập bằng key
print(dict2["name"])
    # Sử dụng phương thức get()
print('Tên:', dict2.get('name'))
    # Nếu không tồn tại key => None / Giá trị mặc định
print('Money:', dict2.get('money'))
print('Girlfriend:', dict2.get('gf', '404 not found'))

# Update - chỉnh sửa
    # Thêm cặp key - value
dict2['laptop'] = 'Lenovo'
    # Chỉnh sửa value
dict2['name'] = 'Khiêm khúc khích'
print(dict2)

# Delete - Xóa 
    # Xóa theo key - del
del dict2['laptop']
    # Xóa theo key, trả về value - pop()
# dict2.pop('gender')
print(dict2.pop('gender'))

# Kiểm tra key tồn tại
print('name' in dict2)          # True
print('girlfriend' in dict2)    # False

# Lấy tất cả cặp key - value: items()
print(dict2.items())
# Lấy tất cả key: keys()
print(dict2.keys())
# Lấy tất cả value: values()
print(dict2.values())