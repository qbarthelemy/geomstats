"""
Plot a geodesic of SE(3) equipped
with its left-invariant canonical METRIC.
"""

import matplotlib.pyplot as plt
import numpy as np
import os
# Examples with visualizations are only implemented with numpy
os.environ['GEOMSTATS_BACKEND'] = 'numpy'  # NOQA

import geomstats.visualization as visualization

from geomstats.special_euclidean_group import SpecialEuclideanGroup

SE3_GROUP = SpecialEuclideanGroup(n=3)
METRIC = SE3_GROUP.left_canonical_metric


def main():
    initial_point = SE3_GROUP.identity
    initial_tangent_vec = [1.8, 0.2, 0.3, 3., 3., 1.]
    geodesic = METRIC.geodesic(initial_point=initial_point,
                               initial_tangent_vec=initial_tangent_vec)

    n_steps = 40
    t = np.linspace(-3, 3, n_steps)

    points = geodesic(t)

    visualization.plot(points, space='SE3_GROUP')
    plt.show()


if __name__ == "__main__":
    main()
