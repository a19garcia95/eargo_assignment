
def change(n):
    coin = [25, 10, 5, 1]  # list of coins
    coin_name = ['Quarters', 'Dimes', 'Nickels', 'Pennies']  # coin name list
    ret = []  # empty list to store the answer

    for i in range(4):  # iterating through all the coin
        x = n//coin[i]  # using x numbers coin[i]
        # calculating the rest of n after using x number of coin[x]
        n = n % coin[i]
        # appending coin name and number of coins needed in the list
        ret.append((coin_name[i], x))
    return ret  # returning the list


'''

Approach: The function will take the number as parameter for which I have to calculate the change. 
It will go through each coin and calculate the number of coins of this type needed. At last it will return the list.

Complexity: The time complexity of the program is O(n) where n is the number of unique coins.

'''
