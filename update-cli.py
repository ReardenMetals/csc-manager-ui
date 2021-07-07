from logic.update import UpdateProcessor


def main():
    update_processor = UpdateProcessor()
    good_coin = input("Enter the last good coin id : ")
    update_processor.update(good_coin)


if __name__ == "__main__":
    main()
