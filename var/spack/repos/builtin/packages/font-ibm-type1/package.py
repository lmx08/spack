# Copyright 2013-2018 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class FontIbmType1(Package):
    """X.org ibm-type1 font."""

    homepage = "http://cgit.freedesktop.org/xorg/font/ibm-type1"
    url      = "https://www.x.org/archive/individual/font/font-ibm-type1-1.0.3.tar.gz"

    version('1.0.3', '2806116e4adcb89d3d5ff5faf65e57c1')

    depends_on('font-util')

    depends_on('fontconfig', type='build')
    depends_on('mkfontdir', type='build')
    depends_on('mkfontscale', type='build')
    depends_on('pkgconfig', type='build')
    depends_on('util-macros', type='build')

    def install(self, spec, prefix):
        configure('--prefix={0}'.format(prefix))

        make('install')

        # `make install` copies the files to the font-util installation.
        # Create a fake directory to convince Spack that we actually
        # installed something.
        mkdir(prefix.lib)
