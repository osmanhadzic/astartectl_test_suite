# SPDX-FileCopyrightText: 2024 SECO Mind Srl
#
# SPDX-License-Identifier: Apache-2.0


import subprocess


def test_pairing_agent_register(astarte_env_vars):
    astarte_url = astarte_env_vars["astarte_url"]
    realm = astarte_env_vars["realm"]
    jwt = astarte_env_vars["jwt"]
    device_test_2 = astarte_env_vars["device_test_2"]

    arg_list = [
        "astartectl",
        "pairing",
        "agent",
        "register",
        device_test_2,
        "-t",
        jwt,
        "-u",
        astarte_url,
        "-r",
        realm,
    ]
    sample_data_result = subprocess.run(arg_list, capture_output=True, text=True)
    assert "successfully registered" in sample_data_result.stdout


def test_pairing_agent_unregister(astarte_env_vars):
    astarte_url = astarte_env_vars["astarte_url"]
    realm = astarte_env_vars["realm"]
    jwt = astarte_env_vars["jwt"]
    device_test_2 = astarte_env_vars["device_test_2"]

    arg_list = [
        "astartectl",
        "pairing",
        "agent",
        "unregister",
        device_test_2,
        "-t",
        jwt,
        "-u",
        astarte_url,
        "-r",
        realm,
    ]
    sample_data_result = subprocess.run(arg_list, capture_output=True, text=True, input="y\n")
    assert "ok" in sample_data_result.stdout
