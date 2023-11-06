

import random
import argparse
import codecs
import os
import numpy

# observations
class Observation:
    def __init__(self, stateseq, outputseq):
        self.stateseq  = stateseq   # sequence of states
        self.outputseq = outputseq  # sequence of outputs
    def __str__(self):
        return ' '.join(self.stateseq)+'\n'+' '.join(self.outputseq)+'\n'
    def __repr__(self):
        return self.__str__()
    def __len__(self):
        return len(self.outputseq)

# hmm model
class HMM:
    def __init__(self, transitions={}, emissions={}):
        """creates a model from transition and emission probabilities"""
        ## Both of these are dictionaries of dictionaries. e.g. :
        # {'#': {'C': 0.814506898514, 'V': 0.185493101486},
        #  'C': {'C': 0.625840873591, 'V': 0.374159126409},
        #  'V': {'C': 0.603126993184, 'V': 0.396873006816}}

        self.transitions = transitions
        self.emissions = emissions

    ## part 1 - you do this.
    def load(self, basename):
        """reads HMM structure from transition (basename.trans),
        and emission (basename.emit) files,
        as well as the probabilities."""
        transition_file = basename + ".trans"
        emission_file = basename + ".emit"
        with open(transition_file, 'r') as f:
            for line in f:
                line = line.strip()
                if line:
                    line = line.split()
                    # add the transition probability to the dictionary
                    if line[0] not in self.transitions:
                        self.transitions[line[0]] = {}
                    self.transitions[line[0]][line[1]] = float(line[2])
        with open(emission_file, 'r') as f:
            for line in f:
                line = line.strip()
                if line:
                    line = line.split()
                    # add the emission probability to the dictionary
                    if line[0] not in self.emissions:
                        self.emissions[line[0]] = {}
                    self.emissions[line[0]][line[1]] = float(line[2])



   ## you do this.
    def generate(self, n):
        """return an n-length observation by randomly sampling from this HMM."""



    ## you do this: Implement the Viterbi alborithm. Given an Observation (a list of outputs or emissions)
    ## determine the most likely sequence of states.

    def viterbi(self, observation):
        """given an observation,
        find and return the state sequence that generated
        the output sequence, using the Viterbi algorithm.
        """

if __name__ == '__main__':
    model = HMM()
    model.load('two_english')
    print("Loaded model: transitions")
    print(model.transitions)
    print("Loaded model: emissions")
    print(model.emissions)




