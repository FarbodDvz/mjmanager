CREATE TABLE IF NOT EXISTS members (
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT NOT NULL,
phone TEXT,
fingerprint_id TEXT UNIQUE,
join_date TEXT
);

CREATE TABLE IF NOT EXISTS memberships (
id INTEGER PRIMARY KEY AUTOINCREMENT,
member_id INTEGER,
start_date TEXT,
end_date TEXT,
status TEXT,
FOREIGN KEY(member_id) REFERENCES members(id)
);