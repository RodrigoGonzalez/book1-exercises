# chapter 5 invest.py
# calculate compound interest to track the growth of an investment


def invest(amount, rate, time):
    print(f"principal amount: ${amount}")
    print("annual rate of return:", rate)
    for t in range(1, time + 1):
        amount = amount * (1 + rate)
        print(f"year {t}: ${amount}")
    print()

invest(100, .05, 8)
invest(2000, .025, 5)
