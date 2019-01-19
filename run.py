import os

from app import create_app

from typing import Optional

config_name: Optional[str]= os.getenv('APP_SETTINGS')
if config_name:
    app = create_app(config_name)

if __name__ == "__main__":
    app.run()
