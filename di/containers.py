"""Containers module."""

import logging.config

from dependency_injector import containers, providers


class MyContainer(containers.DeclarativeContainer):

    config = providers.Configuration()

    logging = providers.Resource(
        logging.config.fileConfig,
        fname='logging.ini',
    )


