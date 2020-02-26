"""Run this file to test the app!"""

from App import app

if __name__ == '__main__':
    app.run(host='192.168.111.20', port=8080, debug=True)
    # app.run(host='127.0.0.1', port=80)
