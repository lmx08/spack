# Copyright 2013-2018 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class RRcppeigen(RPackage):
    """R and 'Eigen' integration using 'Rcpp'. 'Eigen' is a C++ template
    library for linear algebra: matrices, vectors, numerical solvers and
    related algorithms. It supports dense and sparse matrices on integer,
    floating point and complex numbers, decompositions of such matrices, and
    solutions of linear systems. Its performance on many algorithms is
    comparable with some of the best implementations based on 'Lapack' and
    level-3 'BLAS'. The 'RcppEigen' package includes the header files from the
    'Eigen' C++ template library (currently version 3.2.8). Thus users do not
    need to install 'Eigen' itself in order to use 'RcppEigen'. Since version
    3.1.1, 'Eigen' is licensed under the Mozilla Public License (version 2);
    earlier version were licensed under the GNU LGPL version 3 or later.
    'RcppEigen' (the 'Rcpp' bindings/bridge to 'Eigen') is licensed under the
    GNU GPL version 2 or later, as is the rest of 'Rcpp'."""

    homepage = "http://eigen.tuxfamily.org/"
    url      = "https://cran.r-project.org/src/contrib/RcppEigen_0.3.2.9.0.tar.gz"
    list_url = "https://cran.r-project.org/src/contrib/Archive/RcppEigen"

    version('0.3.3.3.1', '1a5ae17828813e40e6b3e7400e408a2b')
    version('0.3.2.9.0', '14a7786882a5d9862d53c4b2217df318')
    version('0.3.2.8.1', '4146e06e4fdf7f4d08db7839069d479f')

    depends_on('r-matrix', type=('build', 'run'))
    depends_on('r-rcpp', type=('build', 'run'))
