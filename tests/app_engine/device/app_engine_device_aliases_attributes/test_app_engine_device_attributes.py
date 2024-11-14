# SPDX-FileCopyrightText: 2024 SECO Mind Srl
#
# SPDX-License-Identifier: Apache-2.0

import subprocess

from resources import list_of_attributes


def test_app_engine_device_attributes_set(astarte_env_vars):
    device_id = astarte_env_vars["device_test_1"]
    astarte_url = astarte_env_vars["astarte_url"]
    realm = astarte_env_vars["realm"]
    jwt = astarte_env_vars["jwt"]

    for attribute in list_of_attributes:
        arg_list = [
            "astartectl",
            "appengine",
            "devices",
            "attributes",
            "set",
            device_id,
            list_of_attributes[attribute],
            "-t",
            jwt,
            "-u",
            astarte_url,
            "-r",
            realm,
        ]
        attributes_add_result = subprocess.run(arg_list, capture_output=True, text=True)
        assert attributes_add_result.stdout.replace("\n", "") == "ok"


def test_app_engine_device_atributes_list(astarte_env_vars):
    device_id = astarte_env_vars["device_test_1"]
    astarte_url = astarte_env_vars["astarte_url"]
    realm = astarte_env_vars["realm"]
    jwt = astarte_env_vars["jwt"]

    arg_list = [
        "astartectl",
        "appengine",
        "devices",
        "attributes",
        "list",
        device_id,
        "-t",
        jwt,
        "-u",
        astarte_url,
        "-r",
        realm,
    ]
    attributes_result = subprocess.run(arg_list, capture_output=True, text=True)
    attributes_result = (
        attributes_result.stdout.replace("map[", "").replace("]", "").replace("\n", "")
    )

    for attribute in list_of_attributes:
        assert attribute in attributes_result


def test_app_engine_device_attributes_remove(astarte_env_vars):
    device_id = astarte_env_vars["device_test_1"]
    astarte_url = astarte_env_vars["astarte_url"]
    realm = astarte_env_vars["realm"]
    jwt = astarte_env_vars["jwt"]

    for attribute in list_of_attributes:
        print(attribute)
        arg_list = [
            "astartectl",
            "appengine",
            "devices",
            "attributes",
            "remove",
            device_id,
            attribute,
            "-t",
            jwt,
            "-u",
            astarte_url,
            "-r",
            realm,
        ]
        attributes_delete_result = subprocess.run(arg_list, capture_output=True, text=True)
        assert attributes_delete_result.stdout.replace("\n", "") == "ok"
