import sys
from irt_estimation.IIIPL import IIIPL, MLE_Ability_Estimator
import numpy as np








def run():
    print('-->  RUNNING')
    theta = np.arange(0, 1, 0.01)
    theta = [0.4, 0.6]
    # print(theta)

    # IIIPL(10, .5, .25).plot_model()



    answers = [
        (1, IIIPL(10, .5, .25)),
        (0, IIIPL(4, .4, .25)),
        (1, IIIPL(6, .8, .25))
    ]


    estimate = MLE_Ability_Estimator(answers).estimate()



if __name__ == "__main__":
    run()