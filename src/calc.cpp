#include "calc.h"
#include <Eigen/Dense>
#include <Eigen/src/Core/Matrix.h>

namespace calc {

using namespace Eigen;

Vector3d runge_kutta_step(const Vector3d &n, double t, double dt,
    std::function<Vector3d(Vector3d,double)> func) {
  Vector3d k1 = func(n, t);
  Vector3d k2 = func(n + 0.5 * dt * k1,t);
  Vector3d k3 = func(n + 0.5 * dt * k2,t);
  Vector3d k4 = func(n + dt * k3, t);

  return n + (dt / 6.0) * (k1 + 2 * k2 + 2 * k3 + k4);
}

}
