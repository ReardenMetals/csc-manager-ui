from coin_factory_inject import coinFactory


def test_coin():
    currency = "ETH"
    service = coinFactory.get_coin_service(currency)
    coin = service.generate()
    print(currency)
    print(coin)



