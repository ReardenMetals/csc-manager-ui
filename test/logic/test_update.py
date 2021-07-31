from unittest.mock import Mock, MagicMock

from logic.coin_files_saver import FileKey
from logic.update import UpdateProcessor


def test_update():
    last_good_coin = 'A0004'
    numbers_list = [
        'A0000',
        'A0001',
        'A0002',
        'A0003',
        'A0004',
        'A0005',
        'A0006',
        'A0007',
        'A0008',
        'A0009'
    ]

    labels_list = [
        '16hcB19aq5o8ZsMYuLSKJFUox18DMg7EkF, 6hcB19',
        '1M9uq4pJH8nwauShL5cEdrEJGJFXUBJZ8D, M9uq4p',
        '1MR1ZgYEiUksFdvXZ2cwgJDn6TW8ZtQHYX, MR1ZgY',
        '19tXfABHrp9oAWsNAzbSz5j8L34iXfNdq6, 9tXfAB',
        '1PrjsYHtL8YsfLYmn68rUAUMUe6ytk3YMU, PrjsYH',
        '1N3md8Sn68NpYxC45xjHcg66R7oBa8VcWe, N3md8S',
        '1ANmrnLL8GsvVEo9GMN67rmoYgut4F7Mp4, ANmrnL',
        '15Vu9ftHSp4A4M9xvKdaMR6U9SsBGDrNx4, 5Vu9ft',
        '1MJWnLVHAi6mgp2QSg8msUF6HLXyhYj5vz, MJWnLV',
        '19TFwxekWjvFfLGhu3Z4f2QpSuXQccNWj3, 9TFwxe',
    ]

    key_list = [
        'L1N4iayJQHGituYeeKEGhrMKdLjWgEepfiLvFKSFzEvGdqWAv1s5',
        'L4BLgbNMdQEQZgY6CPVa1iHAqhKHP26AozpGaEaSCjvuod2xJctY',
        'L1dGGuuaoZwmXEKD34f5xAgAVNi2N34NWQui5bt1nDfLrhKWyMsb',
        'L3R7LmxqgwXbW9JKSYqyPMfmQ6WY5RmFTCXR4V9pZY5KPBUGs7ga',
        'L3J9VxbR7vCqJ3ofrye3fNmQKqLigfruoUrS9WZ6cWjnNodNQxRz',
        'KzvpEmGvYX4a4EozC7uD4MDXxA8TsifVyGteTWnARzkFWFLF5WdK',
        'L5FzaRYA2uaPmWMovVE4KgiodGkHrKVnVxfY2nBvYRcoZvpCmLyU',
        'L2CAs4PEmxFkm88Q5ne77enL3cvfT1rUzdWmcMzRNngbetMaFBuE',
        'L4MFfyoe1dRrr7e42Hz2UJ45i4sCXyEQwLBMGTcnFGvA1sTPcfn6',
        'KzvMdkT8DeYuikqXd86eq1CWuauiEEomR77YQTZsv6BwYRtLiRUd'
    ]

    snip_list = [
        '6hcB19',
        'M9uq4p',
        'MR1ZgY',
        '9tXfAB',
        'PrjsYH',
        'N3md8S',
        'ANmrnL',
        '5Vu9ft',
        'MJWnLV',
        '9TFwxe'
    ]
    keypair_list = [
        'WIF,Address,Seed',
        'L1N4iayJQHGituYeeKEGhrMKdLjWgEepfiLvFKSFzEvGdqWAv1s5,16hcB19aq5o8ZsMYuLSKJFUox18DMg7EkF,believe rely merry '
        'cabin slot perfect daughter police absent scene gun nut',
        'L4BLgbNMdQEQZgY6CPVa1iHAqhKHP26AozpGaEaSCjvuod2xJctY,1M9uq4pJH8nwauShL5cEdrEJGJFXUBJZ8D,fox dwarf correct '
        'bubble journey live sound ability mercy evidence caution half',
        'L1dGGuuaoZwmXEKD34f5xAgAVNi2N34NWQui5bt1nDfLrhKWyMsb,1MR1ZgYEiUksFdvXZ2cwgJDn6TW8ZtQHYX,smoke gate when '
        'peace shove volume jealous uncover pause love wrap release',
        'L3R7LmxqgwXbW9JKSYqyPMfmQ6WY5RmFTCXR4V9pZY5KPBUGs7ga,19tXfABHrp9oAWsNAzbSz5j8L34iXfNdq6,special month coin '
        'middle umbrella critic zebra find exclude absorb camp trial',
        'L3J9VxbR7vCqJ3ofrye3fNmQKqLigfruoUrS9WZ6cWjnNodNQxRz,1PrjsYHtL8YsfLYmn68rUAUMUe6ytk3YMU,lyrics craft idea '
        'bicycle kite depth seek stadium social false shove try',
        'KzvpEmGvYX4a4EozC7uD4MDXxA8TsifVyGteTWnARzkFWFLF5WdK,1N3md8Sn68NpYxC45xjHcg66R7oBa8VcWe,reward oppose '
        'surround liberty replace birth ability frozen ethics unfold wealth cube',
        'L5FzaRYA2uaPmWMovVE4KgiodGkHrKVnVxfY2nBvYRcoZvpCmLyU,1ANmrnLL8GsvVEo9GMN67rmoYgut4F7Mp4,erosion water robust '
        'rifle world super avoid strong check fruit order butter',
        'L2CAs4PEmxFkm88Q5ne77enL3cvfT1rUzdWmcMzRNngbetMaFBuE,15Vu9ftHSp4A4M9xvKdaMR6U9SsBGDrNx4,brown planet '
        'bachelor laptop very word scare embark green comfort december raise',
        'L4MFfyoe1dRrr7e42Hz2UJ45i4sCXyEQwLBMGTcnFGvA1sTPcfn6,1MJWnLVHAi6mgp2QSg8msUF6HLXyhYj5vz,dance mask vanish '
        'anchor play expect hello acquire current ugly icon neither',
        'KzvMdkT8DeYuikqXd86eq1CWuauiEEomR77YQTZsv6BwYRtLiRUd,19TFwxekWjvFfLGhu3Z4f2QpSuXQccNWj3,dune drum glove '
        'impulse isolate engine enough summer mass uncle close mobile '
    ]
    coin_file_saver = Mock()
    coin_file_saver.read_sequence_coin_id.return_value = numbers_list

    def read_from_file_by_key(key: FileKey):
        if key == FileKey.BASE_FILE_KEY:
            return keypair_list
        if key == FileKey.SNIP_FILE_KEY:
            return snip_list
        if key == FileKey.PRIVATE_FILE_KEY:
            return key_list
        if key == FileKey.LABELS_FILE_KEY:
            return labels_list
        if key == FileKey.NUMBERS_FILE_KEY:
            return numbers_list

    coin_file_saver.read_from_file_by_key = MagicMock(side_effect=read_from_file_by_key)

    def save_to_file_by_key(lines, key: FileKey):
        items_count = numbers_list.index(last_good_coin) + 1
        if key == FileKey.BASE_FILE_KEY:
            assert len(lines) == items_count + 1
            assert lines[1] == keypair_list[6] + '\n'
        if key == FileKey.SNIP_FILE_KEY:
            assert len(lines) == items_count
            assert lines[0] == snip_list[5] + '\n'
        if key == FileKey.PRIVATE_FILE_KEY:
            assert len(lines) == items_count
            assert lines[0] == key_list[5] + '\n'
        if key == FileKey.LABELS_FILE_KEY:
            assert len(lines) == items_count
            assert lines[0] == labels_list[5] + '\n'
        if key == FileKey.NUMBERS_FILE_KEY:
            assert len(lines) == items_count
            assert lines[0] == numbers_list[5] + '\n'

    coin_file_saver.save_to_file_by_key = MagicMock(side_effect=save_to_file_by_key)

    update_processor = UpdateProcessor(coin_file_saver=coin_file_saver)
    update_processor.update(last_good_coin=last_good_coin)
