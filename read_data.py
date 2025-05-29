import polars as pl

db_uri = "sqlite://sqlite.db"


df_family = pl.read_database_uri(query="SELECT * FROM family", uri=db_uri)
df_person = pl.read_database_uri(query="SELECT * FROM person", uri=db_uri)
df_place = pl.read_database_uri(query="SELECT * FROM place", uri=db_uri)


if __name__ == "__main__":
    print(df_family.head())
    print(df_person.head())
    print(df_place.head())
