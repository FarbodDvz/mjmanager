CREATE TABLE IF NOT EXISTS members (
ncode INTEGER PRIMARY KEY,
name TEXT NOT NULL,
phone TEXT,
join_date TEXT
);

CREATE TABLE IF NOT EXISTS memberships (
id INTEGER PRIMARY KEY AUTOINCREMENT,
member_id INTEGER,
start_date TEXT,
end_date TEXT,
is_active TEXT,
FOREIGN KEY(member_id) REFERENCES members(id)
);

CREATE TABLE IF NOT EXISTS attendance_logs (
id INTEGER PRIMARY KEY AUTOINCREMENT,
member_id INTEGER,
timestamp TEXT,
FOREIGN KEY(member_id) REFERENCES members(id)
);