#pragma once
#include <functional>
#include <Eigen/Dense>
#include <Eigen/src/Core/Matrix.h>

namespace bloch_rhs {

Eigen::Vector3d basic(const Eigen::Vector3d &n, 
    double T_parallel, double T_perp);

Eigen::Vector3d bloch_rhs_rotating_field(const Eigen::Vector3d &n, double t);

}
