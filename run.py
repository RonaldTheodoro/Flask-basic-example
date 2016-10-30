from app import app
from decouple import config


if __name__ == '__main__':
    DEBUG = config('DEBUG', default=False, cast=bool)
    PORT = config('PORT', default=5000, cast=int)
    
    app.run(debug=DEBUG, port=PORT)