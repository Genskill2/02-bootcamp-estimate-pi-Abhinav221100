import math
import unittest
from random import random as r

def wallis(num):
    pi = 1
    for i in range(num):
        j=i+1 #iteration starts from 1
        eq = (4*(j**2))/((4*(j**2))-1) #value that is multiplied every iteration(the wallis formula)
        pi = pi*eq # the value of pi/2
    pi = 2*pi
    return pi

def monte_carlo(num):
    val1 = 0 #area of circle(probabilistic)
    val2 = 0 #area of square(probabilistic)
    for i in range(num):
        x = r()
        y = r()
        if(math.sqrt((x**2) + (y**2)))<=1:  #lies within circle
            val1 +=1
        val2 +=1
        ratio = val1/val2
        pi = 4*(ratio) #monte carlo formula
    return pi

class TestWallis(unittest.TestCase):
    def test_low_iters(self):
        for i in range(0, 5):
            pi = wallis(i)
            self.assertTrue(abs(pi - math.pi) > 0.15, msg=f"Estimate with just {i} iterations is {pi} which is too accurate.\n")
            
    def test_high_iters(self):
        for i in range(500, 600):
            pi = wallis(i)
            self.assertTrue(abs(pi - math.pi) < 0.01, msg=f"Estimate with even {i} iterations is {pi} which is not accurate enough.\n")


class TestMC(unittest.TestCase):
    def test_randomness(self):
        pi0 = monte_carlo(15000)
        pi1 = monte_carlo(15000)
        
        self.assertNotEqual(pi0, pi1, "Two different estimates for PI are exactly the same. This is almost impossible.")

        self.assertFalse(abs(pi0 - pi1) > 0.05, "Two different estimates of PI are too different. This should not happen")

    def test_accuracy(self):
        for i in range(500, 600):
            pi = monte_carlo(i)
            self.assertTrue(abs(pi - math.pi) < 0.4, msg=f"Estimate with even {i} iterations is {pi} which is not accurate enough.\n")
        
    
if __name__ == "__main__":
    unittest.main()
