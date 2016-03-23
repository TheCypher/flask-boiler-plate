# Difine the application directory
import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))


# Define database
# SQLite
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'nick.db')
DATABASE_CONNECT_OPTIONS = {}

# Not sure what this does but to be safe turn off
# to save memory.
SQLALCHEMY_TRACK_MODIFICATIONS = False


# Application threads. A common general assumption is
# using 2 per availible processor cores - to handle
# incoming requests using one and performing background
# operations using the other.

THREADS_PER_PAGE = 2


# Enable protection agains *Cross-site Request Forgery (CSRF)*
CSRF_ENABLED  = True


# Use a secure, unique and absolutely secret key for
# signing the data. 
CSRF_SESSION_KEY = "secret"

# Secret key for signing cookies
SECRET_KEY = "secret"

# Application server config
SERVER = {'DEBUG' : True, 'PORT' : 8000, 'HOST' : '0.0.0.0'}