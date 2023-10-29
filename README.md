# Memory-Leak-Inspector

[![Dashboard Grafana](https://img.shields.io/badge/Dashboard-Grafana-fd6600)](http://localhost:3000/?orgId=1)
## Introduction

A tool for memory leak inspection
<p align="center">
<img src="fig/memory leak inspector.png" width = "686" height = "250" alt="memory leak inspector" />
</p>

## Installation

Assuming a fresh Anaconda distribution with Python 3.8, you can install the dependencies with:

```sh
cd Memory-Leak-Inspector
pip install -r requirements.txt
```

## Run without environment (pyinstaller)

- Run the following command to build the executable file:
 ```sh
 pyinstaller --distpath <path-to-exe-file> memory_measurement_app.spec
 ```
 
 - Run the following command to execute the file:
  ```sh
 cd <path-to-exe-file>\memory_measurement_app
 memory_measurement_app.exe --exe_name <exe-name> --del_table <yes/no> --database <DB-name> --user <user> --password <password> --host <host> --port <port>
 ```