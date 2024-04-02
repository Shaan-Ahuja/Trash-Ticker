# Trash Ticker
## Decide who takes out the trash based on company stock performance

Too often, the trash can in my apartment remains full until the stench is so unbearable that one of our three roommates cracks and takes it out. So, I created 'Trash Ticker' to determine who will take the trash out based on our employers' stock performance. Every weekday at 2 pm PT, my computer runs this Python script which sends a text to each of us, announcing who's stock had the largest percentage gain from that day's open to close and, subsequently, who is on trash duty for that evening.

What chores seldom get done in your household? You may modify this script in several ways for your specific situarion: 
* Chore/task
* Criteria: best/worst weekly/daily performance
* Specific Stocks: we chose our employers, but you can use any of your favorite public companies
 
### Example Texts
<img src="https://github.com/Shaan-Ahuja/Trash-Ticker/assets/82416480/b762b58e-882f-47f1-99b2-979c7ded784a" width="300">


### Configuration
To get 'Trash Ticker' up and running, follow these configuration steps:

#### 1. Environment Setup
Environment Variables:
The script uses environment variables to manage sensitive information. You will need to create a .env file in the project root directory with the following variables:

```
ACCOUNT_SID: Your Twilio account SID.
AUTH_TOKEN: Your Twilio authentication token.
MY_TWILIO_NUMBER: The Twilio phone number used to send texts.
ROOMATE_1_NUMBER, ROOMATE_2_NUMBER, ROOMATE_3_NUMBER: The phone numbers of the roommates, add as many as needed.
```

Example .env file content:
```
ACCOUNT_SID=your_account_sid_here
AUTH_TOKEN=your_auth_token_here
MY_TWILIO_NUMBER=your_twilio_number_here
ROOMATE_1_NUMBER=+12345678901
ROOMATE_2_NUMBER=+12345678902
ROOMATE_3_NUMBER=+12345678903
```

#### 2. Twilio Account:

Sign up for a Twilio account if you don't have one.
Get your ACCOUNT_SID and AUTH_TOKEN from the Twilio console.
Purchase a Twilio phone number, which will be used as MY_TWILIO_NUMBER.


#### 3. Python Libraries:
Install the necessary Python libraries using the following command:

'''
pip install -r requirements.txt
'''
This will install dotenv, yfinance, and twilio.


#### 4. Script Customization
Roommate and Stock Tickers:
Customize the roommates dictionary in the script to include the names of your roommates and their associated stock tickers.

Example:
```
roommates = {
    'Alice': 'AAPL',
    'Bob': 'GOOGL',
    'Charlie': 'AMZN'
}
```
Choose the stocks based on your specific criteria, like your employers' stocks or any other public company.

#### 5. Scheduling the Script:
To run this script every weekday at a time after trading hours, consider using a task scheduler.

* For Linux/MacOS, you can use cron.
* For Windows, you can use Task Scheduler.
  
#### 6. Testing:
Test the script to ensure it's sending messages correctly. You might want to temporarily set the target numbers to your own to avoid sending test messages to your roommates.

