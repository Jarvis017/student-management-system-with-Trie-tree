from random import randint


class Hash:
    def __init__(self, n):

        # initialize hash
        self.n = n
        self.table = [None for i in range(n)]

    def hash(self, key, obj):
        while True:

            # make random number
            rand = randint(1000, 2500)

            # checking for collision
            if self.table[(rand * key) % self.n] is None:

                # add to table
                self.table[(rand + key) % self.n] = obj
                tmp = (rand + key) % self.n
                break

        # return key
        return tmp

