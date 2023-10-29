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

- Enter the account `admin` and the password `admin` on the web page.

<p align="center">
<img src="fig/login.png" width = "420" height = "401" alt="login" />
</p>

- Go to `Home` > `Connections` > `Data sources` and click `Add data source`

<p align="center">
<img src="fig/data.png" width = "1049" height = "239" alt="data" />
</p>

- Choose PostgreSQL

<p align="center">
<img src="fig/postgresql.png" width = "1049" height = "244" alt="postgresql" />
</p>

- Please fill in the following information and select `disable` for TLS/SSL Mode

<p align="center">
<img src="fig/disable.png" width = "719" height = "459" alt="disable" />
</p>

- Then please click the `+` in the upper right corner and select `import dashboard`, you can start using it after importing it.

<p align="center">
<img src="fig/import.png" width = "1202" height = "289" alt="import" />
</p>

<p align="center">
<img src="fig/start.png" width = "1014" height = "463" alt="start" />
</p>