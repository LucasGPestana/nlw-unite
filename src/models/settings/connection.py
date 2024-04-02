from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine import Engine

class __DBConnectionHandler:

    def __init__(self) -> None:

        self.__connection_string = "{}:///{}".format("sqlite", "./storage.db")
        self.__engine = None
        self.session = None

    def connect_to_db(self) -> None:
        
        self.__engine = create_engine(self.__connection_string)
    
    def get_engine(self) -> Engine:
        
        return self.__engine
    
    def __enter__(self):

        session_maker = sessionmaker()
        self.session = session_maker(bind=self.__engine)

        return self

    def __exit__(self, exc_type, exc_val, exc_tb):

        self.session.close()

DB_CONNECTION_HANDLER = __DBConnectionHandler()