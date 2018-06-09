import os

# grab the folder where this script lives
basedir = os.path.abspath(os.path.dirname(__file__))

DATABASE = 'flasktaskr.db'
USERNAME = 'admin'
PASSWORD = 'admin'
WTF_CSRF_ENABLED = True
SECRET_KEY = r'l-\xc9\xb8x#\x9e,\xa0\x9e\x11\xf2K\x7f\xbe\xee%~OaD$\x14\x9f'

# define the full path for the database
DATABASE_PATH = os.path.join(basedir, DATABASE)