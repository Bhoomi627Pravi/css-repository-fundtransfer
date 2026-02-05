from abc import ABC, abstractmethod

# Abstract Base Class
class FundTransfer(ABC):
    def __init__(self, account_number: int, balance: float):
        self._account_number = account_number
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, amount):
        self._balance = amount

    def validate(self, amount):
        # 10-digit check and balance check
        if len(str(self._account_number)) == 10 and 0 < amount <= self._balance:
            return True
        else:
            print("Account Number or transfer amount seems to be wrong")
            return False

    @abstractmethod
    def transfer(self, amount):
        pass

# NEFT: 2% Service Charge
class NEFTTransfer(FundTransfer):
    def transfer(self, amount):
        if self.validate(amount):
            charge = amount * 0.02
            if (amount + charge) <= self.balance:
                self.balance -= (amount + charge)
                print(f"NEFT: ₹{amount} sent. Fee: ₹{charge}. New Balance: ₹{self.balance}")
                return True
            else:
                print("NEFT: Insufficient balance for fee.")
        return False

# RTGS: Min amount > 10,000
class RTGSTransfer(FundTransfer):
    def transfer(self, amount):
        if self.validate(amount):
            if amount > 10000:
                self.balance -= amount
                print(f"RTGS: ₹{amount} sent. New Balance: ₹{self.balance}")
                return True
            else:
                print("RTGS: Failed. Amount must be > ₹10,000.")
        return False

# IMPS: Instant, ₹5 Fixed Fee
class IMPSTransfer(FundTransfer):
    def transfer(self, amount):
        if self.validate(amount):
            fee = 5.0
            if (amount + fee) <= self.balance:
                self.balance -= (amount + fee)
                print(f"IMPS: ₹{amount} sent. Fee: ₹{fee}. New Balance: ₹{self.balance}")
                return True
            else:
                print("IMPS: Insufficient balance for fee.")
        return False

# PTGS: Priority Transfer (Custom 5% High Priority Fee)
class PTGSTransfer(FundTransfer):
    def transfer(self, amount):
        if self.validate(amount):
            priority_fee = amount * 0.05  # 5% Priority handling
            if (amount + priority_fee) <= self.balance:
                self.balance -= (amount + priority_fee)
                print(f"PTGS: ₹{amount} sent. Priority Fee: ₹{priority_fee}. New Balance: ₹{self.balance}")
                return True
            else:
                print("PTGS: Insufficient balance for priority fee.")
        return False

# --- RUNNING THE APPLICATION ---

if __name__ == "__main__":
    # Test NEFT
    acc_neft = NEFTTransfer(1234567890, 5000)
    acc_neft.transfer(1000)

    # Test RTGS
    acc_rtgs = RTGSTransfer(9876543210, 20000)
    acc_rtgs.transfer(15000)

    # Test IMPS
    acc_imps = IMPSTransfer(1122334455, 1000)
    acc_imps.transfer(500)

    # Test PTGS
    acc_ptgs = PTGSTransfer(5566778899, 10000)
    acc_ptgs.transfer(2000)
    