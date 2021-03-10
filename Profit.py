
"""
Excersise 5 - Profit
Description: You work for a manufacturer, and have been asked to calculate the total
             profit made on the sales of a product. You are given a dictionary containing
             thecost price per unit(in dollars),sell price per unit(in dollars),
             and thestarting inventory. Return the totalprofitmade, rounded to the nearest dollar.

Name: Fabián Munoz Aguirre
Student ID: A00354910
"""

profitDictionary = {
    "cost_price" : 0.0,
    "sell_price" : 0.0,
    "inventory" : 0
    }

def CalculateProfit(dictionary):
    
    profit = 0.0
    profit = (dictionary["sell_price"] - dictionary["cost_price"]) * dictionary["inventory"]
    return profit


profitDictionary["cost_price"] = 1
profitDictionary["sell_price"] = 1.5
profitDictionary["inventory"] = 100
print(CalculateProfit(profitDictionary))

profitDictionary["cost_price"] = 9
profitDictionary["sell_price"] = 12
profitDictionary["inventory"] = 10
print(CalculateProfit(profitDictionary))

profitDictionary["cost_price"] = 16
profitDictionary["sell_price"] = 17
profitDictionary["inventory"] = 2012
print(CalculateProfit(profitDictionary))

profitDictionary["cost_price"] = 3
profitDictionary["sell_price"] = 8
profitDictionary["inventory"] = 50
print(CalculateProfit(profitDictionary))

profitDictionary["cost_price"] = 8
profitDictionary["sell_price"] = 8.22
profitDictionary["inventory"] = 100
print(CalculateProfit(profitDictionary))

profitDictionary["cost_price"] = 0.9
profitDictionary["sell_price"] = 1.9
profitDictionary["inventory"] = 1000
print(CalculateProfit(profitDictionary))

profitDictionary["cost_price"] = 3.25
profitDictionary["sell_price"] = 8.5
profitDictionary["inventory"] = 100
print(CalculateProfit(profitDictionary))

profitDictionary["cost_price"] = 12
profitDictionary["sell_price"] = 34
profitDictionary["inventory"] = 56
print(CalculateProfit(profitDictionary))

profitDictionary["cost_price"] = 78
profitDictionary["sell_price"] = 98
profitDictionary["inventory"] = 159
print(CalculateProfit(profitDictionary))

profitDictionary["cost_price"] = 5
profitDictionary["sell_price"] = 6
profitDictionary["inventory"] = 90
print(CalculateProfit(profitDictionary))