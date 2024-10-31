# SPDX-FileCopyrightText: 2024 SECO Mind Srl
#
# SPDX-License-Identifier: Apache-2.0

import subprocess


def test_get_sample_data_for_nonexisting_device(astarte_env_vars):
    device_id = "nonexisting_device"
    astarte_url = astarte_env_vars["astarte_url"]
    realm = astarte_env_vars["realm"]
    jwt = astarte_env_vars["jwt"]

    interface_name = "any_interface"
    path = "any_path"

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

    assert "Device not found" in sample_data_result.stderr


def test_get_sample_data_for_existing_device(astarte_env_vars):
    device_id = astarte_env_vars["device_test_1"]
    astarte_url = astarte_env_vars["astarte_url"]
    realm = astarte_env_vars["realm"]
    jwt = astarte_env_vars["jwt"]

    interface_name = "nonexisting_interface"
    path = "any_path"

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
    output = f"Device {device_id} has no interface named nonexisting_interface"
    assert output in sample_data_result.stderr


def test_get_sample_data_for_nonexisting_path(astarte_env_vars):
    device_id = astarte_env_vars["device_test_1"]
    astarte_url = astarte_env_vars["astarte_url"]
    realm = astarte_env_vars["realm"]
    jwt = astarte_env_vars["jwt"]

    interface_name = "test.astarte-platform.device.object.parametric.Datastream"
    path = "nonexisting_path"

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
    assert (
        "nonexisting_path does not match valid query paths for endpoint /%{parameter}/stringarray"
        in sample_data_result.stderr
    )
