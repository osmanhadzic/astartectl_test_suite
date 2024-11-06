# SPDX-FileCopyrightText: 2024 SECO Mind Srl
#
# SPDX-License-Identifier: Apache-2.0

import subprocess
import json

from resources import (
    list_of_params_endpoints,
    list_of_nonparams_endpoints,
    map_of_nonparams_json_data,
    map_of_params_json_data,
)


def test_get_sample_data_for_device_individual_parametric_datastream_json(astarte_env_vars):
    device_id = astarte_env_vars["device_test_1"]
    astarte_url = astarte_env_vars["astarte_url"]
    realm = astarte_env_vars["realm"]
    jwt = astarte_env_vars["jwt"]

    interface_name = "test.astarte-platform.device.individual.parametric.Datastream"

    for path in list_of_params_endpoints:
        arg_list = [
            "astartectl",
            "appengine",
            "devices",
            "get-samples",
            device_id,
            interface_name,
            path,
            "-t",
            jwt,
            "-u",
            astarte_url,
            "-r",
            realm,
            "-o",
            "json",
        ]
        sample_data_result = subprocess.run(arg_list, capture_output=True, text=True)
        samples_json = json.loads(sample_data_result.stdout)
        value = samples_json[0]["value"]
        assert value == map_of_params_json_data[path]


def test_get_sample_data_for_device_individual_nonparametric_datastream_json(astarte_env_vars):
    device_id = astarte_env_vars["device_test_1"]
    astarte_url = astarte_env_vars["astarte_url"]
    realm = astarte_env_vars["realm"]
    jwt = astarte_env_vars["jwt"]

    interface_name = "test.astarte-platform.device.individual.nonparametric.Datastream"

    for path in list_of_nonparams_endpoints:
        arg_list = [
            "astartectl",
            "appengine",
            "devices",
            "get-samples",
            device_id,
            interface_name,
            path,
            "-t",
            jwt,
            "-u",
            astarte_url,
            "-r",
            realm,
            "-o",
            "json",
        ]
        sample_data_result = subprocess.run(arg_list, capture_output=True, text=True)
        samples_json = json.loads(sample_data_result.stdout)
        value = samples_json[0]["value"]
        assert value == map_of_nonparams_json_data[path]


def test_get_sample_data_for_device_object_parametric_datastream_json(astarte_env_vars):
    device_id = astarte_env_vars["device_test_1"]
    astarte_url = astarte_env_vars["astarte_url"]
    realm = astarte_env_vars["realm"]
    jwt = astarte_env_vars["jwt"]

    interface_name = "test.astarte-platform.device.object.parametric.Datastream"
    path = "/a"

    arg_list = [
        "astartectl",
        "appengine",
        "devices",
        "get-samples",
        device_id,
        interface_name,
        path,
        "-t",
        jwt,
        "-u",
        astarte_url,
        "-r",
        realm,
        "-o",
        "json",
    ]
    sample_data_result = subprocess.run(arg_list, capture_output=True, text=True)
    samples_json = json.loads(sample_data_result.stdout)

    json_data = _remove_path_from_map(map_of_params_json_data, "/a/")
    for data in json_data:
        assert samples_json[0]["Values"][data] == json_data[data]


def test_get_sample_data_for_device_object_nonparametric_datastream_json(astarte_env_vars):
    device_id = astarte_env_vars["device_test_1"]
    astarte_url = astarte_env_vars["astarte_url"]
    realm = astarte_env_vars["realm"]
    jwt = astarte_env_vars["jwt"]

    interface_name = "test.astarte-platform.device.object.nonparametric.Datastream"
    path = "/the"

    arg_list = [
        "astartectl",
        "appengine",
        "devices",
        "get-samples",
        device_id,
        interface_name,
        path,
        "-t",
        jwt,
        "-u",
        astarte_url,
        "-r",
        realm,
        "-o",
        "json",
    ]
    sample_data_result = subprocess.run(arg_list, capture_output=True, text=True)
    samples_json = json.loads(sample_data_result.stdout)
    json_data = _remove_path_from_map(map_of_nonparams_json_data, "/the/")
    for data in json_data:
        assert samples_json[0]["Values"][data] == json_data[data]


def test_get_sample_data_for_server_individual_parametric_datastream_json(astarte_env_vars):
    device_id = astarte_env_vars["device_test_1"]
    astarte_url = astarte_env_vars["astarte_url"]
    realm = astarte_env_vars["realm"]
    jwt = astarte_env_vars["jwt"]

    interface_name = "test.astarte-platform.server.individual.parametric.Datastream"

    for path in list_of_params_endpoints:
        arg_list = [
            "astartectl",
            "appengine",
            "devices",
            "get-samples",
            device_id,
            interface_name,
            path,
            "-t",
            jwt,
            "-u",
            astarte_url,
            "-r",
            realm,
            "-o",
            "json",
        ]
        sample_data_result = subprocess.run(arg_list, capture_output=True, text=True)
        samples_json = json.loads(sample_data_result.stdout)
        value = samples_json[0]["value"]
        assert value == map_of_params_json_data[path]


def test_get_sample_data_for_server_individual_nonparametric_datastream_json(astarte_env_vars):
    device_id = astarte_env_vars["device_test_1"]
    astarte_url = astarte_env_vars["astarte_url"]
    realm = astarte_env_vars["realm"]
    jwt = astarte_env_vars["jwt"]

    interface_name = "test.astarte-platform.server.individual.nonparametric.Datastream"

    for path in list_of_nonparams_endpoints:
        arg_list = [
            "astartectl",
            "appengine",
            "devices",
            "get-samples",
            device_id,
            interface_name,
            path,
            "-t",
            jwt,
            "-u",
            astarte_url,
            "-r",
            realm,
            "-o",
            "json",
        ]
        sample_data_result = subprocess.run(arg_list, capture_output=True, text=True)
        samples_json = json.loads(sample_data_result.stdout)
        value = samples_json[0]["value"]
        assert value == map_of_nonparams_json_data[path]


def _remove_path_from_map(map_of_nonparams_json_data, path):
    return {key.replace(path, ""): value for key, value in map_of_nonparams_json_data.items()}
