from database import get_connection

class GameHistory:

    @staticmethod
    def save(resultat, tentatives):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
        INSERT INTO historique (resultat, tentatives)
        VALUES (?, ?)
        """, (resultat, tentatives))

        conn.commit()
        conn.close()

    @staticmethod
    def get_all():
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
        SELECT resultat, tentatives, played_at
        FROM historique
        ORDER BY played_at DESC
        """)

        rows = cursor.fetchall()
        conn.close()
        return rows
