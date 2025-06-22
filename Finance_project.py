#installing yfinance - using API
import yfinance as yf

#stock price tracker
#r:.2f means interest rate is noted to 2 decimal places
def stock_price_tracker():
    #.upper() makes line all caps
    ticker = input("Enter stock ticker (e.g. NVDA): ").upper()
    stock = yf.Ticker(ticker)
    #.historty() fetches historical market data, period = '1d' means data for past 1d trading, interval = '1m' means return data in 1-min intervals
    data = stock.history(period = '1d', interval = '1m')

    #last row as a data frame, data.tail(1) gives last row as DataFrame
    last_row = data.tail(1) 

    #last_row['Close'] means close pricve column from last row, .values[0] extracts actual numeric value from column
    current_price = last_row['Close'].values[0]

    #:.2f rounds to 2 decimal places
    print(f"\n{ticker} Current Price: £{current_price:.2f}")

#loan calculator
def loan_calculator():
    principal = float(input("Enter loan amount: "))
    annual_rate = float(input("Enter annual interest rate (in %): "))
    years = int(input("Enter loan term (in years): "))

    monthly_rate = annual_rate / 100 / 12
    months = years * 12

    if monthly_rate == 0:
        monthly_payment = principal / months
    else:
        monthly_payment = principal * monthly_rate * (1 + monthly_rate) ** months / ((1 + monthly_rate) ** months - 1)

    print(f"\nMonthly Payment: ${monthly_payment:.2f}")
    print(f"Total Payment: ${monthly_payment * months:.2f}")
    print(f"Total Interest: ${(monthly_payment * months) - principal:.2f}\n")

#savings goal forecaster
import math

def savings_goal_forecaster():
    future_value_goal = float(input("Enter your goal value:"))
    contribution = float(input("Enter how much you will contribute per period: "))
    annual_rate = float(input("Enter annual interest rate (in %): "))
    time_period = float(input("Enter number of periods (in months): "))

    #convert annual rate % to monthly decimal rate
    r = (annual_rate / 100) / 12

    #calculate future value using formula
    future_value_goal = contribution * ((1 + r)**time_period - 1) / r
   
    # Print the formula used
    #r:.5f means interest rate is noted to 5 decimal places
    print(f"\nUsing formula: FV = P × ((1 + r)^n - 1) / r")
    print(f"FV = {contribution} x ((1 + {r:.5f})^{time_period} - 1) / {r:.5f}")
    print(f"\nYour future value after {time_period} months will be: £{future_value_goal:.2f}")
    
def main():
    while True:
        print("Choose a tool:")
        print("1. Stock Price Tracker")
        print("2. Loan Calculator")
        print("3. Savings goal Forecaster")
        print("4. Exit")
        choice = input("Enter your choice (1/2/3/4): ")

#needs stock_price_tracker() or savings_goal_forecaster() after to allow code to run
        if choice == '1':
            stock_price_tracker()
        elif choice == '2':
            loan_calculator()
        elif choice == '3':
            savings_goal_forecaster()
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()

