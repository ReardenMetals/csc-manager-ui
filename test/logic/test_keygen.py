from keygen.crypto_coin import CryptoCoin
from keygen.currencies.btc_crypto_coin_service import BtcCoinService
from logic.keygen import KeygenProcessor
from unittest.mock import Mock


def test_keygen():
    count = 3
    currency = 'BTC'
    laser = 'A'

    asset_ids = ['Nv7Q8D', '2JpYwg', '4LHRes']
    coins = [
        CryptoCoin(address='1Nv7Q8DNRACY23tzJd7bHnbGBba3vpiYp5',
                   wif='L2phQzEhgrtbxPjeY9rJA8jXdNy3nbzNhF5V7rJNL1GrBX2HLs5t',
                   seed='wrong angry guilt crucial town rifle oyster business finger vendor favorite story'),
        CryptoCoin(address='12JpYwg54fZSDZRfmRL5uKocsgvmmbqo3T',
                   wif='Kyk7oiU5UYRr5KAEVp2kpyvAXcrfvys68CXFVphsjjeJTkg6Wq7C',
                   seed='faculty jaguar garlic obey piece average trend frown strong void speed tank'),
        CryptoCoin(address='14LHResr7USCqxYPwML3py1Zp2DyicTQCe',
                   wif='L5BkyNWnLDnAA81enTXq9k3aC8jqj1Bc1LCkPy1KjmDV3xu91e5n',
                   seed='enforce elite odor wink wheat purse exclude suffer oil polar rose hobby'),
    ]

    coin_factory = Mock()
    coin_file_saver = Mock()

    service = BtcCoinService()
    service_mock = Mock(spec=service, wraps=service)
    service_mock.generate_list.return_value = coins

    coin_factory.get_coin_service.return_value = service_mock

    keygen_processor = KeygenProcessor(coin_factory=coin_factory, coin_file_saver=coin_file_saver)
    keygen_processor.generate_keys(count=count, coin=currency, laser=laser)

    assert currency == coin_factory.get_coin_service.call_args.args[0]
    assert count == coin_factory.get_coin_service().generate_list.call_args.args[0]

    index = 2

    main_lines = coin_file_saver.save_coins_list.call_args.args[0]
    assert coins[index].wif + ',' + coins[index].address + ',' + coins[index].seed + '\n' == main_lines[index+1]

    asset_id_lines = coin_file_saver.save_asset_ids.call_args.args[0]
    assert asset_ids[index] + '\n' == asset_id_lines[index]

    private_key_lines = coin_file_saver.save_private_keys.call_args.args[0]
    assert coins[index].wif + '\n' == private_key_lines[index]

    public_key_lines = coin_file_saver.save_public_keys.call_args.args[0]
    assert coins[index].address + ',' + asset_ids[index] + '\n' == public_key_lines[index]

    sequence_lines = coin_file_saver.save_sequence_coin_id.call_args.args[0]
    assert laser + '000' + str(index) + '\n' == sequence_lines[index]
