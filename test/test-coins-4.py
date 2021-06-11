from keygen.crypto_coin_factory import CoinFactory


def test_coin():
    currency = "ETH"
    service = CoinFactory.get_coin_service(currency)
    coin = service.generate()
    print(currency)
    print(coin)



