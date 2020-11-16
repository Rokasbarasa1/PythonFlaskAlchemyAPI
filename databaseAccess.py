import pyodbc

class DataAccess:
    @staticmethod
    def get_co2():
        server = 'tcp:enviorment-server.database.windows.net'
        database = 'EnviormentDatabase'
        username = 'rokasbarasa1'
        password = 'Augis123*'
        cnxn = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
        cursor = cnxn.cursor()
        cursor.execute('SELECT top 1 * FROM [EnviormentDatabase].[dbo].[CarbonDioxideReading]')
        return dict(enumerate(item[0] for item in cursor))

    @staticmethod
    def get_settings():
        server = 'tcp:enviorment-server.database.windows.net'
        database = 'EnviormentDatabase'
        username = 'rokasbarasa1'
        password = 'Augis123*'
        cnxn = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
        cursor = cnxn.cursor()
        cursor.execute('SELECT * FROM [EnviormentDatabase].[dbo].[Settings]')
        return dict(enumerate(item[0] for item in cursor))
