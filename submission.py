import HMM
import carnet
import carnet_KeyPresent


def test_HMM():
    model = HMM.HMM()
    print("################################################################################")
    print("Loading model: two_english")
    model.load("two_english")
    print("Loaded model: transitions")
    print(model.transitions)
    print("Loaded model: emissions")
    print(model.emissions)

def test_HMM_generate():
    model = HMM.HMM()
    model.load("partofspeech.browntags.trained")
    print("################################################################################")
    print("Generating 20 observations from the model")
    observation = model.generate(20)
    print(observation)

def test_HMM_forward():
    model = HMM.HMM()
    model.load("partofspeech.browntags.trained")
    print("################################################################################")
    observations = HMM.read_observation("ambiguous_sents.obs")
    for observation in observations:
        print(f"Observation: {observation}")
        print("the most likely final state:", model.forward(observation))

def test_HMM_viterbi():
    model = HMM.HMM()
    model.load("partofspeech.browntags.trained")
    print("################################################################################")
    observations = HMM.read_observation("ambiguous_sents.obs")
    for observation in observations:
        state_sequence = model.viterbi(observation)
        print(' '.join(state_sequence))
        print(observation)
def test_carnet():
    carnet.main()

def test_carnet_KeyPresent():
    carnet_KeyPresent.main()


if __name__ == '__main__':


    test_HMM()
    test_carnet()
    test_carnet_KeyPresent()
    test_HMM_generate()
    test_HMM_forward()
    test_HMM_viterbi()
    pass
