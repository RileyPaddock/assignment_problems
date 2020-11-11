from neuron import Neuron


def s_t(t):
    if 10 <= t <= 11 or 20 <= t <= 21 or \
            30 <= t <= 40 or 50 <= t <= 51 or \
            53 <= t <= 54 or 56 <= t <= 57 or \
            59 <= t <= 60 or 62 <= t <= 63 or \
            65 <= t <= 66:
        return 150
    return 0


neuron = Neuron(s_t)
neuron.plot_activity()


