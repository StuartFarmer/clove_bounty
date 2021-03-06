
from clove.network.bitcoin import Bitcoin


class Bitcurrency(Bitcoin):
    """
    Class with all the necessary BTCR network information based on
    http://www.github.com/tokyoghetto/BitCurrencyPro/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'bitcurrency'
    symbols = ('BTCR', )
    seeds = ('dns0.BitCurrencyPro.org',)
    port = 16814


class BitcurrencyTestNet(Bitcurrency):
    """
    Class with all the necessary BTCR testing network information based on
    http://www.github.com/tokyoghetto/BitCurrencyPro/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'test-bitcurrency'
    seeds = ('dns1.BitCurrencyPro.org', 'dns2.BitCurrencyPro.org', 'dns3.BitCurrencyPro.org', 'dns4.BitCurrencyPro.org', 'dns5.BitCurrencyPro.org', 'dns6.BitCurrencyPro.org', 'dns7.BitCurrencyPro.org', 'dns8.BitCurrencyPro.org', 'dns9.BitCurrencyPro.org')
    port = 26814
