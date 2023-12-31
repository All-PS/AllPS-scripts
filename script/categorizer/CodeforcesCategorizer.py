from config.DatabaseConfig import DatabaseConfig

class CodeforcesCategorizer:

    def __init__(self):
        self.dbConnection = DatabaseConfig().getConnection()

    def categorize(self):
        with self.dbConnection.cursor() as cursor:
            delete_query = """
                DELETE FROM problem_category
                WHERE problem_id IN (
                    SELECT * FROM (
                        SELECT p.id
                        FROM problem p
                            INNER JOIN problem_category pc ON p.id = pc.problem_id
                        WHERE p.platform_id = 2
                    ) AS subquery
                )
            """
            cursor.execute(delete_query)
            self.dbConnection.commit()
            print("All deleted.")

            select_query = """
                SELECT p.id, ppc.platform_category_id
                FROM problem p
                    INNER JOIN problem_platform_category ppc ON p.id = ppc.problem_id
                    INNER JOIN platform_category pc ON ppc.platform_category_id = pc.id
                WHERE p.platform_id = 2
                """

            cursor.execute(select_query)
            rows = cursor.fetchall()

            cnt = 0
            for row in rows:
                if row[1] in [208]:  # DP
                    self.insert(cursor, row[0], 1)
                elif row[1] in [219]:  # 구현
                    self.insert(cursor, row[0], 2)
                elif row[1] in [215]:  # 그리디
                    self.insert(cursor, row[0], 3)
                elif row[1] in [212]:  # 완전탐색
                    self.insert(cursor, row[0], 4)
                elif row[1] in [221, 223]:  # 문자열
                    self.insert(cursor, row[0], 5)
                elif row[1] in []:  # 백트래킹
                    self.insert(cursor, row[0], 6)
                elif row[1] in [207, 210]:  # 그래프탐색
                    self.insert(cursor, row[0], 7)
                elif row[1] in [229]:  # 투포인터
                    self.insert(cursor, row[0], 8)
                elif row[1] in [216]:  # 트리
                    self.insert(cursor, row[0], 9)
                elif row[1] in []:  # 우선순위큐
                    self.insert(cursor, row[0], 10)
                elif row[1] in [206]:  # 자료구조
                    self.insert(cursor, row[0], 11)
                elif row[1] in [235]:  # 최단거리
                    self.insert(cursor, row[0], 12)
                elif row[1] in []:  # 누적합
                    self.insert(cursor, row[0], 13)
                elif row[1] in [222, 238]:  # 이진탐색
                    self.insert(cursor, row[0], 14)
                elif row[1] in []:  # 전처리
                    self.insert(cursor, row[0], 15)
                elif row[1] in [213]:  # 수학
                    self.insert(cursor, row[0], 16)
                elif row[1] in []:  # 재귀
                    self.insert(cursor, row[0], 17)
                elif row[1] in [226]:  # 분할정복
                    self.insert(cursor, row[0], 18)
                elif row[1] in [218]:  # 정렬
                    self.insert(cursor, row[0], 19)
                elif row[1] in []:  # 위상정렬
                    self.insert(cursor, row[0], 20)
                elif row[1] in [211]:  # 해싱
                    self.insert(cursor, row[0], 21)
                elif row[1] in [228]:  # 기하학
                    self.insert(cursor, row[0], 22)
                elif row[1] in [209]:  # 분리집합
                    self.insert(cursor, row[0], 23)
                elif row[1] in []:  # 최소신장트리
                    self.insert(cursor, row[0], 24)
                elif row[1] in []:  # 세그먼트트리
                    self.insert(cursor, row[0], 25)
                elif row[1] in [227]:  # 비트마스킹
                    self.insert(cursor, row[0], 26)
                elif row[1] in [224, 225]:  # 유량
                    self.insert(cursor, row[0], 27)

                cnt += 1
                if cnt % 1000 == 0:
                    self.dbConnection.commit()
                    print(f"{cnt} committed.")
                self.dbConnection.commit()
            print("All committed.")

    def insert(self, cursor, problem_id, category_id):
        insert_query = """
            INSERT INTO problem_category(problem_id, category_id) 
            VALUES (%s, %s)
            ON DUPLICATE KEY UPDATE problem_id = problem_id;
        """
        cursor.execute(insert_query, (problem_id, category_id))
