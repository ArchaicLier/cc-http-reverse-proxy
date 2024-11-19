"""Flask server for computercraft."""

from pathlib import Path

from flask import Flask, Response, request
from werkzeug.exceptions import HTTPException

import proxy_server

MODULE_PATH = Path(proxy_server.__file__).parent.absolute()
LUA_PATH = MODULE_PATH.joinpath("lua")

cc_server = Flask("cc_server")

@cc_server.route("/installer")
def installer() -> Response:
    """Download installer.lua."""
    installer_template_path = LUA_PATH.joinpath("installer.lua")
    if not installer_template_path.is_file():
        msg = "Installer template not found."
        raise HTTPException(msg, Response(msg, 404))

    with installer_template_path.open() as file:
        installer = file.read()
        installer = installer.replace("{SERVER_ADDRESS}", request.host_url)

    return Response(installer)

@cc_server.route("/get_runner")
def get_runner() -> Response:
    """Get new runner."""
    runner_path = LUA_PATH.joinpath("runner.lua")
    if not runner_path.is_file():
        msg = "Runner not found"
        raise HTTPException(msg, Response(msg, 404))

    with runner_path.open() as file:
        runner = file.read()

    return Response(runner)
