import oop

# Khởi tạo dữ liệu
dtb = oop.PlayerDatabase("data.json")

# Kiểm tra dữ liệu
print("players_dict:", len(dtb.players_dict))
print("players_list:", len(dtb.players_list))

# Load data vào danh sách object
dtb.convert_to_object()

# Kiểm tra dữ liệu
print("players_dict:", len(dtb.players_dict))
print("players_list:", len(dtb.players_list))

# Hiển thị toàn bộ dữ liệu
dtb.show_all()

# Tìm kiếm theo tên
find1 = dtb.find_player_by_name("Lionel Messi")
find2 = dtb.find_player_by_name("Duc Trung")

    # Tìm thấy
if find1 != False:
    print("Found player:\n", find1.show_info())
else:
    print("Player not found!")

if find2 != False:
    print("Found player:\n", find2.show_info())
else:
    print("Player not found!")

    # Thêm 1 player mới
# Thêm 1 data mới
new_player = {
        "id": 9999999,
        "name": "Duc Khiem",
        "dob": "17/10/2013",
        "region": "Vietnam",
        "club": "Roblox",
        "rating": 1.0,
        "worth": 1
}
# dtb.add_player(new_player)

# Sửa thông tin
edit_player = {
        "id": 1,
        "name": "Duc Khiem hihi",
        "dob": "17/10/2013",
        "region": "Vietnam",
        "club": "Roblox",
        "rating": 1.0,
        "worth": 1
}
dtb.edit_player('Lionel Messi', edit_player)

# Xóa thông tin
dtb.delete_player("Duc Khiem hihi")