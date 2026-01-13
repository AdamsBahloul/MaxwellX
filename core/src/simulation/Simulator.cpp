#include "../../include/simulation/Simulator.hpp"

static constexpr double k = 8.9875517923e9;

void Simulator::add_charge(double q, double x, double y) {
    charges.emplace_back(q, Vector2(x, y));
}

Vector2 Simulator::electric_field(double x, double y) {
    Vector2 E(0,0);
    Vector2 p(x, y);

    for (auto& c : charges) {
        Vector2 r = p - c.position;
        double d = r.norm() + 1e-9;
        E = E + r * (k * c.q / (d*d*d));
    }
    return E;
}
