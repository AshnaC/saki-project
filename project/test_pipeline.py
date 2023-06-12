
from data.pipeline import load_temperature_file
import sqlite3


def test_file_read():
    load_temperature_file()
    conn = sqlite3.connect('data/dataset.sqlite')
    c = conn.cursor()

    # get the count of tables with the name
    c.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='temperature' ''')

    assert c.fetchone()[0] == 1
    conn.commit()
    conn.close()
