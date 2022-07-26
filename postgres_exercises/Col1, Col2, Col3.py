Col1, Col2, Col3
V1, V2, V3
V4, V5, V6
import uuid

rows = [
    [1, 2, 3],
    [4, 5, 6],
    [4, 5, 6],
    [4, 5, 6],
    [4, 5, 6],
    [4, 5, 6],
    [4, 5, 6],
    [4, 5, 6],
    [4, 5, 6],
    [4, 5, 6],
    [4, 5, 6],
    [4, 5, 6],
    [4, 5, 6],
    [4, 5, 6],
    [4, 5, 6],
    [4, 5, 6],
]

header = ["Col1", "Col2", "Col3"]

for row in rows:
    uuid_val = uuid.uuid4()
    sql = f"insert into mytable (pkcol, {header[0]}, {header[1]}, {header[2]}) values ('{uuid_val}','{row[0]}', '{row[1]}', '{row[2]}')"


