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
            