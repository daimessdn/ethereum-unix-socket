# ethereum-unix-socket

**ethereum-unix-socket** is an UNIX-domain-socket-based program for Ethereum transaction.

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
- Run the UDS server, where `<pathname>` is required.

```bash
python3 server.py <pathname>
```
or
```bash
./vault <pathname>
```

- Run the UDS client to interact with UDS server with the same `<pathname>` as `server.py` or `vault`.
```bash
python3 client.py <pathname>
```