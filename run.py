from app import app
from db.database import db
import config


if __name__ == '__main__':
    app.run(port=config.api_port, debug=True)