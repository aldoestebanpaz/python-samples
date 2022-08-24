import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

def fetch_todo(todo_id):
  result_dict = {}
  try:
    res = requests.get(f'{BASE_URL}/todos/{todo_id}', timeout=3)
    res.raise_for_status()
    result_dict = res.json()
  except requests.exceptions.HTTPError as errh:
    print("Http Error:", errh)
  except requests.exceptions.ConnectionError as errc:
    print("Error Connecting:", errc)
  except requests.exceptions.Timeout as errt:
    print("Timeout Error:", errt)
  except requests.exceptions.RequestException as err:
    print("OOps: Something Else", err)

  return result_dict
