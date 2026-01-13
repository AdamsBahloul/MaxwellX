#pragma once
#include <vector>
#include "../physics/Charge.hpp"

class Simulator {
public:
    void add_charge(double q, double x, double y);
    Vector2 electric_field(double x, double y);

private:
    std::vector<Charge> charges;
};
