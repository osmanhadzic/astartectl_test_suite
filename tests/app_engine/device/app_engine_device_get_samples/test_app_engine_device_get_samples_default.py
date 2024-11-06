# SPDX-FileCopyrightText: 2024 SECO Mind Srl
#
# SPDX-License-Identifier: Apache-2.0

import subprocess
import re
import ast

from resources import (
    expected_output_object,
    list_of_params_endpoints,
    list_of_nonparams_endpoints,
    map_of_params_data,
    map_of_nonparams_data,
)


def test_get_sample_data_for_device_individual_parametric_datastream(astarte_env_vars):
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
        ]
        sample_data_result = subprocess.run(arg_list, capture_output=True, text=True)
        sample_data_result.stdout = _remove_table_border(sample_data_result)

        assert sample_data_result.stdout != ""

        sample_data_result.stdout = _normalize_and_split(sample_data_result.stdout)

        parsed_elements_list = _extract_elements_from_brackets(sample_data_result.stdout)

        list_length = len(sample_data_result.stdout) - 1

        if parsed_elements_list != []:
            assert parsed_elements_list == map_of_params_data[path]
        else:
            assert sample_data_result.stdout[list_length] == map_of_params_data[path]


def test_get_sample_data_for_device_individual_nonparametric_datastream(astarte_env_vars):
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
        ]
        sample_data_result = subprocess.run(arg_list, capture_output=True, text=True)
        sample_data_result.stdout = _remove_table_border(sample_data_result)

        assert sample_data_result.stdout != ""

        sample_data_result.stdout = _normalize_and_split(sample_data_result.stdout)

        parsed_elements_list = _extract_elements_from_brackets(sample_data_result.stdout)

        list_length = len(sample_data_result.stdout) - 1

        if parsed_elements_list != []:
            assert parsed_elements_list == map_of_nonparams_data[path]
        else:
            assert sample_data_result.stdout[list_length] == map_of_nonparams_data[path]


def test_get_sample_data_for_device_object_nonparametric_datastream(astarte_env_vars):
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
    ]
    sample_data_result = subprocess.run(arg_list, capture_output=True, text=True)
    sample_data_result.stdout = _remove_table_border(sample_data_result)

    sample_data_result.stdout = _normalize_and_split(sample_data_result.stdout)

    assert sample_data_result.stdout == expected_output_object


def test_get_sample_data_for_device_object_parametric_datastream(astarte_env_vars):
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
    ]
    sample_data_result = subprocess.run(arg_list, capture_output=True, text=True)
    sample_data_result.stdout = _remove_table_border(sample_data_result)

    sample_data_result.stdout = _normalize_and_split(sample_data_result.stdout)

    assert sample_data_result.stdout == expected_output_object


def test_get_sample_data_for_server_individual_parametric_datastream(astarte_env_vars):
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
        ]
        sample_data_result = subprocess.run(arg_list, capture_output=True, text=True)
        sample_data_result.stdout = _remove_table_border(sample_data_result)

        assert sample_data_result.stdout != ""

        sample_data_result.stdout = _normalize_and_split(sample_data_result.stdout)

        parsed_elements_list = _extract_elements_from_brackets(sample_data_result.stdout)

        list_length = len(sample_data_result.stdout) - 1

        if parsed_elements_list != []:
            assert parsed_elements_list == map_of_params_data[path]
        else:
            assert sample_data_result.stdout[list_length] == map_of_params_data[path]


def test_get_sample_data_for_server_individual_nonparametric_datastream(astarte_env_vars):
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
        ]
        sample_data_result = subprocess.run(arg_list, capture_output=True, text=True)
        sample_data_result.stdout = _remove_table_border(sample_data_result)

        assert sample_data_result.stdout != ""

        sample_data_result.stdout = _normalize_and_split(sample_data_result.stdout)

        parsed_elements_list = _extract_elements_from_brackets(sample_data_result.stdout)

        list_length = len(sample_data_result.stdout) - 1

        if parsed_elements_list != []:
            assert parsed_elements_list == map_of_nonparams_data[path]
        else:
            assert sample_data_result.stdout[list_length] == map_of_nonparams_data[path]


def _remove_table_border(table):
    table = table.stdout.replace("\n", "")

    table = "".join(ch for ch in table if not (9472 <= ord(ch) <= 9584))
    return table


def _parse_element(element):
    element = element.strip()
    if element.startswith("[") and element.endswith("]"):
        return ast.literal_eval(element)
    return element


def _extract_elements_from_brackets(sample_data_result):
    parsed_elements_list = []
    for element in sample_data_result:
        if element.startswith("["):
            parsed_elements_list.append(element.replace("[", ""))
        elif element.endswith("]"):
            parsed_elements_list.append(element.replace("]", ""))
    return parsed_elements_list


def _normalize_and_split(sample_data_result):
    sample_data_result = re.sub(r"\s+", " ", sample_data_result).strip()
    sample_data_result = sample_data_result.replace(" ", ",").split(",")
    sample_data_result = [_parse_element(el) for el in sample_data_result]
    return sample_data_result
