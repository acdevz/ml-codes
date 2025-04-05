import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import PolynomialFeatures

def poly_data(x, y):
    # polynomial data
    x = x[:, np.newaxis]  # Reshape x to be a 2D array [[1], [2], ...] from [1, 2, ...]
    y = y[:, np.newaxis]  # Reshape y to be a 2D array
    poly = PolynomialFeatures(degree=1)
    x_poly = poly.fit_transform(x)
    return x_poly, y

def poly_linear_regression(data, degree=1):
    x_poly, y = data
    model = LinearRegression()
    model.fit(x_poly, y)
    y_poly_pred = model.predict(x_poly)

    mse = mean_squared_error(y, y_poly_pred)
    r2 = r2_score(y, y_poly_pred)
    model.degree = degree
    model.mse = mse
    model.r2 = r2
    return model

def regression_plot(data, model, axis, color):
    x_poly, y = data
    axis.plot(x_poly[:, 1], model.predict(x_poly), color=color[model.degree], label="Model Degree: {}, MSE: {:.2f}, R2: {:.2f}".format(model.degree, model.mse, model.r2))
    axis.legend()


if(__name__ == "__main__"):
    # Generate synthetic data
    np.random.seed(0)
    x = np.arange(-5, 5, 0.2) + np.random.normal(0, 1, 50)
    y = -1 * (x**4) - 2 * (x**3) + 13 * (x**2) + 14 * (x) - 24 + 10 * np.random.normal(-1, 1, 50)

    _, axis = plt.subplots()
    color = ["blue", "green", "red", "orange"]
    axis.grid();
    axis.set_title("Polynomial Regression")
    axis.set_xlabel("x")
    axis.set_ylabel("y")
    axis.scatter(x[:, np.newaxis], y[:, np.newaxis], color=color[0], label="Data points")

    for degree in range(1, 5):
        data = poly_data(x, y)
        model = poly_linear_regression(data, degree=degree - 1)
        regression_plot(data, model, axis, color)