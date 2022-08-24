from unittest import mock
import requests
from src.api import todos_api

SUT_MODULE = "src.api.todos_api"



#### TESTS NOT USING pytest-mock (mocker)

@mock.patch(f'{SUT_MODULE}.requests.get')
def test_fetch_todo_returns_successful_response_without_mocker_1(mocked_dependency):
  # arrange
  response_body = { "id": 1, "userId": 1, "title": "ella", "completed": True }
  mocked_dependency.return_value.status_code = 200
  mocked_dependency.return_value.raise_for_status.return_value = None
  mocked_dependency.return_value.json.return_value = response_body

  # act
  result = todos_api.fetch_todo(1)

  # assert
  assert result == response_body
  mocked_dependency.return_value.raise_for_status.assert_called_once()
  mocked_dependency.assert_called_once_with("https://jsonplaceholder.typicode.com/todos/1", timeout=3)



def test_fetch_todo_returns_successful_response_without_mocker_2():
  with mock.patch(f'{SUT_MODULE}.requests.get') as mocked_dependency:
    # arrange
    response_body = { "id": 1, "userId": 1, "title": "ella", "completed": True }
    mocked_dependency.return_value.status_code = 200
    mocked_dependency.return_value.raise_for_status.return_value = None
    mocked_dependency.return_value.json.return_value = response_body

    # act
    result = todos_api.fetch_todo(1)

    # assert
    assert result == response_body
    mocked_dependency.return_value.raise_for_status.assert_called_once()
    mocked_dependency.assert_called_once_with("https://jsonplaceholder.typicode.com/todos/1", timeout=3)



#### TESTS USING pytest-mock (mocker)

def test_fetch_todo_returns_successful_response(mocker):
  # arrange
  response_body = { "id": 1, "userId": 1, "title": "ella", "completed": True }

  # OPTION 1 - no mock internal functions of mocked response
  # mocked_dependency = mocker.patch(
  #   f'{SUT_MODULE}.requests.get',
  #   return_value=mock.Mock(status_code=200, raise_for_status=lambda: None, json=lambda: response_body)
  # )

  # OPTION 2 - no mock internal functions of mocked response, separately
  # mocked_dependency = mocker.patch(f'{SUT_MODULE}.requests.get')
  # mocked_dependency.return_value = mock.Mock(status_code=200, raise_for_status=lambda: None, json=lambda: response_body)

  # OPTION 3 - mock everything
  mocked_dependency = mocker.patch(f'{SUT_MODULE}.requests.get')
  mocked_dependency.return_value.status_code = 200
  mocked_dependency.return_value.raise_for_status.return_value = None
  mocked_dependency.return_value.json.return_value = response_body

  # OPTION 4 - mock everything explicitly
  # mocked_response = mock.Mock(
  #   status_code=200,
  #   raise_for_status=mock.Mock(return_value=None),
  #   json = mock.Mock(return_value=response_body)
  # )
  # mocked_dependency = mocker.patch(f'{SUT_MODULE}.requests.get', return_value=mocked_response)

  # OPTION 5 - mock everything explicitly and separately
  # mocked_response = mock.Mock(status_code=200)
  # mocked_response.raise_for_status = mock.Mock(return_value=None)
  # mocked_response.json = mock.Mock(return_value=response_body)
  # mocked_dependency = mocker.patch(f'{SUT_MODULE}.requests.get', return_value=mocked_response)

  # OPTION 6 - mock everything using dictionary
  # mock_attrs = { 'status_code': 200, 'raise_for_status.return_value': None, 'json.return_value': response_body }
  # mocked_response = mock.Mock(**mock_attrs)
  # mocked_dependency = mocker.patch(f'{SUT_MODULE}.requests.get', return_value=mocked_response)

  # act
  result = todos_api.fetch_todo(1)

  # assert
  assert result == response_body
  mocked_dependency.return_value.raise_for_status.assert_called_once()
  mocked_dependency.assert_called_once_with("https://jsonplaceholder.typicode.com/todos/1", timeout=3)



def test_fetch_todo_returns_empty_object_when_fails(mocker):
  # arrange

  # OPTION 1 - no mock internal functions of mocked response
  # def do_exception():
  #   raise requests.exceptions.HTTPError()
  # mocked_dependency = mocker.patch(
  #   f'{SUT_MODULE}.requests.get',
  #   return_value=mock.Mock(status_code=500, raise_for_status=do_exception)
  # )

  # OPTION 2 - no mock internal functions of mocked response, separately
  # def do_exception():
  #   raise requests.exceptions.HTTPError()
  # mocked_dependency = mocker.patch(f'{SUT_MODULE}.requests.get')
  # mocked_dependency.return_value = mock.Mock(status_code=500, raise_for_status=do_exception)

  # OPTION 3 - mock everything
  mocked_dependency = mocker.patch(f'{SUT_MODULE}.requests.get')
  mocked_dependency.return_value.status_code = 500
  mocked_dependency.return_value.raise_for_status.side_effect = requests.exceptions.HTTPError

  # OPTION 4 - mock everything explicitly
  # mocked_response = mock.Mock(
  #   status_code=500,
  #   raise_for_status=mock.Mock(side_effect=requests.exceptions.HTTPError)
  # )
  # mocked_dependency = mocker.patch(f'{SUT_MODULE}.requests.get', return_value=mocked_response)

  # OPTION 5 - mock everything explicitly and separately
  # mocked_response = mock.Mock(status_code=500)
  # mocked_response.raise_for_status = mock.Mock(side_effect=requests.exceptions.HTTPError)
  # mocked_dependency = mocker.patch(f'{SUT_MODULE}.requests.get', return_value=mocked_response)

  # OPTION 6 - mock everything using dictionary
  # mock_attrs = { 'status_code': 500, 'raise_for_status.side_effect': requests.exceptions.HTTPError }
  # mocked_response = mock.Mock(**mock_attrs)
  # mocked_dependency = mocker.patch(f'{SUT_MODULE}.requests.get', return_value=mocked_response)

  #act
  result = todos_api.fetch_todo(1)

  # assert
  assert result == {}
  mocked_dependency.return_value.raise_for_status.assert_called_once()
  mocked_dependency.assert_called_once_with("https://jsonplaceholder.typicode.com/todos/1", timeout=3)
