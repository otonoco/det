
import os
import sys
import matplotlib.pyplot as plt
plt.rcParams['figure.figsize'] = [14, 8]

sys.path.append('../..')
from pytracking.analysis.plot_results import plot_results, print_results, print_per_sequence_results
from pytracking.evaluation import Tracker, get_dataset, trackerlist
from pytracking.analysis import playback_results

def play():
    trackers = []
    trackers.extend(trackerlist('atom', 'DeT_ATOM_Max', range(0,5), 'ATOM'))
    trackers.extend(trackerlist('dimp', 'DeT_DiMP50_Max', range(0,5), 'DiMP50'))
    trackers.extend(trackerlist('tomp', 'DeT_ToMP50_Max', range(0,5), 'ToMP50'))

    # trackers.extend(trackerlist('dimp', 'dimp50', range(0,5), 'DiMP50'))
    # trackers.extend(trackerlist('dimp', 'prdimp18', range(0,5), 'PrDiMP18'))
    # trackers.extend(trackerlist('dimp', 'prdimp50', range(0,5), 'PrDiMP50'))

    dataset = get_dataset("rgbcolormap", 'depthtrack')

    playback_results.playback_results(trackers, dataset[0])


def main():
    play()

if __name__ == "__main__":
    main()