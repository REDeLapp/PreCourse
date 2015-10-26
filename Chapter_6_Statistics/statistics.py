import pickle
import numpy as np
import scipy.stats as scs

# Don't change this. This fixes the randomness in sampling
np.random.seed(seed=1234)


# This loads in the list of numbers you are going to deal with
def load_pickle(file_name):
    """INPUT:
    - file_name(STR) [The name of the file]

    OUTPUT:
    - population(NUMPY ARRAY) [A array of numbers for the exercise]
    """
    return pickle.load(open(file_name))


def draw_sample(population, n):
    """INPUT:
    - population(NUMPY ARRAY) [The array containing all the numbers]
    - n(INT) [The number of sample you wanna draw]

    OUTPUT:
    - sample(NUMPY ARRAY) [A array that contains a subset of the population]

    Hint: Use np.random.choice(). Google it. Google is your best friend
    """
    return np.random.choice(population,n)
    pass


def get_mean(lst):
    """INPUT:
    - lst(NUMPY ARRAY) [The array of numbers where we find the mean of]

    OUTPUT:
    - mean_value(FLOAT)

    Hint: Don't use np.mean().
    Then use np.mean(arr) to see if you got the same value
    """
    return float(np.sum(lst))/float(len(lst))
    pass


def get_variance(lst, sample=True):
    """INPUT:
    - lst(NUMPY ARRAY) [Either the sample or the population]
    - sample(BOOL) [True if sample variance, False if population variance]

    OUTPUT:
    - lst_variance(FLOAT) [Sample or population variance depending]
    """
    if sample == False:
        return np.sum(np.power(np.add(lst,-1.0*get_mean(lst)),2))/float(len(lst))
    else:
        return np.sum(np.power(np.add(lst,-1.0*get_mean(lst)),2))/float(len(lst)-1)
    pass


def get_sem(sample):
    """INPUT:
    - sample(NUMPY ARRAY)

    OUTPUT:
    - sem(FLOAT) [Standard Error Mean]
    """
    return np.sqrt(get_variance(sample))/np.sqrt(len(sample))
    pass


def get_confidence_interval(sample, confidence=.95):
    """INPUT:
    - sample(NUMPY ARRAY)
    - confidence(FLOAT) [The confidence of the ci from 0 to 1, usually .95]

    OUTPUT:
    - (tuple) [mean, mean - half_rng, mean + half_rng]
    """
    mean = get_mean(sample)

    half_rng = scs.t.ppf(confidence/2,sample) * get_sem(sample)
    return half_rng
    #return [mean,mean-half_rng,mean+half_rng]
    pass


def get_interquartile_range(population):
    """INPUT:
    - population(NUMPY ARRAY)

    OUTPUT:
    - iqr(FLOAT) [Interquartile range]
    """
    pass


def get_outlier(population):
    """INPUT:
    - population(NUMPY ARRAY)

    OUTPUT:
    - outliers(NUMPY ARRAY) [List of outliers]
    """
    pass


if __name__ == '__main__':
    population = load_pickle('population.pkl')
    print 'First 5 element of the population: ', population[:5]
    sample_100 = draw_sample(population, 100)
    sample_1000 = draw_sample(population, 1000)
    population_mean = get_mean(population)
    sample_100_mean = get_mean(sample)
    sample_1000_mean = get_mean(sample)
    print 'Population mean: ', population_mean
    print 'Sample 100 mean: ', sample_100_mean
    print 'Sample 1000 mean: ', sample_1000_mean
    population_var = get_variance(population)
    sample_100_var = get_variance(sample_100)
    sample_1000_var = get_variance(sample_1000)
    print 'Population variance: ', population_variance
    print 'Sample 100 variance: ', sample_100_variance
    print 'Sample 1000 variance: ', sample_1000_variance
    print 'per difference between sample of 1000 / 100: ', (sample_1000_variance - sample_100_variance)/sample_100_variance
    population_sem = get_sem(population)
    sample_100_sem = get_sem(sample_100)
    sample_1000_sem = get_sem(sample_1000)
    print 'Population sem: ', population_sem
    print 'Sample 100 sem: ', sample_100_sem
    print 'Sample 1000 sem: ', sample_1000_sem
    print 'per difference between sample of 1000 / 100: ', (sample_1000_sem - sample_100_sem)/sample_100_sem
    # how precisely we know the mean

