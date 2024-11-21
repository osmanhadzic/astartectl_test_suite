# SPDX-FileCopyrightText: 2024 SECO Mind Srl
#
# SPDX-License-Identifier: Apache-2.0


import subprocess
import os
import json


def test_realm_management_trigger_install(astarte_env_vars):
    astarte_url = astarte_env_vars["astarte_url"]
    realm = astarte_env_vars["realm"]
    jwt = astarte_env_vars["jwt"]

    current_dir = os.path.dirname(__file__)
    assert os.path.exists(current_dir)

    trigger_path = os.path.join(current_dir, "test_triggers", "test_trigger.json")

    arg_list = [
        "astartectl",
        "realm-management",
        "triggers",
        "install",
        trigger_path,
        "-t",
        jwt,
        "-u",
        astarte_url,
        "-r",
        realm,
    ]
    trigger_result = subprocess.run(arg_list, capture_output=True)
    assert trigger_result.stdout.replace(b"\n", b"") == b"ok"


def test_realm_management_trigger_list(astarte_env_vars):
    astarte_url = astarte_env_vars["astarte_url"]
    realm = astarte_env_vars["realm"]
    jwt = astarte_env_vars["jwt"]

    arg_list = [
        "astartectl",
        "realm-management",
        "triggers",
        "list",
        "-t",
        jwt,
        "-u",
        astarte_url,
        "-r",
        realm,
    ]
    trigger_result = subprocess.run(arg_list, capture_output=True)
    assert trigger_result.stdout.replace(b"[", b"").replace(b"]", b"").replace(b"\n", b"") == (
        b"test_trigger"
    )


def test_realm_management_trigger_show(astarte_env_vars):
    astarte_url = astarte_env_vars["astarte_url"]
    realm = astarte_env_vars["realm"]
    jwt = astarte_env_vars["jwt"]

    current_dir = os.path.dirname(__file__)
    assert os.path.exists(current_dir)

    arg_list = [
        "astartectl",
        "realm-management",
        "trigger",
        "show",
        "test_trigger",
        "-t",
        jwt,
        "-u",
        astarte_url,
        "-r",
        realm,
    ]
    trigger_result = subprocess.run(arg_list, capture_output=True)
    tigger_json = json.loads(trigger_result.stdout)

    with open(os.path.join(current_dir, "test_triggers", "test_trigger.json")) as f:
        expected_trigger_json = json.load(f)

    assert tigger_json["name"] == expected_trigger_json["name"]
    assert tigger_json["simple_triggers"] == expected_trigger_json["simple_triggers"]


def test_realm_management_trigger_sync(astarte_env_vars):
    astarte_url = astarte_env_vars["astarte_url"]
    realm = astarte_env_vars["realm"]
    jwt = astarte_env_vars["jwt"]

    current_dir = os.path.dirname(__file__)
    assert os.path.exists(current_dir)

    trigger_path = os.path.join(current_dir, "test_triggers", "test_trigger.json")

    arg_list = [
        "astartectl",
        "realm-management",
        "trigger",
        "sync",
        trigger_path,
        "-t",
        jwt,
        "-u",
        astarte_url,
        "-r",
        realm,
    ]
    trigger_result = subprocess.run(arg_list, capture_output=True)
    trigger_result.stdout = trigger_result.stdout.replace(b"\n", b"")
    trigger_result.stdout = trigger_result.stdout.decode("utf-8")
    expect = "The following triggers already exists and WILL NOT be updated"
    assert expect in trigger_result.stdout


def test_realm_management_trigger_save(astarte_env_vars):
    astarte_url = astarte_env_vars["astarte_url"]
    realm = astarte_env_vars["realm"]
    jwt = astarte_env_vars["jwt"]

    current_dir = os.path.dirname(__file__)
    assert os.path.exists(current_dir)

    arg_list = [
        "astartectl",
        "realm-management",
        "trigger",
        "save",
        current_dir,
        "-t",
        jwt,
        "-u",
        astarte_url,
        "-r",
        realm,
    ]
    trigger_result = subprocess.run(arg_list, capture_output=True)
    assert os.path.exists(os.path.join(current_dir, "test_trigger.json"))


def test_realm_management_trigger_delete(astarte_env_vars):
    astarte_url = astarte_env_vars["astarte_url"]
    realm = astarte_env_vars["realm"]
    jwt = astarte_env_vars["jwt"]

    arg_list = [
        "astartectl",
        "realm-management",
        "trigger",
        "delete",
        "test_trigger",
        "-t",
        jwt,
        "-u",
        astarte_url,
        "-r",
        realm,
    ]
    trigger_result = subprocess.run(arg_list, capture_output=True)
    assert trigger_result.stdout.replace(b"\n", b"") == b"ok"
