# SPDX-FileCopyrightText: 2024 SECO Mind Srl
#
# SPDX-License-Identifier: Apache-2.0

import subprocess
import json
import os
from resources import list_of_interface_names


def test_realm_management_interfaces_list(astarte_env_vars):
    astarte_url = astarte_env_vars["astarte_url"]
    realm = astarte_env_vars["realm"]
    jwt = astarte_env_vars["jwt"]

    arg_list = [
        "astartectl",
        "realm-management",
        "interfaces",
        "list",
        "-t",
        jwt,
        "-u",
        astarte_url,
        "-r",
        realm,
    ]
    interfaces_result = subprocess.run(arg_list, capture_output=True, text=True)
    interfaces_result.stdout = _replace_brackets_from_string(interfaces_result.stdout)

    for interface in list_of_interface_names:
        assert interface in interfaces_result.stdout


def test_realm_management_interfaces_install(astarte_env_vars):
    astarte_url = astarte_env_vars["astarte_url"]
    realm = astarte_env_vars["realm"]
    jwt = astarte_env_vars["jwt"]

    current_dir = os.path.realpath("interfaces")

    assert os.path.exists(current_dir)

    for interface in list_of_interface_names:
        interface_path = os.path.join(current_dir, f"{interface}.json")
        arg_list = [
            "astartectl",
            "realm-management",
            "interfaces",
            "install",
            interface_path,
            "-t",
            jwt,
            "-u",
            astarte_url,
            "-r",
            realm,
        ]
        install_result = subprocess.run(arg_list, capture_output=True, text=True)

        exception = "Interface already exists"
        assert exception in install_result.stderr


def test_realm_management_interfaces_version(astarte_env_vars):
    astarte_url = astarte_env_vars["astarte_url"]
    realm = astarte_env_vars["realm"]
    jwt = astarte_env_vars["jwt"]

    for interface in list_of_interface_names:
        arg_list = [
            "astartectl",
            "realm-management",
            "interfaces",
            "versions",
            interface,
            "-t",
            jwt,
            "-u",
            astarte_url,
            "-r",
            realm,
        ]
        version_result = subprocess.run(arg_list, capture_output=True, text=True)
        versions = _replace_brackets_from_string(version_result.stdout)
        assert versions.replace("\n", "") == "1"


def test_realm_management_interfaces_show(astarte_env_vars):
    astarte_url = astarte_env_vars["astarte_url"]
    realm = astarte_env_vars["realm"]
    jwt = astarte_env_vars["jwt"]

    for interface in list_of_interface_names:
        arg_list = [
            "astartectl",
            "realm-management",
            "interfaces",
            "show",
            interface,
            "1",
            "-t",
            jwt,
            "-u",
            astarte_url,
            "-r",
            realm,
        ]
        show_result = subprocess.run(arg_list, capture_output=True, text=True)
        show_result.stdout = json.loads(show_result.stdout)
        assert show_result.stdout["interface_name"] == interface


def test_realm_management_interfaces_sync(astarte_env_vars):
    astarte_url = astarte_env_vars["astarte_url"]
    realm = astarte_env_vars["realm"]
    jwt = astarte_env_vars["jwt"]

    current_dir = os.path.realpath("interfaces")

    assert os.path.exists(current_dir)

    for interface in list_of_interface_names:

        interface_path = os.path.join(current_dir, f"{interface}.json")

        arg_list = [
            "astartectl",
            "realm-management",
            "interfaces",
            "sync",
            interface_path,
            "-t",
            jwt,
            "-u",
            astarte_url,
            "-r",
            realm,
        ]
        sync_result = subprocess.run(arg_list, capture_output=True, text=True)
        exception = "Your realm is in sync with the provided interface files\n"
        assert sync_result.stdout == exception


def test_realm_management_interfaces_save(astarte_env_vars):
    astarte_url = astarte_env_vars["astarte_url"]
    realm = astarte_env_vars["realm"]
    jwt = astarte_env_vars["jwt"]

    current_dir = os.path.dirname(__file__)

    assert os.path.exists(current_dir)

    arg_list = [
        "astartectl",
        "realm-management",
        "interfaces",
        "save",
        current_dir,
        "-t",
        jwt,
        "-u",
        astarte_url,
        "-r",
        realm,
    ]
    subprocess.run(arg_list, capture_output=True, text=True)

    for interface in list_of_interface_names:
        assert os.path.exists(os.path.join(current_dir, f"{interface}_v1.json"))


def test_realm_management_interfaces_install_draft(astarte_env_vars):
    astarte_url = astarte_env_vars["astarte_url"]
    realm = astarte_env_vars["realm"]
    jwt = astarte_env_vars["jwt"]

    interface = "test.astarte-platform.draft.interfaces.Install"

    current_dir = os.path.dirname(__file__)
    interface_path = os.path.join(current_dir, "test_interfaces", f"{interface}.json")

    assert os.path.exists(interface_path)

    arg_list = [
        "astartectl",
        "realm-management",
        "interfaces",
        "install",
        interface_path,
        "-t",
        jwt,
        "-u",
        astarte_url,
        "-r",
        realm,
    ]
    install_result = subprocess.run(arg_list, capture_output=True, text=True)
    install_result.stdout.replace("\n", "") == "ok"


def test_realm_management_interfaces_update_draft(astarte_env_vars):
    astarte_url = astarte_env_vars["astarte_url"]
    realm = astarte_env_vars["realm"]
    jwt = astarte_env_vars["jwt"]

    interface = "test.astarte-platform.draft.interfaces.Install"

    current_dir = os.path.dirname(__file__)
    interface_path = os.path.join(
        current_dir, "test_interfaces/test_interfaces_update", f"{interface}.json"
    )

    assert os.path.exists(interface_path)

    arg_list = [
        "astartectl",
        "realm-management",
        "interfaces",
        "update",
        interface_path,
        "-t",
        jwt,
        "-u",
        astarte_url,
        "-r",
        realm,
    ]
    update_result = subprocess.run(arg_list, capture_output=True, text=True)
    update_result.stdout.replace("\n", "") == "ok"


def test_realm_management_interfaces_delete_draft(astarte_env_vars):
    astarte_url = astarte_env_vars["astarte_url"]
    realm = astarte_env_vars["realm"]
    jwt = astarte_env_vars["jwt"]

    interface = "test.astarte-platform.draft.interfaces.Install"

    current_dir = os.path.dirname(__file__)
    interface_path = os.path.join(current_dir, "test_interfaces", f"{interface}.json")

    assert os.path.exists(interface_path)

    arg_list = [
        "astartectl",
        "realm-management",
        "interfaces",
        "delete",
        interface,
        "-t",
        jwt,
        "-u",
        astarte_url,
        "-r",
        realm,
    ]
    delete_result = subprocess.run(arg_list, capture_output=True, text=True)
    delete_result.stdout.replace("\n", "") == "ok"


def _replace_brackets_from_string(string):
    return string.replace("[", "").replace("]", "")
