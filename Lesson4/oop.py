import data_io

class Player:
    def __init__(self, id, name, dob, region, club, rating=None, worth=None):
        self.id = id
        self.name = name
        self.dob = dob
        self.region = region
        self.club = club
        # Nếu có thì định dạng float, không có thì mặc định = 0
        self.rating = float(rating) if rating else 0
        self.worth = float(worth) if worth else 0

    def show_info(self):
        print(f"""====================
ID:         {self.id}
Name:       {self.name}
DOB:        {self.dob}
Region:     {self.region}
Club:       {self.club}
Rating:     {self.rating}
Worth:      {self.worth}
====================""")
        
    def update(self, new_data:dict):
        for key, value in new_data.items():
            # Chỉ khi nào có thuộc tính mới gán giá trị (update)
            if value:
                setattr(self, key, value)
            
class PlayerDatabase:
    def __init__(self, file_path):
        # filepath: đường dẫn đến file dữ liệu
        self.file_path = file_path
        # Danh sách dạng object Player
        self.players_list = list()
        # Danh sách dạng dictionary
        self.players_dict = data_io.load_json_data(file_path)

    # Chuyển đổi từ dict sang object Player
    def convert_to_object(self):
        new_players = []
        for player_data in self.players_dict:
            player = Player(id = player_data["id"],
                            name = player_data['name'],
                            dob = player_data['dob'],
                            region = player_data['region'],
                            club = player_data['club'],
                            rating = player_data['rating'],
                            worth = player_data['worth'])
            new_players.append(player)
        self.players_list = new_players

    # Chuyển từ object => dictionary / json
    def convert_to_dict(self):
        json_data = list()
        for player in self.players_list:
            json_data.append(player.__dict__)
        return json_data

