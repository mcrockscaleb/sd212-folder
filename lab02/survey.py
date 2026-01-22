# SD212 Survey lab

from flask import Flask, jsonify, request, render_template
import jinja2

app = Flask(__name__, template_folder='.')
app.jinja_env.undefined = jinja2.StrictUndefined

@app.route('/hello')
def hello():
    return "YOUR MESSAGE HERE\n"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=YOUR_PORT_HERE, debug=True, threaded=False)
