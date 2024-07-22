from bd.oracle import OracleDB

class RunPackage:

    def __init__(self):
        self.db = OracleDB()

    def ejecutaPLSQL(self):
        package = """
            BEGIN
                DBMS_OUTPUT.PUT_LINE(
                    NEXUS_GIS.INFORMACION_ENREMTAT_DIN.INICIO
                );
            END;
        """
        self.db.connect()
        self.db.execute_plsql(package)
        self.db.close()

if __name__ == "__main__":
    run_package = RunPackage()
    run_package.ejecutaPLSQL()
