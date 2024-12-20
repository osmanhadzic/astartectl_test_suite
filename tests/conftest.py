# SPDX-FileCopyrightText: 2024 SECO Mind Srl
#
# SPDX-License-Identifier: Apache-2.0

import os
import pytest


@pytest.fixture(scope="module")
def astarte_env_vars():
    """
    Fixture to provide Astarte environment variables for tests.
    """
    astarte_url = os.environ.get("E2E_API_URL")
    realm = os.environ.get("E2E_REALM")
    jwt = os.environ.get("E2E_JWT")
    housekeeping_jwt = os.environ.get("E2E_HOUSEKEEPING_JWT")
    device_test_1 = os.environ.get("E2E_DEVICE_TEST_1")
    device_test_2 = os.environ.get("E2E_DEVICE_TEST_2")

    assert (
        astarte_url and realm and jwt and device_test_1 and device_test_2 and housekeeping_jwt
    ), "Environment variables for Astarte setup are not properly configured."

    return {
        "astarte_url": astarte_url,
        "realm": realm,
        "jwt": jwt,
        "device_test_1": device_test_1,
        "device_test_2": device_test_2,
        "housekeeping_jwt": housekeeping_jwt,
    }
