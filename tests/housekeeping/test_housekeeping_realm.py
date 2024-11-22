# SPDX-FileCopyrightText: 2024 SECO Mind Srl
#
# SPDX-License-Identifier: Apache-2.0

import subprocess
import os


def test_housekeeping_realm_list(astarte_env_vars):
    astarte_url = astarte_env_vars["astarte_url"]
    realm = astarte_env_vars["realm"]
    housekeeping_jwt = astarte_env_vars["housekeeping_jwt"]

    arg_list = [
        "astartectl",
        "housekeeping",
        "realms",
        "list",
        "-u",
        astarte_url,
        "-t",
        housekeeping_jwt,
    ]
    realm_list_result = subprocess.run(arg_list, capture_output=True, text=True)
    realm_list = _replace_brackets_from_string(realm_list_result.stdout)
    assert realm in realm_list


def test_housekeeping_realm_create(astarte_env_vars):
    astarte_url = astarte_env_vars["astarte_url"]
    housekeeping_jwt = astarte_env_vars["housekeeping_jwt"]

    new_realm = "newrealm"

    ark_key_create = ["astartectl", "utils", "gen-keypair", new_realm]

    subprocess.run(ark_key_create, capture_output=True, text=True)

    new_private_key = f"{new_realm}_public.pem"

    private_key_dir = os.path.realpath(new_private_key)

    arg_create = [
        "astartectl",
        "housekeeping",
        "realms",
        "create",
        new_realm,
        "-u",
        astarte_url,
        "--realm-public-key",
        private_key_dir,
        "-t",
        housekeeping_jwt,
        "-y",
    ]
    realm_create_result = subprocess.run(arg_create, capture_output=True, text=True)
    assert f"Realm {new_realm} created successfully!\n" in realm_create_result.stdout


def test_housekeeping_realm_show(astarte_env_vars):
    astarte_url = astarte_env_vars["astarte_url"]
    realm = astarte_env_vars["realm"]
    jwt_token = astarte_env_vars["housekeeping_jwt"]

    arg_show = [
        "astartectl",
        "housekeeping",
        "realms",
        "show",
        realm,
        "-t",
        jwt_token,
        "-u",
        astarte_url,
    ]
    realm_show_result = subprocess.run(arg_show, capture_output=True, text=True)

    assert f"Name:{realm}" in realm_show_result.stdout


def _replace_brackets_from_string(string):
    return string.replace("[", "").replace("]", "").replace("\n", "")
