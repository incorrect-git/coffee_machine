class Puppy:
    n_puppies = 0  # number of created puppies
    LIMIT = 10
    # define __new__
    def __new__(cls):
        if cls.n_puppies < cls.LIMIT:
            cls.n_puppies += 1
