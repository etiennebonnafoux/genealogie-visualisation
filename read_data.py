import sqlite3

from utils import dms_to_dd
import polars as pl

db_uri = "sqlite.db"


def read_place(db_uri: str = db_uri) -> list[tuple[float, float]]:
    """Return the list of location with their coordinate"""
    con = sqlite3.connect(db_uri)
    cur = con.cursor()
    cur.execute("SELECT long,lat FROM place")
    res = cur.fetchall()
    locations = [(dms_to_dd(long_str), dms_to_dd(lat_str)) for long_str, lat_str in res]
    return locations

places = read_place()
places_pl = pl.from_dict({"lat":[x[1] for x in places],"lon":[x[0] for x in places]})

if __name__ == "__main__":
    read_place(db_uri)
