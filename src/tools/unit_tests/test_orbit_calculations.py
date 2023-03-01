

# 3rd party libraries
import math as m
# local libraries
import orbit_calculations as oc

def test_calc_JD():
    JD = oc.calc_JD("1:1:2010:11:12:4")

    assert m.isclose(JD, 2455197.96671, rel_tol=1e-4) == True # 01/01/2010 11:12:4

    # - Julian Date (JD) calc
    # - Local Sideral Time (LST) calc
    # - Universal variables
    # - rv2coe
    # - coe2rv
    # - Coordinate transformations
    # - Calculate COEs
    # - Keplers
    # - Orbit transfers
    # - Pertubations options

def test_kepler_E():
    e = 0.37255
    M = 3.6029

    E = oc.kepler_E(e, M)
    assert m.isclose(E, 3.47942, rel_tol=1e-4) == True

def test_sv2coe():
    pass