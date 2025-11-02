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