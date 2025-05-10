#pragma once
#include <functional>
#include <Eigen/Dense>
#include <Eigen/src/Core/Matrix.h>

namespace calc {

Eigen::Vector3d runge_kutta_step(const Eigen::Vector3d &n, double t, double dt,
    std::function<Eigen::Vector3d(Eigen::Vector3d,double)> func);
}
