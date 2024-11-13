# SPDX-FileCopyrightText: 2024 SECO Mind Srl
#
# SPDX-License-Identifier: Apache-2.0


import subprocess
import json


from resources import list_of_interface_names


def test_app_engine_device_list(astarte_env_vars):
    astarte_url = astarte_env_vars["astarte_url"]
    realm = astarte_env_vars["realm"]
    jwt = astarte_env_vars["jwt"]
    device_test_1 = astarte_env_vars["device_test_1"]

    arg_list = [
        "astartectl",
        "appengine",
        "devices",
        "list",
        "-t",
        jwt,
        "-u",
        astarte_url,
        "-r",
        realm,
    ]
    sample_data_result = subprocess.run(arg_list, capture_output=True, text=True)
    assert device_test_1 in sample_data_result.stdout


def test_app_engine_device_show(astarte_env_vars):
    astarte_url = astarte_env_vars["astarte_url"]
    realm = astarte_env_vars["realm"]
    jwt = astarte_env_vars["jwt"]
    device_test_1 = astarte_env_vars["device_test_1"]

    arg_list = [
        "astartectl",
        "appengine",
        "devices",
        "show",
        device_test_1,
        "-t",
        jwt,
        "-u",
        astarte_url,
        "-r",
        realm,
    ]
    sample_data_result = subprocess.run(arg_list, capture_output=True, text=True)

    assert device_test_1 in sample_data_result.stdout

    for key in list_of_interface_names:
        assert key in sample_data_result.stdout


def test_app_engine_device_data_snapshot(astarte_env_vars):
    astarte_url = astarte_env_vars["astarte_url"]
    realm = astarte_env_vars["realm"]
    jwt = astarte_env_vars["jwt"]
    device_test_1 = astarte_env_vars["device_test_1"]

    arg_list = [
        "astartectl",
        "appengine",
        "devices",
        "data-snapshot",
        device_test_1,
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

    json_value = json.loads(sample_data_result.stdout)

    for interface in list_of_interface_names:
        assert interface in json_value


def test_app_engine_stats_device(astarte_env_vars):
    astarte_url = astarte_env_vars["astarte_url"]
    realm = astarte_env_vars["realm"]
    jwt = astarte_env_vars["jwt"]

    arg_list = [
        "astartectl",
        "appengine",
        "stats",
        "device",
        "-t",
        jwt,
        "-u",
        astarte_url,
        "-r",
        realm,
    ]

    sample_data_result = subprocess.run(arg_list, capture_output=True, text=True)
    except_output = "{TotalDevices:1 ConnectedDevices:0}\n"
    assert sample_data_result.stdout == except_output
