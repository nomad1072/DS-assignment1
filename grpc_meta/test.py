import pickle

with open('same_machine.pickle', 'rb') as handle:
    data = pickle.load(handle)

    print('Data: ', data)