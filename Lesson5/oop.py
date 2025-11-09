import data_io

class User:
    def __init__(self, email, password):
        self.email = email
        self.password = password

    def update(self, new_data:dict):
        # Chỉ khi có thuộc tính mới update
        for key, value in new_data.items():
            if value:
                setattr(self, key, value)

    def show_info(self):
        print(f'Email: {self.email} - Password: {self.password}')

class UserDatabase:
    def __init__ (self, file_path):
        # filepath: đường dẫn đến file dữ liệu
        self.file_path = file_path
        # Danh sách dạng object / list
        self.users_list = list()
        # Danh sách dạng dictionary / json
        self.users_dict = data_io.load_json_data(self.file_path)

    # Chuyển danh sách dictonary => object
    def convert_to_object(self):
        new_users = []
        for user_data in self.users_dict:
            user = User(email = user_data["email"],
                        password = user_data["password"])
            new_users.append(user)
        self.users_list = new_users
        