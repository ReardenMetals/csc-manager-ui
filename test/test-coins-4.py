from crypto_coin_factory import CoinFactoryExtended


def test_coin():
    currency = "ETH"
    service = CoinFactoryExtended().get_coin_service(currency)
    coin = service.generate()
    print(currency)
    print(coin)



