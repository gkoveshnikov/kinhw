#include "bloch_rhs.h"
#include <Eigen/Dense>
#include <Eigen/src/Core/Matrix.h>

namespace bloch_rhs {

using namespace Eigen;

Eigen::Vector3d basic(const Eigen::Vector3d &n, 
    double T_parallel, double T_perp) {
  Eigen::Vector3d dn(
      -1/T_perp * n[0],
      -1/T_perp * n[1],
      -1/T_parallel * n[2]
      );
  return dn;
}

Vector3d bloch_rhs_rotating_field(const Vector3d &n, double t) {
  Vector3d B(cos(t*20)*1, sin(t*20)*1, 0.3*20); 
  //B = Vector3d(0,0,1.0);
  double gamma_perp = 0.2, gamma_parallel = 0.1;
  Vector3d rot = 2.0 * B.cross(n);
  Vector3d damp = -Vector3d(gamma_perp * n[0],
      gamma_parallel * n[1], gamma_parallel * n[0]);
  return rot + damp;
}

}
