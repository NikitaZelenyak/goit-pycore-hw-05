import re
text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."

def generator_numbers(text: str):
    for match in re.findall(r'\d+\.\d+|\d+', text):
        yield float(match)

def sum_profit(text: str, generator):
    return sum(generator(text))

total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")
