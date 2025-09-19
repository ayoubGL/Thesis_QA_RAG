from sqlalchemy.engine import make_url
from llama_index.vector_stores.postgres import PGVectorStore
import psycopg2
import NodeEmbedder
from sqlalchemy.engine import make_url
from llama_index.vector_stores.postgres import PGVectorStore


class DBConnect:
    
    def __init__(
        db_name: str, 
        host: str,
        password: str,
        port:str,
        user:str,
        table_name:str 
        self,
    ):
        self._db_name = db_name,
        self._host = host,
        self._password = password,
        self._port = port,
        self._user = user,
        self._table_name = table_name
        
    
    connection = psycopg2.connect(
        db_name = self._db_name,
        host = self._host,
        password = self._password,
        port =  self._port,
        
    )
    connection.autocommit = True
    
    vector_score = PGVectorStore.from_params(
        
        db_name = self._db_name,
        host = self._host,
        password = self._password,
        port =  self._port,
        user = self._user,
        embed_dim = 384,
    )
    
    nodes = NodeEmbedder()
    
    vector_score.add(nodes)
    
    
    if vector_score:
        return "nodes is stored"