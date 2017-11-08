# -*- coding: utf-8 -*-
"""
Fundamentals of Artificial Inteligence (5DV121)
Martin Sjölund
Fredrik Östlund
2017-10-04
"""
class ImageRead:

    """
    Constructs a new "ImageRead" object.
    :return: returns nothing
    """
    def __init__(self):
        pass

    def readImage(self, file):
        """
        Opens a textfile and reads the lines to an array.
        :param file: The text file to read from
        :return: an array for the Neural Network to train from
        """
        """Table to have the name as key, and the array as value"""
        imageDict = {}
        string = "empty"
        valueArray = []

        """opens file to read"""
        image_file = open(file, 'r')

        try:
            i = 0
            for line in image_file:

                """saves the image name and the 20 lines of image values"""
                if line[0] == "#" or not line.strip():
                    continue
                else:
                    if i == 0:
                        string = line
                        string = string.rstrip('\n')
                        i += 1
                    elif i == 20:
                        valueArray.append(line.split())
                        imageDict[string] = valueArray
                        valueArray = []
                        i = 0
                    else:
                        valueArray.append(line.split())
                        i += 1

        except StopIteration as ex:
            pass

        image_file.close()
        return imageDict

    def readfacit(self, file):
        """
        Translates a text file with a answer sheet to a dict with the same
        values.
        :param file: the text file with the answer sheet
        :return: a dict with the aswer sheet
        """

        facit = {}
        facit_file = open(file, 'r')

        try:
            for line in facit_file:
                if line[0] == "#" or not line.strip():
                    continue
                else:
                    linestring = line.split()
                    facit[linestring[0]] = linestring[1].rstrip('\n')

        except StopIteration as ex:
            pass

        facit_file.close()
        return facit