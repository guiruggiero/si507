import sqlite3
import sys
import os
import csv

def create_table():
    if os.path.exists("ConsumerComplaintsSmall.sqlite"):
        os.remove("ConsumerComplaintsSmall.sqlite")
    conn = sqlite3.connect("ConsumerComplaintsSmall.sqlite")
    cur = conn.cursor()
    statement = '''CREATE TABLE 'State' (
                    'id' INTEGER PRIMARY KEY AUTOINCREMENT,
                    'name' TEXT UNIQUE NOT NULL);'''

    cur.execute(statement)
    statement = '''CREATE TABLE 'ZipCode' (
                    'id' INTEGER PRIMARY KEY AUTOINCREMENT,
                    'detail' TEXT UNIQUE NOT NULL,
                    'state_id' INT NOT NULL);'''

    cur.execute(statement)

    statement = '''CREATE TABLE 'Tag' (
                    'id' INTEGER PRIMARY KEY AUTOINCREMENT,
                    'name' TEXT UNIQUE NOT NULL); '''
    cur.execute(statement)

    statement = '''CREATE TABLE 'SubmissionMethod' (
                    'id' INTEGER PRIMARY KEY AUTOINCREMENT,
                    'name' TEXT UNIQUE NOT NULL);'''
    cur.execute(statement)

    statement = '''CREATE TABLE 'ResponseToConsumer' (
                    'id' INTEGER PRIMARY KEY AUTOINCREMENT,
                    'detail' TEXT UNIQUE NOT NULL);'''
    cur.execute(statement)

    statement = '''CREATE TABLE 'Company' (
                    'id' INTEGER PRIMARY KEY AUTOINCREMENT,
                    'name' TEXT UNIQUE NOT NULL);'''
    cur.execute(statement)

    statement = '''CREATE TABLE 'PublicResponse' (
                    'id' INTEGER PRIMARY KEY AUTOINCREMENT,
                    'detail' TEXT UNIQUE NOT NULL); '''
    cur.execute(statement)

    statement = '''CREATE TABLE 'SubIssue' (
                    'id' INTEGER PRIMARY KEY AUTOINCREMENT,
                    'name' TEXT UNIQUE NOT NULL,
                    'issue_id' INTEGER NOT NULL);'''
    cur.execute(statement)

    statement = '''CREATE TABLE 'Issue' (
                    'id' INTEGER PRIMARY KEY AUTOINCREMENT,
                    'name' TEXT UNIQUE NOT NULL);'''
    cur.execute(statement)

    statement = '''CREATE TABLE 'SubProduct' (
                    'id' INTEGER PRIMARY KEY AUTOINCREMENT,
                    'name' TEXT UNIQUE NOT NULL,
                    'product_id' INTEGER NOT NULL);'''
    cur.execute(statement)

    statement = '''CREATE TABLE 'Product' (
                    'id' INTEGER PRIMARY KEY AUTOINCREMENT,
                    'name' TEXT UNIQUE NOT NULL);'''
    cur.execute(statement)

    statement = '''CREATE TABLE 'Complaints' (
                    'id' INTEGER PRIMARY KEY,
                    'product_id' INTEGER NOT NULL,
                    'sub_product_id' INTEGER,
                    'issue_id' INTEGER NOT NULL,
                    'sub_issue_id' INTEGER,
                    'complaint_detail' TEXT,
                    'public_response_id' INTEGER,
                    'company_id' INTEGER,
                    'state_id' INTEGER,
                    'zipcode_id' INTEGER,
                    'tag_id' INTEGER,
                    'consumer_consent_provided' INTEGER,
                    'submitted_via_id' INTEGER,
                    'date_sent_to_company' TEXT,
                    'date_received' TEXT,
                    'response_to_consumer_id' INTEGER,
                    'timely_resposne' INTEGER,
                    'consumer_disputed' INTEGER
                    );'''
    cur.execute(statement)
    conn.commit()
    conn.close()

def prepare_key(conn, cur, table, content, additional_id=None):
    if not content:
        return None
    statement = ""
    valueset = tuple()
    if additional_id:
        statement = "INSERT INTO {} VALUES (?, ? ,?)".format(table)
        valueset = (None, content, additional_id)
    else:
        statement = "INSERT INTO {} VALUES (? ,?)".format(table)
        valueset = (None, content)
    try:
        cur.execute(statement, valueset)
        conn.commit()
        return int(cur.lastrowid)
    except Exception as e:
        try:
            cur.execute("SELECT id FROM {} WHERE name=?".format(table), (content,))
            return int(cur.fetchone()[0])
        except Exception as e:
            cur.execute("SELECT id FROM {} WHERE detail=?".format(table), (content,))
            return int(cur.fetchone()[0])



def insert_data():
    conn = sqlite3.connect("ConsumerComplaintsSmall.sqlite")
    cur = conn.cursor()
    with open("ConsumerComplaintsSmall.csv", 'r') as f:
        csvReader = csv.reader(f)
        next(csvReader)
        for row in csvReader:
            complaint_id = int(row[-1])
            product_id = prepare_key(conn, cur, "Product", row[1])
            subproduct_id = prepare_key(conn, cur, "SubProduct", row[2], product_id)
            issue_id = prepare_key(conn, cur, "Issue", row[3])
            subissue_id = prepare_key(conn, cur, "SubIssue", row[4], issue_id)
            public_response_id = prepare_key(conn, cur, "PublicResponse", row[6])
            company_id = prepare_key(conn, cur, "Company", row[7])
            state_id = prepare_key(conn, cur, "State", row[8])
            zipcode_id = prepare_key(conn, cur, "ZipCode", row[9], state_id)
            tag_id = prepare_key(conn, cur, "Tag", row[10])
            submission_id = prepare_key(conn, cur, "SubmissionMethod", row[12])
            company_response_id = prepare_key(conn, cur, "ResponseToConsumer", row[14])
            
            consumer_consent_provided = None
            if row[11]:
                if row[11].strip().upper() == "CONSENT PROVIDED":
                    consumer_consent_provided = 1
                elif row[11].strip().upper() == "CONSENT NOT PROVIDED":
                    consumer_consent_provided = 0

            timely_resposne = 0
            if row[15]:
                if row[15].strip().upper() == "YES":
                    timely_resposne = 1
            else:
                timely_resposne = None
            
            consumer_disputed = None
            if row[16]:
                if row[16].strip().upper() == "YES":
                    consumer_disputed = 1
                elif row[16].strip().upper() == "NO":
                    consumer_disputed = 0
            statement = "INSERT INTO 'Complaints' VALUES (?{})".format(",?"*17)
            cur.execute(statement, (complaint_id, product_id, subproduct_id, issue_id,
                                    subissue_id, row[5], public_response_id, company_id,
                                    state_id, zipcode_id, tag_id, consumer_consent_provided,
                                    submission_id, row[13], row[0], company_response_id,
                                    timely_resposne, consumer_disputed))



    conn.commit()
    conn.close()


if __name__ == "__main__":
    if len(sys.argv) > 1:
        if sys.argv[1] == "init":
            create_table()
        if sys.argv[1] == "insert":
            insert_data()