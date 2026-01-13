#include <pybind11/pybind11.h>
#include "../core/include/simulation/Simulator.hpp"

namespace py = pybind11;

PYBIND11_MODULE(_maxwellx, m) {
    py::class_<Simulator>(m, "Simulator")
        .def(py::init<>())
        .def("add_charge", &Simulator::add_charge)
        .def("electric_field",
             [](Simulator& s, double x, double y) {
                 auto E = s.electric_field(x, y);
                 return py::make_tuple(E.x, E.y);
             });
}
