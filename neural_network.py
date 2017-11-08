# -*- coding: utf-8 -*-
"""
Fundamentals of Artificial Inteligence (5DV121)
Martin Sjölund
Fredrik Östlund
2017-10-04
"""
import numpy as np

class NeuralNetwork:

    """
    Constructs a new "NeuralNetwork" object.
    :return: returns nothing
    """
    def __init__(self):
        pass

    def imageLoop(self, training, mood, keylist, weights):
        """
        Modifies the weights of the moods by comparing their answer to
        the answer sheet.
        :param training: the training images
        :param mood: the answer sheet for the images
        :param keylist: a list with the image keys randomized
        :param weights: the pixel weights for each of the four mood
        :return: the modified weights
        """
        trainingpart = len(training)/3*2

        for x in range(trainingpart):
            xsad = 0
            xangry = 0
            xhappy = 0
            xmischievous = 0

            """Getting which image we should check from the list of keys"""
            imagestring = keylist[x]
            """Going through each pixel and calculating"""
            for i in range(20):
                for j in range(20):
                    greyscale = self.normalize(training.get(imagestring)[i][j])

                    xsad += self.calculatex(i, j, greyscale, "sad", weights)
                    xangry += self.calculatex(i, j, greyscale, "angry", weights)
                    xhappy += self.calculatex(i, j, greyscale, "happy", weights)
                    xmischievous += self.calculatex(i, j, greyscale,
                                                    "mischievous", weights)


            asad = self.activation(xsad)
            aangry = self.activation(xangry)
            ahappy = self.activation(xhappy)
            amischievous = self.activation(xmischievous)

            """Checking correct mood for the image and assigning a new weight to
             every mood in each pixel"""
            facit = mood.get(keylist[x])

            """Assigning each mood 1 or 0 depending on which mood the 
                                picture represents"""
            ysad = self.calcOutput(facit, "sad")
            yangry = self.calcOutput(facit, "angry")
            yhappy = self.calcOutput(facit, "happy")
            ymischievous = self.calcOutput(facit, "mischievous")

            for a in range(20):
                for b in range(20):
                    """The greyscale for the current pixel"""
                    greyscale = self.normalize(training.get(imagestring)[a][b])



                    """Calculating w for each mood"""
                    wsad = self.computeWDiff(ysad, asad, greyscale)
                    whappy = self.computeWDiff(yhappy, ahappy, greyscale)
                    wangry = self.computeWDiff(yangry, aangry, greyscale)
                    wmischievous = self.computeWDiff(ymischievous, amischievous, greyscale)

                    """Setting new weights to each mood in the pixel"""
                    weights["sad"+str(a)+str(b)] += wsad
                    weights["happy"+str(a)+str(b)] += whappy
                    weights["angry"+str(a)+str(b)] += wangry
                    weights["mischievous"+str(a)+str(b)] += wmischievous
        return weights


    def normalize(self,x):
        """
        Normalizes a value between 0 and 31.
        :param x: value between 0 and 31
        :return: the normalized value
        """
        return float(x)/31

    def calcOutput(self,facit, mood):
        """
        Sets the y-value for each mood, later used for modifying weights.
        :param facit: the answer sheet
        :param mood: "happy", "sad", "angry" or "mischievous"
        :return: 1 if correct, 0 if not
        """
        if facit == '1' and mood == "happy":
            return 1
        elif facit == '2' and mood == "sad":
            return 1
        elif facit == '3' and mood == "mischievous":
            return 1
        elif facit == '4' and mood == "angry":
            return 1
        else:
            return 0

    def computeWDiff(self, y, a, x):
        """
        Calculates and returns the value which to add to the weights
        for modification.
        :param y: 0 or 1
        :param a: activation value
        :param x: greyscale of the pixel
        :return: the value to add to the weight
        """
        e = y - a
        w = 0.05*e*float(x)
        return w

    def calculatex(self, x, y, greyscale, string, weights):
        """
        Computes a value which to add to a sum of x values.
        :param i: x-coordinate of pixel
        :param j: y.coordinate of pixel
        :param greyscale: greyscale of pixel
        :param string: "happy", "sad", "angry" or "mischievous"
        :param weights: the mood-weights
        :return: the mood weight * greyscale
        """
        x = weights.get(string + str(x) + str(y)) * greyscale
        return x

    def activation(self, x):
        """
        Calculates and returns a activation value for x.
        :param x: value to activate
        :return: activated value between 0 and 1
        """
        return 1 / (1 + np.exp(-x))
