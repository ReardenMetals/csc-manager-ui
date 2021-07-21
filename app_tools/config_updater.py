from configparser import ConfigParser


class ConfigUpdater:

    @staticmethod
    def set_value_in_property_file(section, key, value):
        props = [(section, key, value)]
        ConfigUpdater.set_values_in_property_file(props)

    # args = [(section, key, value), ...]
    @staticmethod
    def set_values_in_property_file(args=[], file_path='config.ini'):
        config = ConfigParser(comment_prefixes="/", allow_no_value=True)
        config.read(file_path)
        for arg in args:
            section = arg[0]
            key = arg[1]
            value = arg[2]
            config.set(section, key, value)
        cfg_file = open(file_path, 'w')
        config.write(cfg_file, space_around_delimiters=False)  # use flag in case case you need to avoid white space.
        cfg_file.close()

    @staticmethod
    def get_property(section, key, file_path='config.ini'):
        config = ConfigParser(comment_prefixes="/", allow_no_value=True)
        config.read(file_path)
        return config.get(section, key)
