from sqlalchemy.engine import make_url
from llama_index.vector_stores.postgres import PGVectorStore
import psycopg2
import NodeEmbedder  


class Connector:
    
    """
    Connect to psql database and store vector embeddings.

    Args: 
        [database configuration parameters should be stored in db_config.ini ]
        db_name (str): Name of the PostgreSQL database where the vectors will be stored.
    host (str): Host address of the PostgreSQL server.
    password (str): Password for the PostgreSQL user.
    port (str): Port number on which the PostgreSQL server is running.
    user (str): Username for connecting to the PostgreSQL database.
    table_name (str): Name of the table in PostgreSQL where embeddings/nodes will be stored.
    nodes (NodeEmbedder): A collection of nodes generated using NodeEmbedder
    to be uploaded into the vector store.


    Returns:
        str: connection status
    """
    
    
    
    def __init__(
        self,
        db_name: str,
        host: str,
        password: str,
        port: str,
        user: str,
        table_name: str,
        nodes: NodeEmbedder,
    ):
        self._db_name = db_name
        self._host = host
        self._password = password
        self._port = port
        self._user = user
        self._table_name = table_name
        self._nodes = nodes

    def _connect_storeVector(self):
        try:
            # Establish DB connection
            connection = psycopg2.connect(
                dbname=self._db_name,
                host=self._host,
                password=self._password,
                port=self._port,
                user=self._user,
            )
            connection.autocommit = True

            # Create vector store
            vector_store = PGVectorStore.from_params(
                database=self._db_name,
                host=self._host,
                password=self._password,
                port=self._port,
                user=self._user,
                table_name=self._table_name,
                embed_dim=384,
            )

            # Add nodes
            vector_store.add(self._nodes)

            print("Everything is uploaded successfully!")
            return vector_store
        except Exception as e:
            print(f"Upload failed: {e}")
            return None
