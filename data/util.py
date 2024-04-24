from typing import NoReturn

import streamlit as st
from sqlalchemy import text
from streamlit.connections import SQLConnection

CONNECTION_NAME = "sqlite-db"
DB_URL = "sqlite:///data/data.sqlite"
VALID_TABLE_NAMES = [
    "pet_owners",
    "chinook_album",
]


def get_connection() -> SQLConnection:
    # Let st.connection handle creating or reusing an existing connection
    return st.connection(
        CONNECTION_NAME,
        url=DB_URL,
        type="sql",
    )


def reset_table(conn: SQLConnection, dataset: str) -> NoReturn | None:
    if dataset not in VALID_TABLE_NAMES:
        errmsg = f"Invalid dataset name. Must choose from: {', '.join(VALID_TABLE_NAMES)}"
        raise RuntimeError(errmsg)

    if dataset == "pet_owners":
        # From https://docs.streamlit.io/library/advanced-features/connecting-to-data
        with conn.session as s:
            s.execute("CREATE TABLE IF NOT EXISTS pet_owners (person TEXT, pet TEXT);")
            s.execute("DELETE FROM pet_owners;")
            pet_owners = [
                {"person": "jerry", "pet": "fish"},
                {"person": "barbara", "pet": "cat"},
                {"person": "alex", "pet": "puppy"},
            ]
            s.execute(
                text("INSERT INTO pet_owners (person, pet) VALUES (:person, :pet)"),
                pet_owners,
            )
            s.commit()
    elif dataset == "chinook_album":
        # modified from https://github.com/lerocha/chinook-database/releases
        drop_sql = "drop table if exists chinook_album"
        create_sql = """CREATE TABLE chinook_album
(
    AlbumId INTEGER  NOT NULL,
    Title TEXT  NOT NULL,
    ArtistId INTEGER  NOT NULL,
    CONSTRAINT PK_Album PRIMARY KEY  (AlbumId)
);"""
        insert_sql = """INSERT INTO chinook_album (AlbumId, Title, ArtistId) VALUES
    (1, 'For Those About To Rock We Salute You', 1),
    (2, 'Balls to the Wall', 2),
    (3, 'Restless and Wild', 2),
    (4, 'Let There Be Rock', 1),
    (5, 'Big Ones', 3),
    (6, 'Jagged Little Pill', 4),
    (7, 'Facelift', 5),
    (8, 'Warner 25 Anos', 6),
    (9, 'Plays Metallica By Four Cellos', 7),
    (10, 'Audioslave', 8),
    (11, 'Out Of Exile', 8),
    (12, 'BackBeat Soundtrack', 9),
    (13, 'The Best Of Billy Cobham', 10),
    (14, 'Alcohol Fueled Brewtality Live! [Disc 1]', 11),
    (15, 'Alcohol Fueled Brewtality Live! [Disc 2]', 11),
    (16, 'Black Sabbath', 12),
    (17, 'Black Sabbath Vol. 4 (Remaster)', 12),
    (18, 'Body Count', 13),
    (19, 'Chemical Wedding', 14),
    (20, 'The Best Of Buddy Guy - The Millenium Collection', 15)
    ;
        """
        with conn.session as s:
            s.execute(drop_sql)
            s.execute(create_sql)
            s.execute(insert_sql)
            s.commit()


def create_seed_data_uc1(conn: SQLConnection) -> NoReturn | str:
    TABLE_NAME = "uc1"
    with conn.session as s:
        drop_sql = f"drop table if exists {TABLE_NAME}"

        # last column's definition must not end in a comma.
        create_sql = f"""create table {TABLE_NAME}(
usercode TEXT,
friend_userid TEXT,
invite_status TEXT
);
"""
        # last row of data must not end in a comma.
        insert_sql = f"""insert into {TABLE_NAME} values
('nwu999', 'sfif932', 'accepted'),
('nwu999', 'kden947', 'accepted'),
('nwu999', 'jcha657', 'accepted'),
('nwu999', 'tjoe921', 'requested'),
('tjoe921', 'sfif932', 'accepted')
;
"""
        s.execute(drop_sql)
        s.execute(create_sql)
        s.execute(insert_sql)
        s.commit()

    return TABLE_NAME


def create_seed_data_uc2(conn: SQLConnection) -> NoReturn | str:
    TABLE_NAME = "uc2"
    with conn.session as s:
        drop_sql = f"drop table if exists {TABLE_NAME}"

        # last column's definition must not end in a comma.
        create_sql = f"""create table {TABLE_NAME}(
coursecode TEXT,
coursetitle TEXT,
difficulty TEXT
);
"""
        # last row of data must not end in a comma.
        insert_sql = f"""insert into {TABLE_NAME} values
('Māori 101', 'Introduction to written Te Reo', 'Beginner'),
('Māori 111', 'Introduction to spoken Te Reo', 'Beginner'),
('Māori 115', 'Maori History', 'Beginner'),
('Māori 140', 'Kapa Haka', 'Beginner'),
('Māori 240', 'Kapa Haka II', 'Intemediate'),
('Māori 340', 'Kapa Haka III', 'Advanced')
;
"""
        s.execute(drop_sql)
        s.execute(create_sql)
        s.execute(insert_sql)
        s.commit()

    return TABLE_NAME
