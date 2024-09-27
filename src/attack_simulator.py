import time

class AttackSimulator:
    def __init__(self, account):
        self.account = account

    def load_passwords(self, password_file):
        try:
            with open(password_file, 'r') as file:
                passwords = [line.strip() for line in file]  # remove newline characters
            return passwords
        except FileNotFoundError:
            print("Password file not found.")
            return []

    def brute_force_attack(self, password_file):
        passwords = self.load_passwords(password_file)  # load passwords from file

        for password in passwords:
            if self.account.locked:
                print("Account is locked.")
                break
            
            if self.try_password(password):
                print(f"Password found: {password}")
                return
            else:
                self.account.failed_attempts += 1
                print(f"Failed attempt with: {password}")
                
                # lock account after 3 failed attempts
                if self.account.failed_attempts >= 3:
                    self.account.lock_account()
                    print("Account locked due to too many failed attempts.")
                    break
            time.sleep(1)  # simulate delay between attempts

    def try_password(self, password):
        return password == self.account.password
