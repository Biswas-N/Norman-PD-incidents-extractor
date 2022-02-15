from project0 import SampleClass

def test_say_hi():
    sampleClass = SampleClass()

    want = "Hey Biswas"
    got = sampleClass.say_hi("Biswas")

    assert want == got
