#!/usr/bin/env python

from flask import Flask, request, redirect, json, url_for, render_template
import xml.etree.ElementTree as ET
import requests

app = Flask(__name__)
tv = "http://[your tv ip address]:8060"

def get_apps():
    resp = requests.get(tv + "/query/apps")
    root = ET.fromstring(resp.content)
    apps = {child.text.lower().strip().rstrip(): child.attrib.get('id') for child in root}
    return apps

def get_favs():
    app_dict = get_apps()
    favorites = []
    with open('favorites.json', 'r') as f:
        favs = json.loads(f.read())
    myfavs = [{'name': fav, 'id': app_dict.get(fav.lower().strip().rstrip())} for fav in favs]
    for item in myfavs:
        if item.get('id') is None:
            for appl in app_dict.keys():
                if item.get('name') in appl:
                    favorites.append({'name': item.get('name'), 'id': app_dict.get(appl)})
                    continue
        else:
            favorites.append({'name': item.get('name'), 'id': item.get('id')})
    return favorites

@app.route("/")
def index():
    app_dict = get_apps()
    apps = [{"name": appl, "id": app_dict.get(appl)} for appl in app_dict.keys()]
    return render_template('index.html', tvurl=tv, apps=apps)

@app.route("/launch", methods=['POST'])
def launcher():
    appid = request.form['appid']
    resp = requests.post(tv + "/launch/" + appid)
    return redirect(url_for("controller"))

@app.route("/controller")
def controller():
    favorites = get_favs()
    return render_template("controller.html", tvurl=tv, favorites=favorites)


if __name__ == "__main__":
    app.run()
