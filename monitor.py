
from time import sleep
import sys

def vital_alert(message):
  print(message)
  for i in range(6):
      print('\r* ', end='')
      sys.stdout.flush()
      sleep(1)
      print('\r *', end='')
      sys.stdout.flush()
      sleep(1)

def vitals_ok(temperature, pulseRate, spo2):
  if temperature > 102 or temperature < 95:
   vital_alert('Temperature critical!')
    return False
  elif pulseRate < 60 or pulseRate > 100:
    vital_alert('Pulse Rate is out of range!')
    return False
  elif spo2 < 90:
    vital_alert('Oxygen Saturation out of range!')
    return False
  return True
  