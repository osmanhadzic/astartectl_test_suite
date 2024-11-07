# SPDX-FileCopyrightText: 2024 SECO Mind Srl
#
# SPDX-License-Identifier: Apache-2.0

import subprocess
import csv
from io import StringIO

from resources import (
    expected_output_object_csv,
    list_of_params_endpoints,
    list_of_nonparams_endpoints,
    list_of_keys,
    map_of_params_csv_data,
    map_of_nonparams_csv_data,
)


def test_get_sample_data_for_device_individual_parametric_datastream_csv(astarte_env_vars):
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
            "csv",
        ]
        sample_data_result = subprocess.run(arg_list, capture_output=True, text=True)

        samples_csv = sample_data_result.stdout
        csv_reader = csv.DictReader(StringIO(samples_csv))

        value = _parse_csv_to_sample_value(csv_reader)
        element = map_of_params_csv_data[path]

        assert value == element


def test_get_sample_data_for_device_individual_nonparametric_datastream_csv(astarte_env_vars):
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
            "csv",
        ]
        sample_data_result = subprocess.run(arg_list, capture_output=True, text=True)

        samples_csv = sample_data_result.stdout
        csv_reader = csv.DictReader(StringIO(samples_csv))

        value = _parse_csv_to_sample_value(csv_reader)

        element = map_of_nonparams_csv_data[path]

        assert value == element


def test_get_sample_data_for_device_object_parametric_datastream_csv(astarte_env_vars):
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
        "csv",
    ]
    sample_data_result = subprocess.run(arg_list, capture_output=True, text=True)
    sample_data = csv.DictReader(StringIO(sample_data_result.stdout))

    json_object = _map_sample_data_to_json(sample_data)

    assert json_object == expected_output_object_csv


def test_get_sample_data_for_device_object_nonparametric_datastream_csv(astarte_env_vars):
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
        "csv",
    ]
    sample_data_result = subprocess.run(arg_list, capture_output=True, text=True)
    sample_data = csv.DictReader(StringIO(sample_data_result.stdout))

    json_object = _map_sample_data_to_json(sample_data)

    assert json_object == expected_output_object_csv


def test_get_sample_data_for_server_individual_parametric_datastream_csv(astarte_env_vars):
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
            "csv",
        ]
        sample_data_result = subprocess.run(arg_list, capture_output=True, text=True)

        samples_csv = sample_data_result.stdout
        csv_reader = csv.DictReader(StringIO(samples_csv))

        value = _parse_csv_to_sample_value(csv_reader)
        element = map_of_params_csv_data[path]

        assert value == element


def test_get_sample_data_for_server_individual_nonparametric_datastream_csv(astarte_env_vars):
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
            "csv",
        ]
        sample_data_result = subprocess.run(arg_list, capture_output=True, text=True)

        samples_csv = sample_data_result.stdout
        csv_reader = csv.DictReader(StringIO(samples_csv))

        value = _parse_csv_to_sample_value(csv_reader)

        element = map_of_nonparams_csv_data[path]

        assert value == element


def _parse_csv_to_sample_value(csv_reader):
    samples_json = []
    for row in csv_reader:
        samples_json.append({"timestamp": row["Timestamp"], "value": row["Value"]})
    value = samples_json[0]["value"]
    return value


def _map_sample_data_to_json(sample_data):
    samples_json = []
    for row in sample_data:
        for key in list_of_keys:
            if key in row:
                samples_json.append({key: row[key]})
    return samples_json
