

# local libraries
import orbit_calculations as oc


def test_calc_JD():
    JD = oc.calc_JD()

    assert JD == 2455197.96671 # 01/01/2010 11:12:4

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
