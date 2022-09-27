def card1(max_month):
    #   Paying of Credit Card Debt,
    #   Enter Month,
    #   Returns month, monthly interest, monthly and total debt paid
    total_credit = 5000
    total_paid = 0
    month = 0
    v, w, x, y, z = 0, 0, 0, 0, 0
    while month <= max_month:
        min_monthly_payment = total_credit * 0.02
        balance = total_credit - min_monthly_payment
        interest = 0.18/12 * balance
        total_month = interest + balance
        w = round(total_credit, 2)
        x = round(interest, 2)
        y = round(min_monthly_payment, 2)
        z = round(total_paid, 2)
        v = month
        total_credit = total_month
        total_paid += min_monthly_payment
        month += 1
    print(f'''Month:  {v}
Balance:  {w}
Monthly Interest:  {x}
Monthly Payment:  {y}
Total Paid:  {z}
''')
    return v, w, x, y, z


while True:
    try:
        max_month = int(input('Enter Month > '))
        fed = card1(max_month)
    except ValueError:
        print('Please enter integer...\n')
