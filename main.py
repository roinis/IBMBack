from db_utils import db
from db_utils import init_db
from modules.web_server import WebServer


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    init_db.init()
    web_server = WebServer()
    web_server.start_web_server()

