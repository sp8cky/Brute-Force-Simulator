from account_handler import Account
from attack_simulator import AttackSimulator

def main():
    # create account
    account = Account("user1", "securepassword")

    # attack
    simulator = AttackSimulator(account)
    simulator.brute_force_attack("passwords.txt")

if __name__ == "__main__":
    main()