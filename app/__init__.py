import pymysql

# 1. Trick Django into using PyMySQL instead of mysqlclient
pymysql.install_as_MySQLdb()

# 2. Trick Django into thinking the version is high enough (2.2.1+)
pymysql.version_info = (2, 2, 7, "final", 0)