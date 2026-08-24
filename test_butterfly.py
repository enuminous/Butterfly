import unittest
from butterfly import Layer, Edge, compare_runs, feedback_gain

class TestButterfly(unittest.TestCase):
    def test_zeroish_small_delta_propagates_less_than_large(self):
        layers = {
            "a":Layer(0.4,base=0.1,threshold=0.8),
            "b":Layer(0.3,base=0.1,threshold=0.7),
        }
        edges=[Edge("a","b",0.9)]
        small=compare_runs(layers,edges,"a",0.01,steps=4,deviation_threshold=0.001)
        large=compare_runs(layers,edges,"a",0.2,steps=4,deviation_threshold=0.001)
        self.assertGreater(large["cross_layer_amplification"]*0.2,
                           small["cross_layer_amplification"]*0.01)

    def test_feedback_gain_defined(self):
        layers = {
            "a":Layer(0.6,base=0.1,threshold=0.7),
            "b":Layer(0.5,base=0.1,threshold=0.65),
        }
        edges=[Edge("a","b",0.8),Edge("b","a",0.3,feedback=True)]
        g=feedback_gain(layers,edges,"a",0.1,steps=5)
        self.assertGreater(g,0)

    def test_boundary_crossing_detected(self):
        layers = {
            "a":Layer(0.69,base=0.69,threshold=0.7),
        }
        out=compare_runs(layers,[],"a",0.05,steps=0,deviation_threshold=0.001)
        self.assertGreater(out["boundary_crossings"],0)

if __name__ == "__main__":
    unittest.main()
