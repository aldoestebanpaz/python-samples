import pytest
from src.configuration import Configuration

def test_exception():
  # assert
  with pytest.raises(ValueError, match=r"Error creating Configuration instance.*"):
    # act
    Configuration()

def test_default_connection_string(monkeypatch):
  # arrange
  monkeypatch.setenv("DB_DIALECT", "")
  monkeypatch.setenv("DB_DRIVER", "")
  monkeypatch.setenv("DB_USERNAME", "foo")
  monkeypatch.setenv("DB_PASSWORD", "bar")
  monkeypatch.setenv("DB_HOST", "")
  monkeypatch.setenv("DB_PORT", "")
  monkeypatch.setenv("DB_NAME", "mydb")

  # act
  connection_string = Configuration().get_connection_string()

  # assert
  assert connection_string == "mysql://foo:bar@localhost:3306/mydb"

@pytest.mark.my_custom_mark
def test_full_connection_string(monkeypatch):
  # arrange
  monkeypatch.setenv("DB_DIALECT", "mysql")
  monkeypatch.setenv("DB_DRIVER", "")
  monkeypatch.setenv("DB_USERNAME", "foo")
  monkeypatch.setenv("DB_PASSWORD", "bar")
  monkeypatch.setenv("DB_HOST", "myhost")
  monkeypatch.setenv("DB_PORT", "3306")
  monkeypatch.setenv("DB_NAME", "mydb")

  # act
  connection_string = Configuration().get_connection_string()

  # assert
  assert connection_string == "mysql://foo:bar@myhost:3306/mydb"