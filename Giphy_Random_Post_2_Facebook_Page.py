import facebook
import safygiphy
import json
import datetime
import time
from pprint import pprint

now1 = datetime.datetime.now()
s = int(now1.hour)
d = int(now1.minute)
ss = int(now1.second) + 1

def todayAt(hr, min=0, sec=0, micros=0):
    now = datetime.datetime.now()
    return now.replace(hour=hr, minute=min, second=sec, microsecond=micros)

def post():
  g = safygiphy.Giphy()
  r = g.random(tag="science")
  img = r["data"]["image_original_url"]

  # Fill in the values noted in previous steps here
  cfg = {
    "page_id"      : "****",  # page id in about page
    "access_token" : "****"
    }

  api = get_api(cfg)
  atc = {
     'name': '',
     'link': img,
     'caption': '',
     'description': '',
     'picture': img
}
  msg = ":D #random #giphy" #post
  status = api.put_wall_post(message=msg, attachment=atc)

def get_api(cfg):
  graph = facebook.GraphAPI(cfg['access_token'])
  return graph


if __name__ == "__main__":
  post()
  print "posted"
  exit(0)
