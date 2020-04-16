# Inspired from
# https://github.com/DistrictDataLabs/blog-files/blob/master/computing-bayesian-average-of-star-ratings/code/stars.py


"""
Ranks given data using the star rating.
"""

from collections import Counter

import matplotlib.pyplot as plt
import pandas as pd


class Ratings(object):
    """
    An analytical wrapper that manages access to the data and wraps various
    statistical functions for easy and quick evaluation.
    """

    def __init__(self, data, prior=None, confidence=None):
        self.data = data
        self.prior = prior
        self.confidence = confidence

    def bayesian_mean(self, arr):
        """
        Computes the Bayesian mean from the prior and confidence.
        """
        if not self.prior or not self.confidence:
            raise TypeError("Bayesian mean must be computed with prior and confidence")

        return (self.confidence * self.prior + arr.sum()) / (self.confidence + arr.count())

    def dirichlet_mean(self, arr, prior=None):
        """
        Computes the Dirichlet mean with a prior.
        """
        if prior is None:
            prior = [2, 2, 2, 2, 2]
        counter = Counter(arr)
        votes = [counter.get(n, 0) for n in range(1, 6)]
        posterior = map(sum, zip(votes, prior))
        N = sum(posterior)
        weights = map(lambda i: (i[0] + 1) * i[1], enumerate(posterior))

        return float(sum(weights)) / N

    @property
    def products(self):
        """
        Returns the data grouped by UniversalProductCode
        """
        return self.data.groupby('UniversalProductCode')

    def get_means(self):
        return self.products['Score'].mean()

    def get_counts(self):
        return self.products['Score'].count()

    def get_bayesian_estimates(self):
        return self.products['Score'].agg(self.bayesian_mean)

    def get_dirichlet_estimates(self):
        return self.products['Score'].agg(self.dirichlet_mean)

    # def top_movies(self, n=10):
    #     grid = pd.DataFrame({
    #         'mean': self.get_means(),
    #         'count': self.get_counts(),
    #         'bayes': self.get_bayesian_estimates(),
    #         'dirichlet': self.get_dirichlet_estimates()
    #     })
    #     print(grid)
    #     return grid.loc[grid['dirichlet'].argsort()[-n:]]

    def get_scores(self):
        return pd.DataFrame({
            'mean': self.get_means(),
            'count': self.get_counts(),
            'bayes': self.get_bayesian_estimates(),
            'dirichlet': self.get_dirichlet_estimates()
        })

    def get_product_score(self, ean13, method='bayes'):
        scores = self.get_scores()
        try:
            return scores[method][ean13]
        except:
            return None

    def plot_mean_frequency(self):
        grid = pd.DataFrame({
            'Mean Rating': self.products['Score'].mean(),
            'Number of Reviewers': self.products['Score'].count()
        })

        grid.plot(x='Number of Reviewers', y='Mean Rating', kind='hexbin',
                  xscale='log', cmap='YlGnBu', gridsize=12, mincnt=1,
                  title="Star Ratings by Simple Mean")
        plt.show()

    def describe(self):
        return self.data.describe()

    def __str__(self):
        return str(self.data.head())
