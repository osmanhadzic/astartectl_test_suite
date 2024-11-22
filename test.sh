#!/bin/bash

# SPDX-FileCopyrightText: 2024 SECO Mind Srl
#
# SPDX-License-Identifier: Apache-2.0

pytest -v ./tests/utils
pytest -v ./tests/app_engine
pytest -v ./tests/realm_management
pytest -v ./tests/pairing_agent
