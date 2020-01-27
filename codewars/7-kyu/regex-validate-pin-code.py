def validate_pin(pin):
    if len(pin) in [4, 6]:
      try:
        [int(i) for i in pin]
        return True
      except:
        pass
    return False
