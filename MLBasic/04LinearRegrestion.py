import pandas as pd
import matplotlib.pyplot as plt

dataframe = pd.read_csv('Advertising.csv')
X = dataframe.values[: , 2]  # lấy tất cả các dòng của cột thứ 2 (Radio)
y = dataframe.values[: , 4]  # Lấy (sales)
# plt.scatter(X,y,marker="o")     vẽ lên cho zui

# Sales = Weight * Radio + Bias

def predict_sales(radio, weight, bias):
    return weight*radio + bias

def cost_function(radio, sales, weight, bias):
    companies = len(radio)
    total_error = 0.0
    for i in range(companies):
        total_error += (sales[i] - (weight*radio[i] + bias))**2
    return total_error / companies

def update_weights(radio, sales, weight, bias, learning_rate):
    weight_deriv = 0
    bias_deriv = 0
    companies = len(radio)

    for i in range(companies):
        # Calculate partial derivatives
        # -2x(y - (mx + b))
        weight_deriv += -2*radio[i] * (sales[i] - (weight*radio[i] + bias))

        # -2(y - (mx + b))
        bias_deriv += -2*(sales[i] - (weight*radio[i] + bias))

    # We subtract because the derivatives point in direction of steepest ascent
    weight -= (weight_deriv / companies) * learning_rate
    bias -= (bias_deriv / companies) * learning_rate

    return weight, bias

def train(radio, sales, weight, bias, learning_rate, iters):
    cost_history = []

    for i in range(iters):
        weight,bias = update_weights(radio, sales, weight, bias, learning_rate)

        #Calculate cost for auditing purposes
        cost = cost_function(radio, sales, weight, bias)
        cost_history.append(cost)

    return weight, bias, cost_history

weight, bias, cost = train(X,y, 0.03, 0.0014, 0.001, 100)
print("ket qua la :")
print(weight)
print(bias)
print(cost)
print("gia tri du doan : ")
print(predict_sales(19, weight, bias))

solanlap = [i for i in range(100)]
print(solanlap)
plt.plot(solanlap , cost)
plt.show()