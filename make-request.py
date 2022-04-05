import requests

# route 1 -- this is the ping pong route
def call_ping_route():
  r = requests.get('http://localhost:5000/ping') # make the request
  return r

# route 2 -- this is the random word route
def call_random_word_route():
  r = requests.get('http://localhost:5000/word')
  return r

# route 3 -- this is the string length route
def call_string_count():
  r = requests.post("http://localhost:5000/string-count",json ='antidisestablishmentarianism') # we have only the best words.
  return r


route_callers = [
  call_ping_route,
  call_random_word_route,
  call_string_count
  ]

for call_route in route_callers:
  r = call_route()
  r.status_code # first, check r for errors
  data = r.json()
  print(data) # print the response
