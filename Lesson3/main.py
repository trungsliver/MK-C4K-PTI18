import oop

# Khởi tạo data (UserDatabase)
dtb = oop.UserDatabase("data.json")

# Test data dạng dictionary
print("Dữ liệu dạng dictionary:", len(dtb.users_dict))

# test data dạng object
print("Dữ liệu dạng object trước khi load:", len(dtb.users_list))

# Load dữ liệu từ dictionary sang object
dtb.load_data()
print("Dữ liệu dạng object sau khi load:", len(dtb.users_list))

# Hiển thị tất cả dữ liệu (từ danh sách object - dtb.users_list)
dtb.show_all()