from flask import Flask, render_template
import requests
application = Flask(__name__)

uri = 'http://hub-controller-live-hub-controller.apps-9d00.generic.opentlc.com/api/robot'

@application.route('/')
def index():
    return render_template('./index.html', hubcontrol = uri)

@application.route('/run')
def run():
    response = requests.get(uri + '/power')
    if response.status_code != 200:
    # This means something went wrong.
        raise ApiError('GET /power {}'.format(response.status_code))
     # Example GET invokation of the Robot API       
     #response = requests.get(uri + '/distance')  
        
     # Example POST invokation of the Robot API       
     #response = requests.get(uri + '/forward/5'
    return response.text    

    
@application.route('/status')
def status():
    response = requests.get(uri + '/status')
    if response.status_code != 200:
    # This means something went wrong.
        raise ApiError('GET /status {}'.format(response.status_code))
    return response.text

if __name__ == '__main__':
   application.run()
