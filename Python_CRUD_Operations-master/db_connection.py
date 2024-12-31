import pypyodbc
import config

# Return the sql connection
def getConnection():
    # Access the correct keys from DATABASE_CONFIG
    connection_string = (
        "Driver={" + config.DATABASE_CONFIG["Driver"] + "};"  # Correct key for the driver
        "Server=" + config.DATABASE_CONFIG["Server"] + ";"
        "Database=" + config.DATABASE_CONFIG["Database"] + ";"
        "uid=" + config.DATABASE_CONFIG["UID"] + ";"
        "pwd=" + config.DATABASE_CONFIG["Password"]
    )
    connection = pypyodbc.connect(connection_string)
    return connection