import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize_scalar




class MLE_Ability_Estimator:
    def __init__(self, item_response_vector):
        """
            item_response_vector -> a list of touples: (item answer, IIIPL item model)
        """
        self.item_response_vector = item_response_vector

    def likelihood_arr(self, thetas):
        values = []
        for theta in thetas:
            values.append(self.likelihood(theta) * -1.0)
        return values

    def likelihood(self, theta):
        result = 1.0
        
        for item_tuple in self.item_response_vector:
            answer = int(item_tuple[0])
            item = item_tuple[1]
            if answer == 1:
                result = result * item.prob_correct(theta)
            else:
                result = result * (1.0 - item.prob_correct(theta))

        return (result * -0.1)

    def estimate(self):
        return minimize_scalar(self.likelihood, bounds=(0, 1), method='bounded')

    def estimate2(self):
        theta = np.arange(0, 1, 0.01)
        for val in theta:
            likelih = self.likelihood(val)


class AbilityEstimator:
    def __init__(self, item_response_vector, guess=1):
        """
            item_response_vector -> a list of touples: (item answer, IIIPL item model)
        """
        self.item_response_vector = item_response_vector
        self.guess = guess

    def estimate(self, max_iterations=100):
        threshold = 0.1
        current_guess = self.guess
        delta = 1

        count = 0
        while delta > threshold:
            delta = self.find_delta(current_guess)
            print(count, ' --> OLD GUESS / DELTA: ', current_guess, delta)
            current_guess = current_guess + delta
            count = count + 1
            if count > max_iterations:
                break

        return current_guess


    def find_delta(self, current_guess):

        # Calculate numerator
        numerator = 0
        for item_tuple in self.item_response_vector:
            answer = int(item_tuple[0])
            item = item_tuple[1]
            temp = (item.a * -1) * (answer - item.prob_correct(current_guess))
            numerator = numerator + temp

        # Calculate denominator
        denominator = 0
        for item_tuple in self.item_response_vector:
            answer = int(item_tuple[0])
            item = item_tuple[1]
            temp = (item.a * item.a) * (item.prob_correct(current_guess)) * (1 - item.prob_correct(current_guess))
            denominator = denominator + temp

        return (numerator / denominator)







class IIIPL:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def plot_model(self, theta=None):
        if not theta:
            theta = np.arange(0, 1, 0.01)
        prob_correct = self.prob_correct_arr(theta)
        plt.plot(theta, prob_correct)
        plt.xlabel("user ability")
        plt.ylabel("probability of correctly answering")
        _ = plt.title(f"Item Characteristic Curve a={self.a}, b={self.b}, c={self.c}")
        # plt.show()

    def prob_correct_arr(self, theta_arr):
        probs = []
        for theta in theta_arr:
            probs.append(self.prob_correct(theta))
        return probs

    def prob_correct(self, theta):
        # 1. Find logistic exponent (logit)
        logit = self.find_logit(theta)

        # 2. Compute logistic function
        logistic = self.find_logistic(logit)

        # 3. Scale for guessing and return
        return self.scale_guessing(logistic)
    
    def find_logit(self, theta):
        return self.a * (theta - self.b)
    
    def find_logistic(self, logit):
        # return 1.0 / (1 + np.exp(-logit))
        return np.exp(logit) / (1 + np.exp(logit))

    def scale_guessing(self, logistic):
        return self.c + (1 - self.c) * logistic

