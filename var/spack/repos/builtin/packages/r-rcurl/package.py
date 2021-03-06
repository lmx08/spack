# Copyright 2013-2018 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class RRcurl(RPackage):
    """A wrapper for 'libcurl' <http://curl.haxx.se/libcurl/> Provides
       functions to allow one to compose general HTTP requests and provides
       convenient functions to fetch URIs, get & post forms, etc. and process
       the results returned by the Web server. This provides a great deal of
       control over the HTTP/FTP/... connection and the form of the request
       while providing a higher-level interface than is available just using
       R socket connections. Additionally, the underlying implementation is
       robust and extensive, supporting FTP/FTPS/TFTP (uploads and downloads),
       SSL/HTTPS, telnet, dict, ldap, and also supports cookies, redirects,
       authentication, etc."""

    homepage = "https://cran.rstudio.com/web/packages/RCurl/index.html"
    url      = "https://cran.rstudio.com/src/contrib/RCurl_1.95-4.8.tar.gz"
    list_url = "https://cran.r-project.org/src/contrib/Archive/RCurl"

    version('1.95-4.8', '9c8aaff986eb2792c89dd3ae54d21580')

    depends_on('r-bitops', type=('build', 'run'))
    depends_on('curl')
