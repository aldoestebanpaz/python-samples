import os

class Configuration:
  def __init__(self):
    try:
      self.db_dialect = os.environ["DB_DIALECT"]
      self.db_driver = os.environ["DB_DRIVER"]
      self.db_username = os.environ["DB_USERNAME"]
      self.db_password = os.environ["DB_PASSWORD"]
      self.db_host = os.environ["DB_HOST"]
      self.db_port = os.environ["DB_PORT"]
      self.db_name = os.environ["DB_NAME"]
    except KeyError as e:
      print("Error creating Configuration instance:", e)
      raise ValueError(f"Error creating Configuration instance: {e}")

  def get_connection_string(self):
    # dialect+driver://username:password@host:port/database
    return "{}://{}:{}@{}:{}/{}".format(
      (self.db_dialect if self.db_dialect else "mysql") + (f"+{self.db_driver}" if self.db_driver else ""),
      self.db_username,
      self.db_password,
      (self.db_host if self.db_host else "localhost"),
      (self.db_driver if self.db_driver else 3306),
      self.db_name
    )
