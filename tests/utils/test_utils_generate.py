# SPDX-FileCopyrightText: 2024 SECO Mind Srl
#
# SPDX-License-Identifier: Apache-2.0


import os
import subprocess
import jwt


def test_utils_gen_keypair(astarte_env_vars):
    realm = astarte_env_vars["realm"]

    arg_list = [
        "astartectl",
        "utils",
        "gen-keypair",
        realm,
    ]

    sample_data_result = subprocess.run(arg_list, capture_output=True, text=True)
    except_output = "Keypair generated successfully"
    assert except_output in sample_data_result.stdout


def test_utils_gen_jwt_all_realms(astarte_env_vars):

    realm = astarte_env_vars["realm"]
    private_key_dir = _get_private_key(realm)

    arg_list = ["astartectl", "utils", "gen-jwt", "all-realm-apis", "-k", private_key_dir]
    sample_data_result = subprocess.run(arg_list, capture_output=True, text=True)
    token = sample_data_result.stdout.strip()

    decoded_token = jwt.decode(token, options={"verify_signature": False})

    required_claims = ["a_aea", "a_rma", "a_pa", "a_ch"]

    for claim in required_claims:
        assert claim in decoded_token


def test_utils_gen_jwt_realm_managment(astarte_env_vars):

    realm = astarte_env_vars["realm"]
    private_key_dir = _get_private_key(realm)

    arg_list = ["astartectl", "utils", "gen-jwt", "realm-management", "-k", private_key_dir]
    sample_data_result = subprocess.run(arg_list, capture_output=True, text=True)
    token = sample_data_result.stdout.strip()

    decoded_token = jwt.decode(token, options={"verify_signature": False})
    required_claim = "a_rma"

    assert required_claim in decoded_token


def test_utils_gen_jwt_appengine(astarte_env_vars):

    realm = astarte_env_vars["realm"]
    private_key_dir = _get_private_key(realm)

    arg_list = ["astartectl", "utils", "gen-jwt", "appengine", "-k", private_key_dir]
    sample_data_result = subprocess.run(arg_list, capture_output=True, text=True)
    token = sample_data_result.stdout.strip()

    decoded_token = jwt.decode(token, options={"verify_signature": False})
    required_claim = "a_aea"

    assert required_claim in decoded_token


def test_utils_gen_jwt_pairing(astarte_env_vars):

    realm = astarte_env_vars["realm"]
    private_key_dir = _get_private_key(realm)

    arg_list = ["astartectl", "utils", "gen-jwt", "pairing", "-k", private_key_dir]
    sample_data_result = subprocess.run(arg_list, capture_output=True, text=True)
    token = sample_data_result.stdout.strip()

    decoded_token = jwt.decode(token, options={"verify_signature": False})
    required_claim = "a_pa"

    assert required_claim in decoded_token


def test_utils_gen_jwt_housekeeping(astarte_env_vars):

    realm = astarte_env_vars["realm"]
    private_key_dir = _get_private_key(realm)

    arg_list = ["astartectl", "utils", "gen-jwt", "housekeeping", "-k", private_key_dir]
    sample_data_result = subprocess.run(arg_list, capture_output=True, text=True)

    token = sample_data_result.stdout.strip()

    decoded_token = jwt.decode(token, options={"verify_signature": False})
    required_claim = "a_ha"

    assert required_claim in decoded_token


def test_utils_gen_jwt_channels(astarte_env_vars):

    realm = astarte_env_vars["realm"]
    private_key_dir = _get_private_key(realm)

    arg_list = ["astartectl", "utils", "gen-jwt", "channels", "-k", private_key_dir]
    sample_data_result = subprocess.run(arg_list, capture_output=True, text=True)
    token = sample_data_result.stdout.strip()

    decoded_token = jwt.decode(token, options={"verify_signature": False})
    required_claim = "a_ch"

    assert required_claim in decoded_token


def _get_private_key(realm_name):
    return os.path.realpath(f"{realm_name}_private.pem")
