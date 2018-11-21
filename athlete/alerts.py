from flask import session


def set_alert(state=False, alert_type="danger", header="Danger:",
              message="You should not be seeing this"):
    session["alert"] = {}
    settings = session["alert"]
    settings["state"] = state
    settings["type"] = alert_type
    settings["header"] = header
    settings["message"] = message