#!/usr/bin/env python3

import os
import sqlite3
import sys

from bs4 import BeautifulSoup

if len(sys.argv) != 2:
    print("gen.py {version}")
    # sys.exit(1)
    V = "v21.9.4.35"
else:
    V = sys.argv[1]

db = sqlite3.connect("./docSet.dsidx")
cur = db.cursor()

try:
    cur.execute("DROP TABLE searchIndex;")
except:
    pass

cur.execute(
    "CREATE TABLE searchIndex(id INTEGER PRIMARY KEY, name TEXT, type TEXT, path TEXT);"
)
cur.execute("CREATE UNIQUE INDEX anchor ON searchIndex (name, type, path);")

docpath = f"./Documents/{V}"


def gen_index(filename, typ, selector="h2"):
    page = open(filename).read()
    soup = BeautifulSoup(page, features="html.parser")

    for e in soup.find_all(selector):
        title = e.text.strip()
        id = e.attrs.get("id")
        if id is None:
            continue
        path = filename
        if id is not None:
            path += f"#{id}"
        if title == "":
            continue
        cur.execute(
            "INSERT OR IGNORE INTO searchIndex(name, type, path) VALUES (?,?,?);",
            (title, typ, path[len("./Documents/"):]),
        )


def visit_tree(dir, fn, typ, selector="h2"):
    for dirpath, subdirs, files in os.walk(dir):
        if "amp" not in dirpath:
            for f in files:
                print(f"---> {dirpath}/{f}")
                fn(os.path.join(dirpath, f), typ, selector)

visit_tree(os.path.join(docpath, "sql-reference/functions"), gen_index, "Function")
visit_tree(os.path.join(docpath, "sql-reference/aggregate-functions"), gen_index, "Function")
visit_tree(os.path.join(docpath, "sql-reference/aggregate-functions"), gen_index, "Function", "h1")
visit_tree(os.path.join(docpath, "sql-reference/statements"), gen_index, "Statement", "h1")


db.commit()
db.close()
