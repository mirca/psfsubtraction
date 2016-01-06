import numpy as np


def psf_from_projection(self, image1d, psfbase):
    '''solve a linear algebra system for the best PSF

    Parameters
    ----------
    image1d : array in 1 dim
    psfbase : array in [M,N]
        M = number of pixels in flattened image
        N = number of images that form the space of potential PSFs

    Returns
    -------
    psf_coeff : array in 1 dim
        Coefficients for a linear combination of ``psfbase`` elements that
        that give the optimal PSF.
    '''
    a = np.dot(psfbase.T, psfbase)
    b = np.dot(psfbase.T, image1d)
    psf_coeff = np.linalg.solve(a, b)
    return psf_coeff
