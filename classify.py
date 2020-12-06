import os
import time

import cv2 as cv
import numpy as np

import graph


cur_path = os.path.dirname(os.path.realpath(__file__))
os.chdir(cur_path)

model = './model/model.om'
images_folder = './PetImages'

DVPP_WIDTH = 180
DVPP_HEIGHT = 180



def infer(graph, filepaths):

    accs = []
    times = []
    for fpath in filepaths:
        input_image = cv.imread(fpath)
        if input_image is None:
            continue
        input_image = cv.resize(input_image, (DVPP_WIDTH, DVPP_HEIGHT))
        start = time.time()
        results = graph.Inference(input_image)
        end = time.time()
        accs.append(results)
        times.append(end - start)
        if results is None:
            print("Graph inference failed!")
            continue

    return accs, times


def main():

    try:
        graph = graph.Graph(model)
    except Exception as e:
        print("Except:", e)
        return

    for animal in ['Cat', 'Dog']:
        dir = os.path.join(images_folder, animal)
        fnames = os.listdir(dir)[:1000]
        fpaths = [os.path.join(dir, fname) for fname in fnames]
        accs, times = infer(graph, fpaths)
        mean_acc, sd_acc = np.mean(accs), np.std(accs)
        mean_time, sd_time = np.mean(times), np.std(times)

        print('{}: accuracy (mean, std) = ({:.3f}, {:.3f})'.format(animal, mean_acc, sd_acc))
        print('{}: time (mean, std): ({:.5f}, {:.5f})'.format(animal, mean_time, sd_time))

    graph.Destroy()
    print('------------------- end')


if __name__ == "__main__":
    main()
