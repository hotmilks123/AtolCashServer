from flask import Flask
from flask_restful import Api, Resource, reqparse
import LetsStart
import index
app = Flask(__name__)
api = Api(app)

@app.route("/open/<state>")
def opendevice(state):
    LetsStart.DeviceConnection(state)
    return 'Device Connected'
            
@app.route("/openshift/<state>")
def openshift(state):
    s = LetsStart.DeviceConnection(state)
    s.OpenShift()
    return 'Device Connected'

@app.route("/closeshift/<state>")
def closeshift(state):
    s = LetsStart.DeviceConnection(state)
    s.OpenShift()
    return 'Device Connected'

@app.route("/xreport/<state>")
def xreport(state):
    s = LetsStart.DeviceConnection(state)
    s.xreport()
    return 'Device Connected'


if __name__ == '__main__':
    app.run(debug=True)