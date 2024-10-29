# Astartectl Test Suite

## Overview

The Astartectl Test Suite is a comprehensive testing framework for the Astartectl command-line tool. This suite is designed to ensure the functionality, reliability, and performance of Astartectl across various scenarios and configurations.

## What is Astartectl?

[Astartectl](https://github.com/astarte-platform/astartectl) is a command-line tool for interacting with Astarte, a powerful open-source framework for building IoT applications. Astartectl allows users to manage devices, realms, and data in Astarte, making it easier to develop and test IoT solutions.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Features

- Automated testing for Astartectl commands
- Support for multiple test cases and configurations
- Easy integration with CI/CD pipelines
- Detailed logging and reporting for test results

## Requirements

- Astartectl binary available in your PATH (download from [Releases](https://github.com/astarte-platform/astartectl/releases))
- Python 3.12 or higher
- A running Astarte instance
- Environment variables configured:
  - `E2E_API_URL`: URL of the Astarte API
  - `E2E_REALM`: Realm for the Astarte instance
  - `E2E_JWT`: JSON Web Token for authentication
  - `E2E_DEVICE_TEST_1`: Device ID for testing

## Installation

Clone the repository:

```bash
git clone https://github.com/astarte-platform/astartectl_test_suite.git
cd astartectl_test_suite
pip install -e ./tests
```

Make sure to download the Astartectl binary from the Releases page and place it in your PATH.

Install all required [interfaces](https://github.com/astarte-platform/astartectl_test_suite/tree/main/interfaces) on Astarte instance.

Import data from [import.xml](https://github.com/astarte-platform/astartectl_test_suite/blob/main/import.xml) file using [Astarte import tool](https://github.com/astarte-platform/astarte/tree/master/tools/astarte_import).

## Usage

Before running the tests, ensure that the environment variables are set:

```bash
export E2E_API_URL="http://your-astarte-api-url"
export E2E_REALM="your-realm"
export E2E_JWT="your-jwt-token"
export E2E_DEVICE_TEST_1="your-device-id"
```

Make sure the tests.sh script is executable. You can make it executable with:
```bash
chmod +x tests.sh
```
You can run the test suite using the following command:
```bash
./tests.sh
```
For more detailed output, you can modify the script to include verbose logging.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

1. Fork the repository
2. Create a new branch (`git checkout -b feature/YourFeature`)
3. Make your changes and commit them (`git commit -m 'Add some feature'`)
4. Push to the branch (`git push origin feature/YourFeature`)
5. Open a pull request

## License

Astartectl Test Suite source code is released under the Apache 2 License.

Check the LICENSE file for more information.
