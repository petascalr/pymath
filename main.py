import numpy as np
import matrices
import sys
import numpy as np


def main():
    print(sys.argv)
    # v1 = np.ones(3)
    # m = matrices.randSquareMat(8);
    # m.print()

    # matr = matrices.mat_rand(3, 3)
    # mt = matrices.mat_transp(matr)
    # matrices.mat_print(matr)
    # matrices.mat_print(mt)

    matr = matrices.mat_rand(10, 10)
    matrices.mat_mul_scalar(matr, 10)
    matrices.mat_print(matr)
    d1 = matrices.mat_det(matr)
    print("Liviu: ", d1)
    d2 = np.linalg.det(matr)
    print("numpy: ", d2)
    # matrices.mat_print(matr)


if __name__ == "__main__":
    main()