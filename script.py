class HashMap:
  def __init__(self, size):
    self.array_size = size
    self.array = [None for i in range(self.array_size)]

  def assign(self, key, value):
    hash_code = hash(key)
    array_index = self.compress(hash_code)
    self.array[array_index] = [key, value]

  def retrieve(self, key):
    hash_code = self.hash(key)
    array_index = self.compress(hash_code)
    payload = self.array[array_index]

    if payload is None or payload[0] != key:
      return None
    else:
      return payload[1]

  def hash(self, key):
    return sum(key.encode())

  def compress(self, hash_code):
    return hash_code % self.array_size
