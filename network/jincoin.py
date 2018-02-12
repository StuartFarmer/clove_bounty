
from clove.network.bitcoin import Bitcoin


class Jincoin(Bitcoin):
    """
    Class with all the necessary JIN network information based on
    https://github.com/JinCoin/Jincoin-Core/blob/master/src/chainparams.cpp
    (date of access: 02/12/2018)
    """
    name = 'jincoin'
    symbols = ('JIN', )
    seeds = (
        'seed1.jin-coin.info',
        'seed2.jin-coin.info',
        'seed3.jin-coin.info',
        'seed1.jin-coin.com',
        'seed2.jin-coin.com',
        'seed3.jin-coin.com',
    )
    port = 23099


class JincoinTestNet(Jincoin):
    """
    Class with all the necessary JIN testing network information based on
    https://github.com/JinCoin/Jincoin-Core/blob/master/src/chainparams.cpp
    (date of access: 02/12/2018)
    """
    name = 'test-jincoin'
    seeds = ()
    port = 33099
