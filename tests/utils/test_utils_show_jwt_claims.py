# SPDX-FileCopyrightText: 2024 SECO Mind Srl
#
# SPDX-License-Identifier: Apache-2.0

import os
import subprocess


def test_utils_show_jwt_all_claims(astarte_env_vars):

    jwt = astarte_env_vars["jwt"]

    arg_list = [
        "astartectl",
        "utils",
        "show-jwt-claims",
        jwt,
    ]

    sample_data_result = subprocess.run(arg_list, capture_output=True, text=True)
    expected_output = ["a_aea", "a_rma", "a_pa", "a_ch"]

    for claim in expected_output:
        assert claim in sample_data_result.stdout


def test_utils_show_jwt_appengine_claim(astarte_env_vars):
    realm = astarte_env_vars["realm"]
    private_key_dir = _get_private_key(realm)

    arg_gen_jwt_list = ["astartectl", "utils", "gen-jwt", "appengine", "-k", private_key_dir]
    token_data_result = subprocess.run(arg_gen_jwt_list, capture_output=True, text=True)
    token = token_data_result.stdout.strip()

    arg_gen_jwt_list = ["astartectl", "utils", "show-jwt-claims", token]
    sample_data_result = subprocess.run(arg_gen_jwt_list, capture_output=True, text=True)
    expected_output = "a_aea"

    assert expected_output in sample_data_result.stdout


def test_utils_show_jwt_realm_managment_claim(astarte_env_vars):
    realm = astarte_env_vars["realm"]
    private_key_dir = _get_private_key(realm)

    arg_gen_jwt_list = ["astartectl", "utils", "gen-jwt", "realm-management", "-k", private_key_dir]
    token_data_result = subprocess.run(arg_gen_jwt_list, capture_output=True, text=True)
    token = token_data_result.stdout.strip()

    arg_gen_jwt_list = ["astartectl", "utils", "show-jwt-claims", token]
    sample_data_result = subprocess.run(arg_gen_jwt_list, capture_output=True, text=True)
    expected_output = "a_rma"

    assert expected_output in sample_data_result.stdout


def test_utils_show_jwt_pairing_claim(astarte_env_vars):
    realm = astarte_env_vars["realm"]
    private_key_dir = _get_private_key(realm)

    arg_gen_jwt_list = ["astartectl", "utils", "gen-jwt", "pairing", "-k", private_key_dir]
    token_data_result = subprocess.run(arg_gen_jwt_list, capture_output=True, text=True)
    token = token_data_result.stdout.strip()

    arg_gen_jwt_list = ["astartectl", "utils", "show-jwt-claims", token]
    sample_data_result = subprocess.run(arg_gen_jwt_list, capture_output=True, text=True)
    expected_output = "a_pa"

    assert expected_output in sample_data_result.stdout


def test_utils_show_jwt_chanels_claim(astarte_env_vars):
    realm = astarte_env_vars["realm"]
    private_key_dir = _get_private_key(realm)

    arg_gen_jwt_list = ["astartectl", "utils", "gen-jwt", "channels", "-k", private_key_dir]
    token_data_result = subprocess.run(arg_gen_jwt_list, capture_output=True, text=True)
    token = token_data_result.stdout.strip()

    arg_gen_jwt_list = ["astartectl", "utils", "show-jwt-claims", token]
    sample_data_result = subprocess.run(arg_gen_jwt_list, capture_output=True, text=True)
    expected_output = "a_ch"

    assert expected_output in sample_data_result.stdout


def _get_private_key(realm_name):
    return os.path.realpath(f"{realm_name}_private.pem")
