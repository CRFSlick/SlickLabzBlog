from flask import render_template
from App import app

worthless_var = None


class APIError(Exception):

    def __init__(self, code, name, description):
        self.code = code
        self.name = name
        self.description = description

    # @property
    # def code(self):
    #     """
    #     Returns:
    #         code (str)
    #     """
    #     return self._code
    #
    # @code.setter
    # def code(self, value):
    #     """
    #     Sets:
    #         code (str)
    #     """
    #     self._code = value


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
    return render_template('error.html', title=e.code, code=e.code, name=e.name, description=e.description), e.code
