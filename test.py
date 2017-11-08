# -*- coding: utf-8 -*-
"""
Fundamentals of Artificial Inteligence (5DV121)
Martin Sjölund
Fredrik Östlund
2017-10-04
"""
import numpy as np

class Test:
    """
      Constructs a new "NeuralNetwork" object.
      :return: returns nothing
      """

    def __init__(self):
        pass

    def testtraining(self, facit, images, weights, keylist):
        """
        Test how good the face recognition is and returns the percentage
        of correct answers.
        :param facit: the answer sheet
        :param images: the training images
        :param weights: the mood weights
        :param keylist: a list of shuffled dict keys
        :return: percentage of correct answers
        """
        correctAnswers = 0
        noofimages = len(images)
        testpart = noofimages/3*1

        for x in range(testpart):
            sadsum = 0
            happysum = 0
            angrysum = 0
            mischievoussum = 0
            string = keylist[noofimages-testpart+x]

            for y in range(20):
                for z in range(20):
                    greyscale = self.normalize(images.get(string)[y][z])

                    sadsum += weights.get("sad"+str(y)+str(z)) * greyscale
                    happysum += weights.get("happy"+str(y)+str(z)) * greyscale
                    angrysum += weights.get("angry"+str(y)+str(z)) * greyscale
                    mischievoussum += weights.get("mischievous"+str(y)+str(z)) * greyscale

            sadvote = self.activation(sadsum)
            happyvote = self.activation(happysum)
            angryvote = self.activation(angrysum)
            mischievousvote = self.activation(mischievoussum)

            answer = self.vote(happyvote, sadvote, mischievousvote, angryvote)
            facitanswer = facit.get(string)

            if int(facitanswer) == answer:
                correctAnswers += 1

        return float(correctAnswers)/float(testpart)*100


    def realtest(self, images, weights):
        """
        Tests the program for real, the output is a text file with the answers
        of the program for each image.
        :param images: test images
        :param weights: the mood weights
        :return: returns nothing
        """
        text_file = open('result.txt', 'w')
        text_file.write("#Result of image recognition test\n")
        text_file.write("#Authors: Martin Sjölund (id15msd), "
                        "Fredrik Östlund (id15fod)\n")

        for x in range(len(images)):
            sadsum = 0
            happysum = 0
            angrysum = 0
            mischievoussum = 0
            key = "Image" + str(x+1)

            for y in range(20):
                for z in range(20):
                    greyscale = self.normalize(images.get(key)[y][z])

                    sadsum += weights.get("sad"+str(y)+str(z)) * greyscale
                    happysum += weights.get("happy"+str(y)+str(z)) * greyscale
                    angrysum += weights.get("angry"+str(y)+str(z)) * greyscale
                    mischievoussum += weights.get("mischievous"+str(y)+str(z)) * greyscale

            sadvote = self.activation(sadsum)
            happyvote = self.activation(happysum)
            angryvote = self.activation(angrysum)
            mischievousvote = self.activation(mischievoussum)

            answer = self.vote(happyvote, sadvote, mischievousvote, angryvote)

            text_file.write(key + " " + str(answer) + "\n")
            print key + " " + str(answer)

        text_file.close()


    def activation(self, sum):
        """
        Calculates and returns a activation value for x.
        :param x: value to activate
        :return: activated value between 0 and
        """
        return (1 / (1 + np.exp(-sum)))

    def normalize(self, x):
        """
        Normalizes a value between 0 and 31.
        :param x: value between 0 and 31
        :return: the normalized value
        """
        return float(x)/31

    def vote(self, a, b, c, d):
        """
        Finds the largest of the sums and returns the corresponding vote.
        :param a: sum of the weights for "happy"
        :param b: sum of the weights for "sad"
        :param c: sum of the weights for "mischievous"
        :param d: sum of the weights for "angry"
        :return: the vote for the image, a value 1-4
        """
        vote = 1

        if b > a:
            vote = 2
        if c > b and c > a:
            vote = 3
        if d > c and d > b and d > a:
            vote = 4

        return vote