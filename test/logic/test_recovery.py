from unittest.mock import Mock, MagicMock

from keygen.crypto_coin import CryptoCoin
from logic.recovery import RecoveryProcessor


def test_recovery():
    coins = [
        (CryptoCoin(address='16hcB19aq5o8ZsMYuLSKJFUox18DMg7EkF',
                    wif='L1N4iayJQHGituYeeKEGhrMKdLjWgEepfiLvFKSFzEvGdqWAv1s5',
                    seed='believe rely merry cabin slot perfect daughter police absent scene gun nut'),
         '6hcB19'),
        (CryptoCoin(address='1M9uq4pJH8nwauShL5cEdrEJGJFXUBJZ8D',
                    wif='L4BLgbNMdQEQZgY6CPVa1iHAqhKHP26AozpGaEaSCjvuod2xJctY',
                    seed='fox dwarf correct bubble journey live sound ability mercy evidence caution half'),
         'M9uq4p'),
        (CryptoCoin(address='1MR1ZgYEiUksFdvXZ2cwgJDn6TW8ZtQHYX',
                    wif='L1dGGuuaoZwmXEKD34f5xAgAVNi2N34NWQui5bt1nDfLrhKWyMsb',
                    seed='smoke gate when peace shove volume jealous uncover pause love wrap release'),
         'MR1ZgY'),
    ]
    coin_file_saver = Mock()

    recovery_processor = RecoveryProcessor(coin_file_saver=coin_file_saver)
    recovery_processor.save_recovered_coins(coins)

    recovered_labels = coin_file_saver.save_recovered_labels.call_args.args[0]
    assert coins[2][0].address + ',' + coins[2][1] + '\n' == recovered_labels[2]

    recovered_keys = coin_file_saver.save_recovered_keys.call_args.args[0]
    assert coins[2][0].wif + '\n' == recovered_keys[2]
