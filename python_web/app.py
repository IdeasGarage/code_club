from flask import Flask, render_template, request
import sys
sys.path = ['./lib'] + sys.path

from robot_arm import *


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html');

arm = robot_arm()

@app.route('/ajax', methods=['POST'])
 def ajax():
    if(request.form['data'] == 'test'):
        print 'my sister smells'
        
        arm.light_on()

        #Move arm timed takes a command, and time duration
        #                  Command                Time
        arm.move_arm_timed(BASE_COUNTERCLOCKWISE, 2)

        return 'do something'

    elif(request.form['data'] == 'test2'):
        arm.move_arm_timed(BASE_CLOCKWISE, 2)
        return 'do something else'

    return 'invalid command'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
