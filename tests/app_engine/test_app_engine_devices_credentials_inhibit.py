# SPDX-FileCopyrightText: 2024 SECO Mind Srl
#
# SPDX-License-Identifier: Apache-2.0


import subprocess


def test_app_engine_device_credentials_inhibit(astarte_env_vars):
    astarte_url = astarte_env_vars["astarte_url"]
    realm = astarte_env_vars["realm"]
    jwt = astarte_env_vars["jwt"]
    device_test_1 = astarte_env_vars["device_test_1"]

    arg_list = [
        "astartectl",
        "appengine",
        "devices",
        "credentials",
        "inhibit",
        device_test_1,
        "true",
        "-t",
        jwt,
        "-u",
        astarte_url,
        "-r",
        realm,
    ]
    sample_data_result = subprocess.run(arg_list, capture_output=True, text=True)
    assert sample_data_result.stdout.replace("\n", "") == "ok"


def test_app_engine_device_credentials_inhibit(astarte_env_vars):
    astarte_url = astarte_env_vars["astarte_url"]
    realm = astarte_env_vars["realm"]
    jwt = astarte_env_vars["jwt"]
    device_test_1 = astarte_env_vars["device_test_1"]

    arg_list = [
        "astartectl",
        "appengine",
        "devices",
        "credentials",
        "inhibit",
        device_test_1,
        "false",
        "-t",
        jwt,
        "-u",
        astarte_url,
        "-r",
        realm,
    ]
    sample_data_result = subprocess.run(arg_list, capture_output=True, text=True)
    assert sample_data_result.stdout.replace("\n", "") == "ok"
