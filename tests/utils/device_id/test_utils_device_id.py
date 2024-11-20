# SPDX-FileCopyrightText: 2024 SECO Mind Srl
#
# SPDX-License-Identifier: Apache-2.0


import base64
import subprocess


def test_utils_generate_and_validate_device_id(astarte_env_vars):
    astarte_url = astarte_env_vars["astarte_url"]
    jwt = astarte_env_vars["jwt"]

    arg_list_generate = [
        "astartectl",
        "utils",
        "device-id",
        "generate-random",
        "-t",
        jwt,
        "-u",
        astarte_url,
    ]

    sample_data_result = subprocess.run(arg_list_generate, capture_output=True, text=True)
    device_id = sample_data_result.stdout.replace("\n", "")

    arg_list_validate = [
        "astartectl",
        "utils",
        "device-id",
        "validate",
        device_id,
        "-t",
        jwt,
        "-u",
        astarte_url,
    ]

    sample_data_result = subprocess.run(arg_list_validate, capture_output=True, text=True)
    assert sample_data_result.stdout.replace("\n", "") == "Valid"


def test_utils_to_uuid_and_from_uuid(astarte_env_vars):
    astarte_url = astarte_env_vars["astarte_url"]
    jwt = astarte_env_vars["jwt"]
    device_test_1 = astarte_env_vars["device_test_1"]

    arg_list_to_uuid = [
        "astartectl",
        "utils",
        "device-id",
        "to-uuid",
        device_test_1,
        "-t",
        jwt,
        "-u",
        astarte_url,
    ]

    sample_data_result = subprocess.run(arg_list_to_uuid, capture_output=True, text=True)
    to_uuid_result = sample_data_result.stdout.replace("\n", "")

    arg_list_from_uuid = [
        "astartectl",
        "utils",
        "device-id",
        "from-uuid",
        to_uuid_result,
        "-t",
        jwt,
        "-u",
        astarte_url,
    ]

    sample_data_result = subprocess.run(arg_list_from_uuid, capture_output=True, text=True)
    assert sample_data_result.stdout.replace("\n", "") == device_test_1


def test_utils_compute_from_string_and_from_bytes(astarte_env_vars):
    astarte_url = astarte_env_vars["astarte_url"]
    jwt = astarte_env_vars["jwt"]
    namespace_uuid = "f79ad91f-c638-4889-ae74-9d001a3b4cf8"
    string_data = "myidentifierdata"

    arg_list_from_string = [
        "astartectl",
        "utils",
        "device-id",
        "compute-from-string",
        namespace_uuid,
        string_data,
        "-t",
        jwt,
        "-u",
        astarte_url,
    ]

    sample_data_result = subprocess.run(arg_list_from_string, capture_output=True, text=True)
    from_string_result = sample_data_result.stdout.replace("\n", "")

    string_data = string_data.encode("utf-8")
    base64_encoded_data = base64.b64encode(string_data).decode("utf-8")

    arg_list_from_bytes = [
        "astartectl",
        "utils",
        "device-id",
        "compute-from-bytes",
        namespace_uuid,
        base64_encoded_data,
        "-t",
        jwt,
        "-u",
        astarte_url,
    ]
    sample_data_result = subprocess.run(arg_list_from_bytes, capture_output=True, text=True)
    assert sample_data_result.stdout.replace("\n", "") == from_string_result
