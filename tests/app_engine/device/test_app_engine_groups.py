# SPDX-FileCopyrightText: 2024 SECO Mind Srl
#
# SPDX-License-Identifier: Apache-2.0


import subprocess

from resources import mygroup


def test_app_engine_group_create(astarte_env_vars):
    astarte_url = astarte_env_vars["astarte_url"]
    realm = astarte_env_vars["realm"]
    jwt = astarte_env_vars["jwt"]
    device_test_1 = astarte_env_vars["device_test_1"]

    arg_list = [
        "astartectl",
        "appengine",
        "groups",
        "create",
        mygroup,
        device_test_1,
        "-t",
        jwt,
        "-u",
        astarte_url,
        "-r",
        realm,
    ]

    sample_data_result = subprocess.run(arg_list, capture_output=True, text=True)
    assert sample_data_result.stdout.replace("\n", "") == "ok"


def test_app_engine_group_list(astarte_env_vars):
    astarte_url = astarte_env_vars["astarte_url"]
    realm = astarte_env_vars["realm"]
    jwt = astarte_env_vars["jwt"]

    arg_list = [
        "astartectl",
        "appengine",
        "groups",
        "list",
        "-t",
        jwt,
        "-u",
        astarte_url,
        "-r",
        realm,
    ]

    sample_data_result = subprocess.run(arg_list, capture_output=True, text=True)
    sample_data_result.stdout = _replace_brackets_from_string(sample_data_result.stdout)
    assert sample_data_result.stdout in mygroup


def test_app_engine_group_devices_list(astarte_env_vars):
    astarte_url = astarte_env_vars["astarte_url"]
    realm = astarte_env_vars["realm"]
    jwt = astarte_env_vars["jwt"]
    device_test_1 = astarte_env_vars["device_test_1"]

    arg_list = [
        "astartectl",
        "appengine",
        "groups",
        "devices",
        "list",
        mygroup,
        "-t",
        jwt,
        "-u",
        astarte_url,
        "-r",
        realm,
    ]

    sample_data_result = subprocess.run(arg_list, capture_output=True, text=True)
    sample_data_result.stdout = _replace_brackets_from_string(sample_data_result.stdout)
    assert sample_data_result.stdout in device_test_1


def test_app_engine_group_add_device(astarte_env_vars):
    astarte_url = astarte_env_vars["astarte_url"]
    realm = astarte_env_vars["realm"]
    jwt = astarte_env_vars["jwt"]
    device_test_2 = astarte_env_vars["device_test_2"]

    arg_list = [
        "astartectl",
        "appengine",
        "groups",
        "devices",
        "add",
        mygroup,
        device_test_2,
        "-t",
        jwt,
        "-u",
        astarte_url,
        "-r",
        realm,
    ]

    sample_data_result = subprocess.run(arg_list, capture_output=True, text=True)
    print(sample_data_result.stdout)
    assert sample_data_result.stdout.replace("\n", "") == "ok"


def test_app_engine_group_remove_device(astarte_env_vars):
    astarte_url = astarte_env_vars["astarte_url"]
    realm = astarte_env_vars["realm"]
    jwt = astarte_env_vars["jwt"]
    device_test_2 = astarte_env_vars["device_test_2"]

    arg_list = [
        "astartectl",
        "appengine",
        "groups",
        "devices",
        "remove",
        mygroup,
        device_test_2,
        "-t",
        jwt,
        "-u",
        astarte_url,
        "-r",
        realm,
    ]

    sample_data_result = subprocess.run(arg_list, capture_output=True, text=True)
    print(sample_data_result.stdout)
    assert sample_data_result.stdout.replace("\n", "") == "ok"


def _replace_brackets_from_string(input_string):
    return input_string.replace("\n", "").replace("[", "").replace("]", "")
