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

def test_carnet():
    carnet.main()

def test_carnet_KeyPresent():
    carnet_KeyPresent.main()


if __name__ == '__main__':


    # test_HMM()
    #test_carnet()
    test_carnet_KeyPresent()
