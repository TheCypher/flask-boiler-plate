from app import app
import config

if __name__ == '__main__':
	app.run(
		debug=config.SERVER['DEBUG'], 
		host=config.SERVER['HOST'], 
		port=config.SERVER['PORT']
	)