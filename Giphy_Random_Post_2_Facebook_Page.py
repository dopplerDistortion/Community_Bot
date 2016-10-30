import facebook
import safygiphy
import json
from pprint import pprint

def main():
  g = safygiphy.Giphy()
  r = g.random(tag="bot")
  img = r["data"]["image_original_url"]

  # Fill in the values noted in previous steps here
  cfg = {
    "page_id"      : "",
    "access_token" : "" 
    }

  api = get_api(cfg)
  atc = {
     'name': '',
     'link': img,
     'caption': '',
     'description': '',
     'picture': img
}
  msg = "Hello World! #randomposts"
  status = api.put_wall_post(message=msg, attachment=atc)

def get_api(cfg):
  graph = facebook.GraphAPI(cfg['access_token'])
  return graph


if __name__ == "__main__":
  main()
