from ._maxwellx import Simulator as _Sim

class Simulator:
    def __init__(self):
        self._sim = _Sim()

    def add_charge(self, q, pos):
        self._sim.add_charge(q, pos[0], pos[1])

    def electric_field(self, pos):
        return self._sim.electric_field(pos[0], pos[1])
