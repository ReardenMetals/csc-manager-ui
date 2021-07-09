from crypto_coin_factory import CoinFactoryExtended


def get_coin_address(currency, private_key):
    service = CoinFactoryExtended().get_coin_service(currency)
    return service.get_address(private_key)


def test_eth0():
    address = get_coin_address('ETH', 'bb0d723177603b46d3ba5b4aad018b83bd3cf7afc128274948655f2036549858')
    assert '0xd3af1fdfae6a9871c06b90e23193b3785bd2390a' == address


def test_eth1():
    address = get_coin_address('ETH', 'c2afb46249f70cd011cf594e29af09cebd3fa2570774d80d54447f7440031921')
    assert address == '0x6f2a619733dcc8ee9c53766bd906b5985ab274e2'


def test_btc():
    address = get_coin_address('BTC', 'L4MdVAQgrbmZham4zFzam2zh3U68gqGdE7pQ1JKvrfQzrJPBoEdc')
    assert address == '1QHYPXFHJ5zCaQS5HcwNFzPNpDJXnCoXzo'


def test_btc_old():
    address = get_coin_address('BTC', '5JQcan7Ry4mwGEZThCRW2oZJa9QbAMyahg9pR3LJwDhws85NW2r')
    assert address == '1GXXecdih6PSjuSZ14oMQGPHdtLQFYyGTD'


def test_bch():
    address = get_coin_address('BCH', 'KwLq3AMz5rdpALCFyHqfLe8TVHQCh1pHBhoS9yGuneYF8PmpgXEQ')
    assert address == 'qzyvlkdgscpcpaspdknzscs9dl7phkgpjgkah386nq'


def test_bch_old():
    address = get_coin_address('BCH', '5KMm8HtE8Q6x1P5AuTw7zfDTWWV1wcTp73ntYCWwj6dvBNenvth')
    assert address == 'qre49ddrwdgqyjtpv2dahgn7gamwaxjeq54nvjgpwd'


def test_ltc():
    address = get_coin_address('LTC', 'TAwDFcbahqX9RVVz9aT37jscCNitYp3oZM4SkxBhAmNjSZ9RhDrc')
    assert address == 'LbW51HQNTKmkXKv5jKyU2pfvWSVUeQxA4X'


def test_ltc_old():
    address = get_coin_address('LTC', '6vzYB89RnDcYJBrfY6ansERJ2K5f44jkn2UuqXs3wd229W1U4tB')
    assert address == 'LgU4TSGEkd8PzRiC343pqAPM9M1X9kcFhD'


def test_dash():
    address = get_coin_address('DASH', 'XH7URm12Kksn2dkECSHoExCA5Bnvj3XwbJTdhVVBFnugb4hKHBN2')
    assert address == 'Xjtu6nYbd7ki9NBVB1LXFvDWCPTsAvyPmb'


def test_dash_old():
    address = get_coin_address('DASH', '7rK9xTSzzgAt1N3XWAm8Erc7CJhxc6yyciteLZFU9pVaXozGbNZ')
    assert address == 'Xy79yMGZkeDkqq5GcLhK32zGnomQUXZ4uF'


def test_bsv():
    address = get_coin_address('BSV', 'L4NpF6jfGEtSJ5YCsTQHgkC9zEzAqm913Qxr9Yc2QqsYyt2Gkj7Z')
    assert address == '1PpyrNBE5hRmDK9MWyFZr2sPfT4iRUUYF'


def test_doge():
    address = get_coin_address('DOGE', 'QXArcQ4YdLcxfBkEMucxq1BCfJWUodS7VvNzsEgSSdAt8ioRriey')
    assert address == 'DLH5B4bx4zJ7ZQvphYi5nVJq6fVTPZoT9g'


def test_xrp():
    address = get_coin_address('XRP', 'daf456513aa770d560ab0929a5d31abb81527e88ec1f2ebd7fd6c2947f822db1')
    assert address == 'raSs1L8hDhVGkpvqyQyyY9RVjGPHS6eVdf'


def test_bnb():
    address = get_coin_address('BNB', 'aa541689331812de852348b0fae3a896bf82ddd709dc75896df345e16c409c8b')
    assert address == 'bnb1upfqv7y0hdzvlrznwt83jklsl49lewcclhg9zu'


def test_xmr():
    address = get_coin_address('XMR', '876604d806600496bc05b8b594c9eee5bdfdc97bc8e599096d7bf73be982b20f')
    assert address == '4AYVcwKNaXAJMNeGYVSQ4JD1ovp3i5K7dSbJ2PpYk6KDDxoHc8bwUgqBoA7ZAw8UfLRdhJYmBitjMeBoNscH21XjJyRvBqm'


def test_eos():
    address = get_coin_address('EOS', '5JbaS3Aec97j5G3NHxspfc6xNMT3qEEGpZNbB3GQH3SnNpsGPb5')
    assert address == 'EOS8MWYCQXbs61djAneDLpQHjXe14WMJX9q2eGACoHx9BFLwTz7N5'


def test_pote0():
    address = get_coin_address('POTE', 'U9ZdLDCXhaY5NDkqKuxJwfZUXixKQExgor8MtqGwrzfjx4UoTtQ3')
    assert address == 'PRYU7GUm9BYVya4WgH8iXUCBdwk3dKmKEJ'


def test_pote1():
    address = get_coin_address('POTE', '79mUxQE976DM88ZtUgpFcGMUQEyF3wrSnnSprQjtAk4nQRyQQLf')
    assert address == 'PMT9ZBoJ8D7gq9AhVmRij2X6VtKMXZCCcW'

