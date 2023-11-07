

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
        """ Generate an n-length observation sequence. """
        # Start in the initial state
        cur_state = '#'
        states = []
        emissions = []

        for _ in range(n):
            # next_state: based on the transition probabilities of the current state
            next_state = numpy.random.choice( list(self.transitions[cur_state].keys()), p=list(self.transitions[cur_state].values()) )
            # emission: based on the emission probabilities of the chosen state
            emission = numpy.random.choice( list(self.emissions[next_state].keys()), p=list(self.emissions[next_state].values()) )
            states.append(next_state)
            emissions.append(emission)
            cur_state = next_state
        return Observation(states, emissions)

    def forward(self, observation):
        """
        Set up the initial matrix M, with P=1.0 for the ‘#’ state.
        For each state on day 1: P(state | e0) = 𝛼P(e0 | state) P(state | #)

        for i = 2 to n  :
        foreach state s:
        sum = 0
            for s2 in states :
                sum += M[s2, i-1]*T[s2,s]*E[O[i],s2]
                M[s2,i] = sum

        :param observation:
        :return:
        """
        states = list(self.transitions.keys())
        states.remove('#')
        observation = observation.split()
        observation = observation[:-1]

        T = len(observation)  # Length of the observation sequence
        N = len(states)  # Number of states

        # Initialize forward probabilities matrix M
        M = [[0 for _ in range(N)] for _ in range(T)]

        # Initialization step for t = 1
        for s in range(N):
            state = states[s]
            M[0][s] = self.transitions['#'][state] * self.emissions[state].get(observation[0], 0)

        # Iteration step for t = 2 to T
        for t in range(1, T):
            for s in range(N):
                sum_val = 0
                for s2 in range(N):
                    sum_val += M[t - 1][s2] * self.transitions[states[s2]].get(states[s], 0) * self.emissions[states[s]].get(observation[t], 0)
                M[t][s] = sum_val
        maxv = max(M[T - 1])
        inx = M[T - 1].index(maxv)
        return states[inx]



    ## you do this: Implement the Viterbi alborithm. Given an Observation (a list of outputs or emissions)
    ## determine the most likely sequence of states.

    def viterbi(self, observation):
        """given an observation,
        find and return the state sequence that generated
        the output sequence, using the Viterbi algorithm.
        """
        """
        M[t,s] = 0
        Backpointers[t,s] = 0 # this will keep our path to the best previous state.
        ## set up the initial probabilities from the start state (states[0] to observation 1.
        ## T is the transition probabilities, E is the emission probabilities, O is the vector of observations.
        for s in state_values : 
          M[1,s] = T[states[0], s] * E[s, O[1]]  ## the probability of that state * the probability of that state given observation 1.
        ### 
        for o in observations : ## for each time step
           for s in state_values : ## for each possible hidden state
             val = max[ M[state2, o-1] * T[state2, s]  *p(s, o) for state2 in state_values ]. 
                ## look at the likelihood of the sequence so far, 
                ## times T, times the likelihood of that state, given the observation.
             M[s,o] = val
             Backpointers[s,o] = index(val)
        list = []
        Best = max(M[t,:]).  #find the most likely state for time t
        for o in observations.reverse : # work backwards through time to the initial state
           list.push(best) 
           best = backpointers[best, o] ## from this best state, what was the most likely state?      
        return list
        """
        states = list(self.transitions.keys())
        states.remove('#')
        observations = observation.split()
        T = len(observations)  # Number of time steps
        N = len(states)  # Number of states

        # Initialize the matrices
        M = [[0 for _ in range(N)] for _ in range(T)]
        Backpointers = [[0 for _ in range(N)] for _ in range(T)]

        # Initialization step
        for s, state in enumerate(states):
            M[0][s] = self.transitions['#'].get(state, 0) * self.emissions[state].get(observations[0], 0)

        # Iteration step
        for t in range(1, T):
            for s, state in enumerate(states):
                vals = []
                for s2 in range(N):
                    cur = M[t - 1][s2] * self.transitions[states[s2]].get(state, 0) * self.emissions[state].get(observations[t], 0)
                    vals.append(cur)
                max_prob = max(vals)

                M[t][s] = max_prob
                Backpointers[t][s] = vals.index(max_prob)

        # Termination step to find the last state
        best_last_state = max(range(N), key=lambda s: M[T-1][s])
        best_path_prob = M[T-1][best_last_state]

        # Backtracking to find the best path
        best_path = [best_last_state]
        for t in range(T-1, 0, -1):
            best_path.insert(0, Backpointers[t][best_path[0]])

        # Convert state indices to state names
        best_state_sequence = [states[state_index] for state_index in best_path]

        return best_state_sequence





def test_load():
    model = HMM()
    model.load('two_english')
    print("Loaded model: transitions")
    print(model.transitions)
    print("Loaded model: emissions")
    print(model.emissions)

    print("################################################################################")
    print("Loading model: partofspeech.browntags.trained")
    model.load('partofspeech.browntags.trained')
    print("Loaded model: transitions")
    print(model.transitions)
    print("Loaded model: emissions")
    print(model.emissions)
def read_observation(filename):
    observations = []
    with codecs.open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            if line.strip():
                observations.append(line.strip())
    return observations



def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('model_basename', type=str, help='Base name of the HMM model files')
    parser.add_argument('--generate', type=int, help='Generate a sequence of observations of the specified length')
    parser.add_argument('--forward', type=str, help='Compute the forward probability of an observation')
    parser.add_argument('--viterbi', type=str, help='Compute the Viterbi path for an observation')


    args = parser.parse_args()

    hmm = HMM()
    hmm.load(args.model_basename)

    if args.generate:
        observation = hmm.generate(args.generate)
        print(observation)

    if args.forward:
        observations = read_observation(args.forward)
        for observation in observations:
            print(f"Observation: {observation}")
            print("the most likely final state:", hmm.forward(observation))

    if args.viterbi:
        observations = read_observation(args.viterbi)
        for observation in observations:
            state_sequence = hmm.viterbi(observation)
            # print(f"Observation: {observation}")
            # print(f"State sequence: {' '.join(state_sequence)}")
            print(' '.join(state_sequence))
            print(observation)

if __name__ == '__main__':

    main()




