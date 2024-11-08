# SPDX-FileCopyrightText: 2024 SECO Mind Srl
#
# SPDX-License-Identifier: Apache-2.0


import subprocess

from resources import (
    list_of_params_endpoints,
    list_of_nonparams_endpoints,
    map_of_params_data,
    map_of_nonparams_data,
    list_of_nonparams_endpoints,
)


def test_app_engine_server_publish_datastream_individual_parametric_datastream(astarte_env_vars):
    device_id = astarte_env_vars["device_test_1"]
    astarte_url = astarte_env_vars["astarte_url"]
    realm = astarte_env_vars["realm"]
    jwt = astarte_env_vars["jwt"]

    interface_name = "test.astarte-platform.server.individual.parametric.Datastream"

    for path in list_of_params_endpoints:
        value = map_of_params_data[path]
        if type(value) is type([]):
            value = " ".join(value).replace(" ", ",")
        print(f"Stream data: {value}")
        arg_list = [
            "astartectl",
            "appengine",
            "devices",
            "publish-datastream",
            device_id,
            interface_name,
            path,
            value,
            "-t",
            jwt,
            "-u",
            astarte_url,
            "-r",
            realm,
        ]
        sample_data_result = subprocess.run(arg_list, capture_output=True, text=True)
        assert sample_data_result.stdout.replace("\n", "") == 'ok'


def test_app_engine_server_publish_datastream_individual_nonparametric_datastream(astarte_env_vars):
    device_id = astarte_env_vars["device_test_1"]
    astarte_url = astarte_env_vars["astarte_url"]
    realm = astarte_env_vars["realm"]
    jwt = astarte_env_vars["jwt"]

    interface_name = "test.astarte-platform.server.individual.nonparametric.Datastream"

    for path in list_of_nonparams_endpoints:
        value = map_of_nonparams_data[path]
        if type(value) is type([]):
            value = " ".join(value).replace(" ", ",")
        print(f"Stream data: {value}")
        arg_list = [
            "astartectl",
            "appengine",
            "devices",
            "publish-datastream",
            device_id,
            interface_name,
            path,
            value,
            "-t",
            jwt,
            "-u",
            astarte_url,
            "-r",
            realm,
        ]
        sample_data_result = subprocess.run(arg_list, capture_output=True, text=True)
        assert sample_data_result.stdout.replace("\n", "") == 'ok'
