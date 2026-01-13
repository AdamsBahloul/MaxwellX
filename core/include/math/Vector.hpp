#pragma once
#include <cmath>

struct Vector2 {
    double x, y;

    Vector2(double x_=0, double y_=0) : x(x_), y(y_) {}

    Vector2 operator+(const Vector2& o) const {
        return {x + o.x, y + o.y};
    }

    Vector2 operator-(const Vector2& o) const {
        return {x - o.x, y - o.y};
    }

    Vector2 operator*(double s) const {
        return {x * s, y * s};
    }

    double norm() const {
        return std::sqrt(x*x + y*y);
    }
};
