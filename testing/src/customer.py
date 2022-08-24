from datetime import datetime

class Customer:
  def __init__(self, name, email):
    self.name = name
    self.email = email
    self.created_at = datetime.now()

  def __str__(self):
    return f"name: {self.name}, email: {self.email}"
