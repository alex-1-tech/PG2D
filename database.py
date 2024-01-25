import sqlite3


class ScoreTable:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS scores (
                                id INTEGER PRIMARY KEY,
                                nickname TEXT,
                                score INTEGER
                            )''')
        self.conn.commit()

    def addScore(self, nickname, score):
        self.cursor.execute("INSERT INTO scores (nickname, score) VALUES (?, ?)", (nickname, score))
        self.conn.commit()

    def getTopScores(self, limit=5):
        self.cursor.execute("SELECT nickname, score FROM scores ORDER BY score DESC LIMIT ?", (limit,))
        top_scores = self.cursor.fetchall()
        return top_scores
