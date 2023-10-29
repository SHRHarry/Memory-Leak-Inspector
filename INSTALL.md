# Installation

This page will guide you to install Grafana and PostgreSQL step by step.

## Grafana installation

- Please go to [Grafana official website](https://grafana.com/grafana/download?pg=get&plcmt=selfmanaged-box1-cta1&platform=windows) to download the Windows version.

## PostgreSQL installation

- Please go to the [PostgreSQL official website](https://www.enterprisedb.com/downloads/postgres-postgresql-downloads) to download the Windows version.

- If the computer name is in Chinese, the installation may fail and the following window will pop up. At this point you can use the [download point](https://get.enterprisedb.com/postgresql/postgresql-11.2-1-windows-x64.exe) to install.

<p align="center">
<img src="fig/fail.png" width = "758" height = "242" alt="fail" />
</p>

- When installing, please set the password to `admin` and the port to `5432`.

## Grafana setup

- Run the following command to build the executable file:
 ```sh
 pyinstaller --distpath <path-to-exe-file> memory_measurement_app.spec
 ```
 
 - Run the following command to execute the file:
  ```sh
 cd <path-to-exe-file>\memory_measurement_app
 memory_measurement_app.exe --exe_name <exe-name> --del_table <yes/no> --database <DB-name> --user <user> --password <password> --host <host> --port <port>
 ```
 
 - Or you can place the entire packaged file under \bin and execute MemoryInspector.exe