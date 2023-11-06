import HMM

def test_HMM():
    model = HMM.HMM()
    print("################################################################################")
    print("Loading model: two_english")
    model.load("two_english")
    print("Loaded model: transitions")
    print(model.transitions)
    print("Loaded model: emissions")
    print(model.emissions)


if __name__ == '__main__':


    test_HMM()
