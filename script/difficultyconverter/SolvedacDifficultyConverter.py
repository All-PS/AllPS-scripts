from config.DatabaseConfig import DatabaseConfig

class SolvedacDifficultyConverter:

    def __init__(self):
        self.dbConnection = DatabaseConfig().getConnection()

    def convert(self):
        try:
            with self.dbConnection.cursor() as cursor:
                select_query = """
                    SELECT p.id, p.platform_id, p.platform_difficulty_id
                    FROM problem p
                    """
                delete_query = """
                    DELETE FROM problem WHERE platform_id = 4
                    """

                cursor.execute(select_query)
                rows = cursor.fetchall()

                for row in rows:
                    id = row[0]
                    platform_id = row[1]
                    difficulty_id = row [2]

                    if (platform_id == 1):
                        update_query = "UPDATE problem SET difficulty_id = %s WHERE id = %s"
                        cursor.execute(update_query, (difficulty_id, id))

                self.dbConnection.commit()

        except Exception as e:
            raise


