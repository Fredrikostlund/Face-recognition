# -*- coding: utf-8 -*-
"""
Fundamentals of Artificial Inteligence (5DV121)
Martin Sjölund
Fredrik Östlund
2017-10-04
"""
from test import Test
from image_read import ImageRead
from neural_network import NeuralNetwork
import random
import sys

def createRandomListFromDict(dict):
    """
    Creates and returns a list of a shuffled dict keys.
    :param dict: dict to shuffle
    :return: list of shuffled dict keys
    """
    templist = dict.keys()
    random.shuffle(templist)
    return templist


def randomizeWeights():
    """
    Creates a dict with 400 random weight values.
    :return: dict with weights
    """
    dict = {}
    for x in range(20):
        for y in range(20):
            dict['sad' + str(x) + str(y)] = random.uniform(0.4, 0.5)
            dict['happy' + str(x) + str(y)] = random.uniform(0.4, 0.5)
            dict['angry' + str(x) + str(y)] = random.uniform(0.4, 0.5)
            dict['mischievous' + str(x) + str(y)] = random.uniform(0.4, 0.5)
    return dict

def main():
    """
    Read files from system input and returns them.
    :return: three text files, training images, answer sheet and
    test images
    """
    if (len(sys.argv) > 1):
        file_training = sys.argv[1]
        file_facit = sys.argv[2]
        file_test = sys.argv[3]
    else:
        file_training = "training.txt"
        file_facit = "training-facit.txt"
        file_test = "test-images.txt"

    return file_training, file_facit, file_test

if __name__ == '__main__':
    network = NeuralNetwork()
    test = Test()

    training_images, training_facit, test_images = main()

    imageRead = ImageRead()
    training = imageRead.readImage(training_images)

    facit = imageRead.readfacit(training_facit)
    weights = randomizeWeights()

    running = True
    print "///\nTraining perceptrons until desired performance criteria is " \
          "met,.\n///\n"
    while(running):
        keylist = createRandomListFromDict(training)

        weights = network.imageLoop(training, facit, keylist, weights)
        correctAnswers = test.testtraining(facit, training, weights, keylist)

        print str(correctAnswers) + "% correctness"
        if correctAnswers > 75.0:
            print "\n///\nReady for a real test, let's go!\n///\n"
            running = False

    if test_images != 0:
        test_dict = imageRead.readImage(test_images)
        test.realtest(test_dict, weights)

    print "\n///\nResults are done and written to result.txt\n///"
