# coding=utf-8

import os
import time

import cv2 as cv
import numpy as np

import graph

cur_path = os.path.dirname(os.path.realpath(__file__))
os.chdir(cur_path)
model = './models/catsvsdogs.om'
pathDir = './PetImages'


def main():
    try:
        myGraph = graph.Graph(model)
    except Exception as e:
        print("Except:", e)
        return
    dvppInWidth = 180
    dvppInHeight = 180

    costs = []
    catDir = os.path.join(pathDir, 'Cat')
    catAcc = []
    for allDir in os.listdir(catDir)[:1000]:
        cat = os.path.join(catDir, allDir)
        input_image = cv.imread(cat)
        if input_image is None:
            continue
        input_image = cv.resize(input_image, (dvppInWidth, dvppInHeight))
        start = time.time()
        resultList = myGraph.Inference(input_image)
        catAcc.append(resultList)
        end = time.time()
        costs.append(end - start)
        if resultList is None:
            print("graph inference failed")
            continue
    print('cats: cost time (mean, std): (%.5f, %.5f)' % (np.mean(costs), np.std(costs)))
    print('cats: accuracy (mean) = %.3f' % (np.mean(catAcc)))

    costs = []
    dogDir = os.path.join(pathDir, 'Dog')
    dogAcc = []
    for allDir in os.listdir(dogDir)[:1000]:
        dog = os.path.join(dogDir, allDir)
        input_image = cv.imread(dog)
        if input_image is None:
            continue
        input_image = cv.resize(input_image, (dvppInWidth, dvppInHeight))
        start = time.time()
        resultList = myGraph.Inference(input_image)
        dogAcc.append(resultList)
        end = time.time()
        costs.append(end - start)
        if resultList is None:
            print("graph inference failed")
            continue
    print('dogs: cost time (mean, std): (%.5f, %.5f)' % (np.mean(costs), np.std(costs)))
    print('dogs: accuracy (mean) = %.3f' % (np.mean(dogAcc)))

    myGraph.Destroy()
    print('------------------- end')


if __name__ == "__main__":
    main()
