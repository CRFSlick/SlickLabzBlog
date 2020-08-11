from App.modules.helpers.helpers import determine_slash_type
from App.modules.log.log import Log
from flask import render_template
from flask import request
from App import app

worthless_var = None


class APIError(Exception):

    def __init__(self, code, name, description):
        self.code = code
        self.name = name
        self.description = description


@app.errorhandler(400)
@app.errorhandler(401)
@app.errorhandler(403)
@app.errorhandler(404)
@app.errorhandler(405)
@app.errorhandler(406)
@app.errorhandler(408)
@app.errorhandler(409)
@app.errorhandler(410)
@app.errorhandler(411)
@app.errorhandler(412)
@app.errorhandler(413)
@app.errorhandler(414)
@app.errorhandler(415)
@app.errorhandler(416)
@app.errorhandler(417)
@app.errorhandler(428)
@app.errorhandler(429)
@app.errorhandler(431)
@app.errorhandler(500)
@app.errorhandler(501)
@app.errorhandler(502)
@app.errorhandler(503)
@app.errorhandler(504)
@app.errorhandler(505)
@app.errorhandler(APIError)
def page_not_found(e):

    # Log an internal server error
    if e.code == 500:
        slash = determine_slash_type()
        log_path = f'{app.root_path}{slash}data{slash}log{slash}'
        Log(directory=log_path).out(f'Cod: {e.code} | Path: {request.path}', level='error')

    # Handle error
    return render_template('error.html', page_title=e.code, code=e.code, name=e.name, description=e.description), e.code
