# QuantumLedger: Monad Testnet Wallet Verifier

Efficiently validates Monad testnet wallet creation and genesis block accessibility using CryptowalletsX.

## Detailed Description

QuantumLedger is a Python-based tool designed to streamline the process of verifying Monad testnet wallet creation and accessibility. In the context of blockchain testing, its crucial to ensure that newly created wallets function correctly and can access the genesis block, signifying successful network integration. QuantumLedger addresses this need by leveraging the CryptowalletsX library, enabling rapid and reliable wallet creation and verification. This significantly reduces the manual effort required for developers involved in testing and onboarding onto the Monad testnet.

This tool automates the following critical processes: generating new Monad testnet wallets, attempting to retrieve the genesis block via each wallet, and reporting the success or failure of each attempt. The goal is to provide a clear and concise overview of wallet functionality, facilitating rapid identification of any potential issues in the wallet creation or network connection process. The reporting mechanism provides valuable insights into the health and stability of the Monad testnet during its development phase.

QuantumLedger is particularly valuable for developers, testers, and infrastructure engineers working with the Monad blockchain. It allows for rapid iteration and validation of network configurations, ensuring a smooth onboarding experience for new users. By providing a standardized and automated verification process, it helps to minimize errors and improve the overall reliability of the Monad testnet. The focus on efficiency and accuracy makes QuantumLedger an indispensable tool for maintaining the integrity of the blockchain during its crucial developmental stages.

## Key Features

*   **Automated Wallet Generation:** Utilizes CryptowalletsX to create a specified number of Monad testnet wallets programmatically.
*   **Genesis Block Retrieval:** Attempts to retrieve the genesis block using each generated wallet, verifying network connectivity.
*   **Concurrent Processing:** Employs asynchronous programming to generate and test wallets concurrently, significantly reducing execution time.
*   **Detailed Reporting:** Generates a comprehensive report indicating the success or failure of each wallet's genesis block retrieval attempt, including error messages for failed attempts.
*   **Customizable Wallet Count:** Allows users to specify the number of wallets to generate and test via command-line arguments.
*   **Error Handling:** Implements robust error handling to gracefully manage potential issues such as network connectivity problems or invalid wallet configurations.
*   **Modular Design:** Designed with a modular architecture, facilitating easy extension and modification to support future Monad testnet updates.

## Technology Stack

*   **Python:** The primary programming language used for implementing QuantumLedger, providing a flexible and extensible platform.
*   **CryptowalletsX:** A Python library that handles the complexities of wallet creation and management for various blockchain networks, including Monad. This library provides the functionality to interact with the Monad network and create valid wallet addresses.
*   **Asyncio:** Python's built-in asynchronous I/O library, enabling concurrent processing of wallet creation and genesis block retrieval, improving performance.
*   **Argparse:** A Python module for parsing command-line arguments, allowing users to configure the number of wallets to generate.

## Installation

1.  Clone the repository:
`git clone https://github.com/Nikeran22/QuantumLedger.git`

2.  Navigate to the project directory:
`cd QuantumLedger`

3.  Create a virtual environment:
`python3 -m venv venv`

4.  Activate the virtual environment:
    *   On Linux/macOS: `source venv/bin/activate`
    *   On Windows: `venv\Scripts\activate`

5.  Install the required dependencies:
`pip install -r requirements.txt`

## Configuration

QuantumLedger relies on environment variables for configuration. Create a `.env` file in the project directory and define the following variables:

*   `MONAD_TESTNET_RPC_URL`: The RPC endpoint for the Monad testnet. Example: `MONAD_TESTNET_RPC_URL=http://localhost:8545`
*   `WALLET_COUNT`: The number of wallets to generate. This can also be specified as a command-line argument, overriding the environment variable. Example: `WALLET_COUNT=10`

## Usage

To run QuantumLedger, execute the `main.py` script with the desired number of wallets as a command-line argument:

`python main.py --wallets 20`

This command will generate and test 20 Monad testnet wallets. The script will output a report to the console indicating the success or failure of each wallet's genesis block retrieval attempt. If a wallet fails, the error message will be included in the report. Example output:

Wallet 1: Success
Wallet 2: Failure - Error: Could not connect to RPC endpoint.
Wallet 3: Success
...

A summary report of the successful and failed wallets will also be provided at the end of the process.

## Contributing

We welcome contributions to QuantumLedger! Please follow these guidelines:

1.  Fork the repository.
2.  Create a new branch for your feature or bug fix.
3.  Write clear and concise code with comprehensive comments.
4.  Submit a pull request with a detailed description of your changes.
5.  Ensure your code adheres to the project's coding style.

## License

This project is licensed under the MIT License. See the [LICENSE](https://github.com/Nikeran22/QuantumLedger/blob/main/LICENSE) file for details.

## Acknowledgements

We would like to acknowledge the developers of CryptowalletsX for their excellent library, which is fundamental to the functionality of QuantumLedger.