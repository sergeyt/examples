#!/usr/bin/env python3

import os
from subprocess import Popen, PIPE
import requests

from functools import wraps
from flask import Flask, request, jsonify, Response

app = Flask(__name__)
app.debug = True


@app.route('/api/test')
def get_configs():
    process = Popen(["docker", "exec", "core", "/core/sample_app"],
                    stdout=PIPE)
    (output, err) = process.communicate()
    exit_code = process.wait()
    return output


if __name__ == '__main__':
    app.run(host='0.0.0.0')
