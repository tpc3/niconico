import bottle
import requests

html = ""

with open("./og.html") as f:
    html = f.read()

@bottle.route("/<id>")
def get(id):
    response = requests.get("https://www.nicovideo.jp/api/watch/tmp/" + id + "?_frontendId=6&_frontendVersion=0.0.0", {"content-type": "application/json"})
    if response.status_code != 200:
        return bottle.HTTPResponse(status=500, body={"status": "response is not 200"})
    print(response.json())
    return bottle.template(html, id=id, response=response.json())
    
@bottle.route("/")
def index():
    bottle.redirect("/static/index.html")

@bottle.route("/watch_tmp/<id>")
def watch_tmp(id):
    bottle.redirect("/" + id)

@bottle.route('/static/<filename>')
def server_static(filename):
    return bottle.static_file(filename, root='./static')

bottle.run(host="0.0.0.0", port=8080)
