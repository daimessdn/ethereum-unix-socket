# ethereum-unix-socket

**ethereum-unix-socket** is an UNIX-domain-socket-based program for Ethereum transaction.

## how it works
This program uses **UNIX domain socket**, the way we can used for communicate through filesystem (specific pathname) on the single host. There is `server.py` (shortcut: `vault`) which processes data to generate **signed hash Ethereum transaction** based on client input, and `input.py` which received some input to be sent into server.

## some notes before start
- All input data are assumed to be valid containing `id`:`int`, `type`:`string`, `from_address`:`string`, `to_address`:`string`, and `amount`:`string` to make valid output data containing `id`:`int` and `tx`:`string`.
- Every input object has the same `type` properties by value: `sign_transfer`.
- Every input object has the same `from_address` (sender wallet address). In this case, I'm currently using `0xACa20B87dAEFe8a89f80E15493609bE116c8efc5` as a wallet address.
- Because signing transaction requires **private key** and private key is **too sensitive** to be shared publicly, I created the **hidden file** with filename `.<sender-address>.txt`. You can see the file by typing `ls -la` for displaying all files (including hidden).
- Using `eth_gasPrice` and `eth_estimateGas` JSON-RPC API, I've got gas price value by 1 gwei (1E9 wei) on all testing transactions (`transaction_input.txt`) according to `eth_gasPrice`. I've also got estimated gas usage by `21000` wei according on `eth_estimateGas`.
- I've set the `gas` properties on **all transactions** to 200000 (more than value from `eth_estimateGas` for speed purpose) and `gasPrice` by 1000000000 (1 gwei according to `eth_gasPrice`).
- Knowing **transaction fees** = **gas usage** * **gas price**, I've got fees by 0.000021 Ether (21E12 wei) in all my testing samples (I might be able to assume that current transaction fee in this case is 0.000021 Ether).

## languages feature(s)
Python 3

## package dependencies
You can see the packages requirements in `requirements.txt` file.

## first setup
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## basic operation

### Run the UDS server, where `<pathname>` is required.

```bash
python3 server.py <pathname>
```

or

```bash
./vault <pathname>
```

### Run the UDS client
You can run the UDS client to interact with UDS server with the same `<pathname>` as `server.py` or `vault` after the socket is `started`.

```bash
python3 client.py <pathname>
```

After starting `client.py`, you can input some string input (using JSON format) to be processed (generate signed hash output) in server. You can terminate the client by typing `\n` on client console.