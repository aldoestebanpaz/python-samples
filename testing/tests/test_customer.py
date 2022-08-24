import pytest
from datetime import datetime
from src.customer import Customer



def test_single_instance():
  # arrange
  name = "aldo"
  email = "apaz@noemail.com"

  # act
  customer = Customer(name, email)

  # assert
  assert customer.name == name
  assert customer.email == email



@pytest.mark.parametrize(
  "name,email",
  [
    ("aldo", "apaz@noemail.com"),
    ("ella", "ella@ella.com"),
    ("foo", "foo@bar.com"),
  ]
)
def test_multiple_instances(name, email):
  # act
  customer = Customer(name, email)

  # assert
  assert customer.name == name
  assert customer.email == email



def test_instance_to_str():
  # arrange
  name = "aldo"
  email = "apaz@noemail.com"

  # act
  customer = Customer(name, email)

  # assert
  assert str(customer) == "name: aldo, email: apaz@noemail.com"




def test_get_time_of_day(mocker):
  # arrange
  mocked_curr_datetime = datetime(2022, 5, 20, 14, 10, 0)
  mocked_dependency = mocker.patch("src.customer.datetime")
  mocked_dependency.now.return_value = mocked_curr_datetime

  # act
  customer = Customer("aldo", "apaz@noemail.com")

  # assert
  assert customer.created_at == mocked_curr_datetime
