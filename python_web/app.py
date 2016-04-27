from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html');

@app.route('/ajax', methods=['POST'])
def ajax():
    if(request.form['data'] == 'test'):
        return 'do something'

    elif(request.form['data'] == 'test2'):
        return 'do something else'

    return 'invalid command'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
