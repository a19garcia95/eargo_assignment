
def max_gain(stock_price):
    mx = 0  # variable to compute max gain
    mn = 999999999  # variable to compute minimum stock price till now
    buy_day = 0  # variable to store buy day
    sell_day = 0  # variable to store sell day
    day = 1  # variable to iterate days
    for i in stock_price:  # iterating through each day stock price
        if(i < mn):  # checking if current day stock price is less than the mn
            mn = i  # updating mn
            buy_day = day  # updating buy_day
        if(i-mn > mx):  # checking if I sell at current day, the benefit is greater than or not
            mx = i-mn  # updating max gain
            sell_day = day  # updating sell_day
        day += 1  # incrementing day
    return (buy_day, sell_day, mx)  # returning buy day, sell day and max gain


'''

Approach: The function will take the stock price list as parameter. 
I have iterated through each day stock price and store the minimum stock price in mn variable and updating the buy day. 
Then I have checked if I sell the stock at current day how much benefit I am getting.
If it is bigger than previous then I am updating the mx variable and sell day. 

Complexity: The time complexity of the program is O(n) where n is the number days.

'''
