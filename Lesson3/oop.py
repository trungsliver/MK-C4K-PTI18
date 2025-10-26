class User:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

    def display_info(self):
        return f"{self.username} - {self.email} - {self.password}"