#!/usr/bin/env python3
# insertionsort.py
# Author : Shipra
import logging
import sys

def userInput():
    '''
    Taking numbers as user input and
    creating a  list of numbers
    '''
    initialListOfNumbers = []
    userInputNumber = 0
    while userInputNumber != '':
        userInputNumber = input("Enter the value to create a list: ")
        initialListOfNumbers.append(userInputNumber)

    initialListOfNumbers.pop()
    initialListOfNumbers = list(map(int, initialListOfNumbers))
    return initialListOfNumbers


def InsertionSortNumbers(initialListOfNumbers):
    '''
    Sorting a list of numbers using
    insertion sort algorithm
    '''
    for i in range(len(initialListOfNumbers)-1):
        for j in range(len(initialListOfNumbers)-1):
            if initialListOfNumbers[j] > initialListOfNumbers[j+1]:
                if initialListOfNumbers[j-1] > initialListOfNumbers[j+1]:
                    initialListOfNumbers[j-1] , initialListOfNumbers[j+1] = \
                    initialListOfNumbers[j+1] , initialListOfNumbers[j-1]
                else:
                    initialListOfNumbers[j],initialListOfNumbers[j+1] = \
                    initialListOfNumbers[j+1],initialListOfNumbers[j]
            else:
                continue
            logging.debug(initialListOfNumbers)

    print("The final sorted list:", initialListOfNumbers)


logging.basicConfig(level=logging.DEBUG)

for number in range(1):
    initialListOfNumbers = userInput()
    print("Original list of numbers" + str(number) + " =", initialListOfNumbers)
    logging.debug(initialListOfNumbers)
    InsertionSortNumbers(initialListOfNumbers)
