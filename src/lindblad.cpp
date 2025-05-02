#include <eigen3/Eigen/Dense>
#include <eigen3/Eigen/src/Core/Matrix.h>
#include <fstream>
#include <functional>
#include "calc.h"
#include "bloch_rhs.h"


int main() {
  using namespace calc;
  using namespace bloch_rhs;
  double a = 0.05;
  double b = 0.1;
  double T_parallel = 1 / (4 * b);
  double T_perp = 1 / (2 * a + 2 * b);

  Eigen::Vector3d n (1.0, 0.0, 0.0);
  double dt = 0.01, tmax = 10.0;
  std::ofstream fout("bloch.csv");
  
  fout << "# t,nx,ny,nz\n";
  std::function<Eigen::Vector3d(Eigen::Vector3d,double)> func 
    = [T_parallel, T_perp] (Eigen::Vector3d n, double t) { return basic(n, T_parallel, T_perp); }; 
  for(double t = 0; t <= tmax; t+=dt) {
    fout << t << "," << n[0] << "," << n[1] << "," << n[2] << "\n";
    n = runge_kutta_step(n, t, dt, bloch_rhs_rotating_field);
  }
  fout.close();
  return 0;
}
