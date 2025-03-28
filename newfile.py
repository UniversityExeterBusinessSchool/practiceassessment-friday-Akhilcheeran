#######################################################################################################################################################
# 
# Name:
# SID:
# Exam Date:
# Module:
# Github link for this assignment:  
#
# ######################################################################################################################################################
# Instruction 1. Read the questions and instructions carefully and complete scripts.

# Instruction 2. Only ethical and minimal use of AI is allowed. You might use AI to give advice on how to use a tool or programming language.  
#                You must not use AI to create the code. You might make use of AI to aid debugging of the code.  
#                You must indicate clearly how and where you have used AI.

# Instruction 3. Copy the output of the code and insert it as a comment below your code e.g # OUTPUT (23,45)

# Instruction 4. Ensure you provide comments for the code and the output to show contextual understanding.

# Instruction 5. Upon completing this test, commit to Git, copy and paste your code into the word file and upload the saved file to ELE.
#                There is a leeway on when you need to upload to ELE, however, you must commit to Git at 
#                the end of your session.

# ######################################################################################################################################################
# Question 1 - Data Processing and Loops
# You are given a string representing customer reviews. Use a for loop to process the text and count occurrences of specific keywords.
# Your allocated keywords are determined by the first and last digit of your SID.
# Count and store occurrences of each keyword in a dictionary called keyword_counts.
 
customer_reviews = """The product is well-designed and user-friendly. However, I experienced some issues with durability. The customer service was helpful, 
but I expected a faster response. The quality of the materials used is excellent. Overall, the purchase was satisfactory."""

# Keywords dictionary
keywords = {
    0: 'user-friendly',
    1: 'helpful',
    2: 'durability',
    3: 'response',
    4: 'satisfactory',
    5: 'quality',
    6: 'service',
    7: 'issues',
    8: 'purchase',
    9: 'materials'
}

# Write your code to process the text and count keyword occurrences
mylist=[]
keycode=[7,4]
#key code is 
for keycode in keywords :
    word=keywords[keycode]
    startpos = customer_reviews.find(word)
    if startpos != -1 :
        endpos= startpos + len(word)
        keywordcounts=[startpos,endpos]
#result
print (keywordcounts)
#[188,197]
        
    
##########################################################################################################################################################

# Question 2 - Business Metrics
# Scenario - You work in an online retail company as a business analyst. Your manager wants weekly reports on financial performance, including:
# Gross Profit Margin, Inventory Turnover, Customer Retention Rate (CRR), and Break-even Analysis. Implement Python functions 
# that take relevant values as inputs and return the computed metric. Use the first two and last two digits of your ID number as input values.

# Insert first two digits of ID number here:74
# Insert last two digits of ID number here:94

# Write your function for Gross Profit Margin
def gross_profit_margin(grossprofit, revenue):
    return (grossprofit / revenue) * 100 if revenue != 0 else 0
def grossprofitmargin(grossprofit , revenue ) :
       return (grossprofit / revenue) * 100 if revenue != 0 else 0



# Write your function for Inventory Turnover
def inventoryturnover( cogs, avginv) :
    return (cogs/ avginv) if avginv else 0
# Write your function for Customer Retention Rate (CRR)
def crr( customerretained , customerstart ):
    return(customerretained /customerstart)*100 if customerstart else 0
# Write your function for Break-even Analysis
def bea( fixedcosts , cmpu ):
    return(fixedcosts/cmpu)
# Call your functions here
print ('gross profit margin ', grossprofitmargin(74 ,94) )
print ('crr is ' ,crr(74 ,94))
print('bea is ' , bea(74, 94))
print('itr is ' ,inventoryturnover(74 ,94))
'''
outputgross profit margin  78.72340425531915
crr is  78.72340425531915
bea is  0.7872340425531915
itr is  0.7872340425531915
'''
##########################################################################################################################################################

# Question 3 - Forecasting and Regression
# A logistics company has gathered data on delivery costs and shipment volumes. The table below provides different costs and their corresponding shipment volumes.
# Develop a linear regression model and determine:
# 1. The optimal delivery cost that maximizes profit
# 2. The expected shipment volume when the cost is set at £68

'''
Delivery Cost (£)    Shipment Volume (Units)
-------------------------------------------
25                  500
30                  480
35                  450
40                  420
45                  400
50                  370
55                  340
60                  310
65                  290
70                  250
'''
# Write your regression model code here

from sklearn.linear_model import LinearRegression
import numpy as np

# Correcting the input shape
deliverycost = np.array([25, 30, 35, 40, 45, 50, 55, 60, 65, 70]).reshape(-1, 1)
shippingvolume = np.array([500, 480, 450, 420, 400, 370, 340, 310, 290, 250])

# Training the model
model = LinearRegression()
model.fit(deliverycost, shippingvolume)

# Predicting for a new value
prediction = model.predict(np.array([[68]]))  # Needs to be a 2D array

print("Predicted shipping volume for delivery cost 68:", prediction[0])

#outputPrecPredicted shipping volume for delivery cost 68: 267.939393939394
##########################################################################################################################################################

# Question 4 - Debugging and Data Visualization

import rand as random
import matplotlib.pyplt as plt

# Generate 100 random numbers between 1 and student ID number
your_ID=input("Enter your Student ID: ")
max_value = int(your_ID)
random_numbers = [random.randint( 1 ,max_value) in range(100)]

# Plotting the numbers in a histogram
plt.histogram(random_numbers, bin=10, edgecolour='blue', alpha=0.7, colour='red')
plt.title="Histogram of 100 Random Numbers"
plt.xlabel="Value Range"
plt.ylabel="Frequency"
plt.grid("True")
plt.show()

