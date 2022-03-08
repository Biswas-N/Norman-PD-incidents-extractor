import sqlite3
from contextlib import closing

from project0.parser import Incident


class NormanPdDb():
    """NormanPdDb is used as an abstraction to store and fetch incidents data in and from sqlite3"""

    table_name = 'incidents'

    def __init__(self, db_name) -> None:
        self.db_name = db_name

    # Returns true if the database is connected properly, else returns false
    def check_con(self) -> bool:
        try:
            with closing(sqlite3.connect(self.db_name)) as con:
                if con.total_changes >= 0:
                    return True
        except Exception:
            return False

    # Adds the incidents to the database and returns the number of incidents inserted upon success
    # else returns -1 indicating some exception was occured
    def add_incidents(self, incidents: list[Incident]) -> int:
        try:
            with closing(sqlite3.connect(self.db_name)) as con:
                with closing(con.cursor()) as cur:
                    cur.execute(f'DROP TABLE IF EXISTS {self.table_name}')
                    cur.execute(
                        f'CREATE TABLE {self.table_name} (incident_time TEXT, incident_number TEXT, incident_location TEXT, nature TEXT, incident_ori TEXT)'
                    )

                    for incident in incidents:
                        cur.execute(
                            f'INSERT INTO {self.table_name} VALUES (?,?,?,?,?)',
                            (incident.date_time,
                             incident.incident_number,
                             incident.location,
                             incident.nature,
                             incident.incident_ori))
                    con.commit()
                    return con.total_changes
        except Exception as e:
            print(e)
            return -1

    # Returns a string containing extracted nature types and number of times they appeared
    # Eg. Missing Person|12
    def get_stats(self) -> str:
        try:
            with closing(sqlite3.connect(self.db_name)) as con:
                with closing(con.cursor()) as cur:
                    natures = cur.execute(
                        f"SELECT nature, count(*) FROM {self.table_name} WHERE IFNULL(nature, '') != '' GROUP BY nature ORDER BY count(*) DESC, nature ASC"
                    ).fetchall()

                    natures_with_count = [f'Nature|Count']
                    for nature in natures:
                        natures_with_count.append(f'{nature[0]}|{nature[1]}')
                    return '\n'.join(natures_with_count)
        except Exception as e:
            print(e)
            return None


# Create a sqlite3 datafile in current project root if it is not already exists
def create_db(store_name='normanpd.db') -> NormanPdDb:
    return NormanPdDb(store_name)
