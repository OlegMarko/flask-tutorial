import os


class Config:

    APPLICATION_DIR = os.path.dirname(os.path.realpath(__file__))
    DEBUG = True

    SQLALCHIMY_DATABASE_URL = 'sqlite:///%s/blog.db?check_same_thread=False' % APPLICATION_DIR

