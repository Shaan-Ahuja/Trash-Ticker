#!/usr/bin/env python

from dotenv import load_dotenv
import os
import yfinance as yf
import datetime
from twilio.rest import Client

# Load environment variables - create a .env file or hardcore your values here
load_dotenv()
account_sid = os.getenv('ACCOUNT_SID')
auth_token = os.getenv('AUTH_TOKEN')
twilio_number = os.getenv('MY_TWILIO_NUMBER')
target_numbers = [os.getenv('ROOMATE_1_NUMBER'), os.getenv('ROOMATE_2_NUMBER'), os.getenv('ROOMATE_3_NUMBER')]  # Add other numbers similarly

# Roommates and associated ticker symbols - feel free to edit
roommates = {
    'Shaan': 'MSI',
    'Noah': 'TSLA',
    'Adish': 'PYPL'
}

# Function to fetch stock closing price and daily percentage change (from opening to close price)
def stock_info(ticker_symbol):
    stock = yf.Ticker(ticker_symbol)
    hist = stock.history(period="1d")
    closing_price = hist['Close'].iloc[-1]
    percentage_change = ((closing_price - hist['Open'].iloc[-1]) / hist['Open'].iloc[-1]) * 100
    return closing_price, percentage_change

# Fetch day and date
date = datetime.datetime.today().strftime('%m-%d-%Y')
day = datetime.date.today().strftime("%A")

# Create Twilio client
client = Client(account_sid, auth_token)

# Fetch data for each ticker and determine 'winning roomate' based on stock with best daily percentage change
max_change = -float('inf') #defines max_change as smallest possible float number
winning_roommate = ''
stock_messages = []

for roommate, ticker in roommates.items(): # Iterate through roomates
    close_price, change = stock_info(ticker) # Fetch close price and percentage change for each stock
    stock_messages.append(f"{ticker}: {change:.2f}%, ${close_price:.2f}") # Format stock data to be added to text message
    if change > max_change: # Select winning roomate based on ticker change
        max_change = change
        winning_roommate = roommate

# Define message body for text message
message_body = f"{day} {date}\n" # Day, Date
message_body += f"Congrats {winning_roommate}, your stock performed the best...you're on trash duty\n\n" # Congratulate winner
message_body += '\n'.join(stock_messages) # Stock data

# Send a text to each number
for number in target_numbers:
    message = client.messages.create(to=number, from_=twilio_number, body=message_body)
    # Verify that twilio succesfully sent the text
    print(f"Message sent to {number}: {message.sid}")

# Print text body to terminal
print(f"Message body: {message_body}")