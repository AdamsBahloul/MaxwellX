#pragma once
#include "../math/Vector.hpp"

struct Charge {
    double q;
    Vector2 position;

    Charge(double q_, Vector2 pos_) : q(q_), position(pos_) {}
};
