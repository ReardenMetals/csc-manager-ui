from crypto_coin_factory import CoinFactoryExtended


def get_coin_address(currency, private_key):
    service = CoinFactoryExtended().get_coin_service(currency)
    return service.get_address(private_key)


def test_btc():
    address = get_coin_address('BTC', '5Ke8bzyw8g1H172bCU4jCXQpvVRD3eSFCmsxR81RYJZpTM7xL9X')
    assert '1GDLTzQDLJJLnihqVgcjwuTaSCwx8W4P2B' == address


def test_bch():
    address = get_coin_address('BCH', '5Ke8bzyw8g1H172bCU4jCXQpvVRD3eSFCmsxR81RYJZpTM7xL9X')
    assert 'qznd7gyv3l8ay02skgnperj7rnas4qawgcc90mee7w' == address


def test_ltc():
    address = get_coin_address('LTC', '6vm5LgDCL9kfZGoc7MscpSd9xKWyf6Jj1YQLCDeNTNds8mfzrbV')
    assert 'LgJnMTxsR4tHqxT8Qd2cAeb2sX9PBEscyV' == address


def test_dash():
    address = get_coin_address('DASH', '7rDNFgN32tLmknEC3mpm54VqdworVXrTEbyobbcg1mkvMmPZPdj')
    assert 'XdRsX38wgENu6FrGx3wx6qnSTz7XVwANZx' == address


def test_eth():
    address = get_coin_address('ETH', '813c58c6edc5f2689d54ca06efddbfb56feae888abfe30ce8e293224919ec818')
    assert '0x96fe96e97a107fff1f4c619ad1d5c0d568219f53' == address


def test_xmr():
    address = get_coin_address('XMR', 'e22b4f6e0d81cd7b71f5d2bcf4191c8ed893c0adac59c9f2bf22c27cece1f90d')
    assert '476vPMXFMjJKMrzTtBDCtfNYxVbX1HnqxTaYmoJ8sz9oZLFAbKastHXMVX5BckcdK9fawU4NgooPsYjWngfKFrq4FLMRNiU' == address


def test_pote():
    address = get_coin_address('POTE', '79pHKdz8jC6m9WkBRpira7yMCdpDLZKmKxStsAcMi1XDrja45kQ')
    assert 'PDyWMDMbqBeyKYAtUon5UnB3MH5qmjLaFc' == address


def test_bnb():
    address = get_coin_address('BNB', 'aa541689331812de852348b0fae3a896bf82ddd709dc75896df345e16c409c8b')
    assert 'bnb1upfqv7y0hdzvlrznwt83jklsl49lewcclhg9zu' == address


def test_eos():
    address = get_coin_address('EOS', '5JyZpiLFnCy7JGn4TEKEFSU6pRwne3vgciJbUq5pT2wzM4bvrBB')
    assert 'EOS6ZsC7LhKtAew7srZ6wUDk2HgzRtDscZVHTAbZiMyDCwdUbXKjq' == address


def test_doge():
    address = get_coin_address('DOGE', 'QTtBXsAXSG8miomDVfmvYZVr4AHH9kpkrthAjviZzgxbzkc87eb6')
    assert 'DST5AnAAqdjM1HQX9vLmHdwKjUpWYQQnaX' == address
