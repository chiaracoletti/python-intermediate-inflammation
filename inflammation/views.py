"""Module containing code for plotting inflammation data."""

from matplotlib import pyplot as plt
import numpy as np


def visualize(data_dict):
    """Display plots of basic statistical properties of the inflammation data.

    :param data_dict: Dictionary of name -> data to plot
    """
    # TODO(lesson-design) Extend to allow saving figure to file

    num_plots = len(data_dict)
    fig = plt.figure(figsize=((3 * num_plots) + 1, 3.0))

    for i, (name, data) in enumerate(data_dict.items()):
        axes = fig.add_subplot(1, num_plots, i + 1)

        axes.set_ylabel(name)
        axes.plot(data)

    fig.tight_layout()

    plt.show()


def textual_view(data_dict):
    """Display textual representation of statistics thorugh an optional command line argument.

    :param data_dict: Dictionary of name -> data to summarize
    """
    for i, (name, data) in enumerate(data_dict.items()):
        if name == 'average':
            print('The overall', name, ' is ', np.mean(data), '.\n')
        if name == 'min':
            print('The overall', name, ' is ', np.min(data), '.\n')
        if name == 'max':
            print('The overall', name, ' is ', np.max(data), '.\n')