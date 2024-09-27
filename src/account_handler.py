class Account:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.locked = False
        self.failed_attempts = 0

    def lock_account(self):
        self.locked = True

    def unlock_account(self):
        self.locked = False
        self.failed_attempts = 0