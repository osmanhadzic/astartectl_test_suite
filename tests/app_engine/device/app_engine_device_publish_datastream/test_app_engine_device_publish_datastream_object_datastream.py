# SPDX-FileCopyrightText: 2024 SECO Mind Srl
#
# SPDX-License-Identifier: Apache-2.0


import subprocess
import json
import os


def test_app_engine_server_publish_datastream_object_parametric_datastream(astarte_env_vars):
    device_id = astarte_env_vars["device_test_1"]
    astarte_url = astarte_env_vars["astarte_url"]
    realm = astarte_env_vars["realm"]
    jwt = astarte_env_vars["jwt"]

    interface_name = "test.astarte-platform.server.object.parametric.Datastream"

    path = "/a"
    json_data = _read_json_data()

    arg_list = [
        "astartectl",
        "appengine",
        "devices",
        "publish-datastream",
        device_id,
        interface_name,
        path,
        json_data,
        "-t",
        jwt,
        "-u",
        astarte_url,
        "-r",
        realm,
    ]
    sample_data_result = subprocess.run(arg_list, capture_output=True, text=True)
    assert sample_data_result.stdout.replace("\n", "") == "ok"


def test_app_engine_server_publish_datastream_object_nonparametric_datastream(astarte_env_vars):
    device_id = astarte_env_vars["device_test_1"]
    astarte_url = astarte_env_vars["astarte_url"]
    realm = astarte_env_vars["realm"]
    jwt = astarte_env_vars["jwt"]

    interface_name = "test.astarte-platform.server.object.nonparametric.Datastream"

    path = "/the"
    json_data = _read_json_data()

    arg_list = [
        "astartectl",
        "appengine",
        "devices",
        "publish-datastream",
        device_id,
        interface_name,
        path,
        json_data,
        "-t",
        jwt,
        "-u",
        astarte_url,
        "-r",
        realm,
    ]
    sample_data_result = subprocess.run(arg_list, capture_output=True, text=True)
    assert sample_data_result.stdout.replace("\n", "") == "ok"


def _read_json_data():
    json_path = "json_object"
    current_dir = os.path.dirname(__file__)
    json_path = os.path.join(current_dir, f"{json_path}.json")
    with open(json_path, "r") as file:
        data = json.load(file)
    return json.dumps(data)
